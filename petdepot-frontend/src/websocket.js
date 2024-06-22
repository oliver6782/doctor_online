// src/websocket.js
class WebSocketInstance {
    constructor() {
      this.socketRef = null;
      this.connect();
    }
  
    connect() {
      const path = 'ws://localhost:8000/ws/chat/some-room/'; // Adjust this URL to your WebSocket endpoint
      this.socketRef = new WebSocket(path);
  
      this.socketRef.onopen = () => {
        console.log('WebSocket connection established');
      };
  
      this.socketRef.onclose = (e) => {
        console.log('WebSocket connection closed', e);
        this.connect();
      };
  
      this.socketRef.onerror = (e) => {
        console.log('WebSocket error', e);
      };
  
      this.socketRef.onmessage = (e) => {
        this.onMessage(e);
      };
    }
  
    disconnect() {
      if (this.socketRef) {
        this.socketRef.close();
      }
    }
  
    send(data) {
      try {
        this.socketRef.send(data);
      } catch (err) {
        console.error(err.message);
      }
    }
  
    onMessage(event) {
      // Implement this in Chat component to handle incoming messages
    }
  
    getState() {
      return this.socketRef.readyState;
    }
  
    waitForSocketConnection(callback) {
      const socket = this.socketRef;
      const recursion = this.waitForSocketConnection;
      setTimeout(() => {
        if (socket.readyState === 1) {
          callback();
        } else {
          console.log('waiting for connection...');
          recursion(callback);
        }
      }, 1); // wait 1 millisecond for the connection...
    }
  }
  
  export default WebSocketInstance;
  