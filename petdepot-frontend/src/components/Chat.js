// src/Chat.js
import React, { useState, useEffect, useRef } from 'react';
import WebSocketInstance from './websocket';

const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [message, setMessage] = useState('');
  const [petId, setPetId] = useState('');
  const [symptomDescription, setSymptomDescription] = useState('');
  const [diagnose, setDiagnose] = useState('');
  const [instructions, setInstructions] = useState('');
  const [expiryDate, setExpiryDate] = useState('');
  const [petCard, setPetCard] = useState(null);

  const ws = useRef(null);

  useEffect(() => {
    ws.current = new WebSocketInstance();
    ws.current.onopen = () => console.log('WebSocket connection established');
    ws.current.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setMessages((prevMessages) => [...prevMessages, data]);
    };
    ws.current.onclose = () => console.log('WebSocket connection closed');
    ws.current.onerror = (error) => console.error('WebSocket error', error);

    return () => {
      ws.current.close();
    };
  }, []);

  const fetchPetCard = (petId) => {
    // Replace with your API endpoint to fetch pet details
    fetch(`/api/pets/${petId}/`)
      .then(response => response.json())
      .then(data => setPetCard(data))
      .catch(error => console.error('Error fetching pet details:', error));
  };

  const sendMessage = () => {
    const petCardData = petId ? {
      pet_id: petId,
      symptom_description: symptomDescription,
      diagnose: diagnose,
      instructions: instructions,
      expiry_date: expiryDate
    } : null;

    const messageData = {
      message,
      pet_card: petCardData
    };

    ws.current.send(JSON.stringify(messageData));
    setMessage('');
    setPetId('');
    setSymptomDescription('');
    setDiagnose('');
    setInstructions('');
    setExpiryDate('');
  };

  return (
    <div>
      <div id="chat-log">
        {messages.map((msg, index) => (
          <div key={index}>
            {msg.message} {msg.pet_card && `- Pet Card: ${JSON.stringify(msg.pet_card)}`}
          </div>
        ))}
      </div>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type your message"
      />
      <button onClick={sendMessage}>Send</button>
      <div>
        <input
          type="text"
          value={petId}
          onChange={(e) => setPetId(e.target.value)}
          placeholder="Pet ID"
          onBlur={() => fetchPetCard(petId)}
        />
        <input
          type="text"
          value={symptomDescription}
          onChange={(e) => setSymptomDescription(e.target.value)}
          placeholder="Symptom Description"
        />
        <input
          type="text"
          value={diagnose}
          onChange={(e) => setDiagnose(e.target.value)}
          placeholder="Diagnose"
        />
        <input
          type="text"
          value={instructions}
          onChange={(e) => setInstructions(e.target.value)}
          placeholder="Instructions"
        />
        <input
          type="date"
          value={expiryDate}
          onChange={(e) => setExpiryDate(e.target.value)}
          placeholder="Expiry Date"
        />
      </div>
      {petCard && (
        <div className="pet-card">
          <h3>Pet Information</h3>
          <p>Name: {petCard.name}</p>
          <p>Age: {petCard.age}</p>
          <p>Breed: {petCard.breed}</p>
          {/* Add more pet details as necessary */}
        </div>
      )}
    </div>
  );
};

export default Chat;
