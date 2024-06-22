# chat/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from pets.models import Pet
from prescriptions.serializers import PrescriptionSerializer
from accounts.models import Doctor

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        pet_card = data.get('pet_card')

        if pet_card:
            try:
                pet = Pet.objects.get(id=pet_card['pet_id'])
                doctor = Doctor.objects.get(user=self.scope['user'])
                pet_owner = pet.owner

                # Prescription data entered by the doctor
                prescription_data = {
                    'pet_owner': pet_owner.id,
                    'pet': pet.id,
                    'doctor': doctor.id,
                    'medications': pet_card.get('medications', []),
                    'symptom_description': pet_card.get('symptom_description', ''),
                    'diagnose': pet_card.get('diagnose', ''),
                    'instructions': pet_card.get('instructions', ''),
                    'expiry_date': pet_card['expiry_date'],
                }

                serializer = PrescriptionSerializer(data=prescription_data)
                if serializer.is_valid():
                    serializer.save()
                    prescription_response = serializer.data
                    prescription_response.update({
                        'pet_owner': pet_owner.username,
                        'pet': pet.name,
                        'doctor': doctor.user.username
                    })
                else:
                    prescription_response = serializer.errors

                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'message': message,
                        'pet_card': prescription_response
                    }
                )

            except Pet.DoesNotExist:
                await self.send(text_data=json.dumps({
                    'error': 'Pet not found'
                }))
            except Doctor.DoesNotExist:
                await self.send(text_data=json.dumps({
                    'error': 'Doctor not found'
                }))
        else:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message
                }
            )

    async def chat_message(self, event):
        message = event['message']
        pet_card = event.get('pet_card', None)

        response = {'message': message}
        if pet_card:
            response['pet_card'] = pet_card

        await self.send(text_data=json.dumps(response))
