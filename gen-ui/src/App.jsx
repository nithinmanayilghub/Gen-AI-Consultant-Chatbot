// src/App.jsx
import React, { useState } from 'react';
import ChatContainer from './components/ChatContainer';
import MessageBubble from './components/MessageBubble';
import MessageInput from './components/MessageInput';
import api from './api';

const App = () => {
  const [messages, setMessages] = useState([]);

  const sendMessage = async (message) => {
    setMessages([...messages, { message, isUser: true }]);

    const requestBody = {
      input_data: message,
      session_id: "37", // sessionId,
    };

    try {
      const response = await api.post('/api/chain/invoke', requestBody);
      setMessages((prev) => [...prev, { message: response.result, isUser: false }]);
    } catch (error) {
      console.error('Error sending message:', error);
      setMessages((prev) => [...prev, { message: 'Error sending message', isUser: false }]);
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-200">
      <div className="w-full max-w-lg">
        <ChatContainer>
          {messages.map((msg, index) => (
            <MessageBubble key={index} message={msg.message} isUser={msg.isUser} />
          ))}
        </ChatContainer>
        <MessageInput onSend={sendMessage} />
      </div>
    </div>
  );
};

export default App;
