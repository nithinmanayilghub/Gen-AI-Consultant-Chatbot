// src/components/ChatContainer.jsx
import React from 'react';

const ChatContainer = ({ children }) => {
  return (
    <div className="flex flex-col h-full p-4 bg-gray-100 rounded-lg shadow-md">
      {children}
    </div>
  );
};

export default ChatContainer;
