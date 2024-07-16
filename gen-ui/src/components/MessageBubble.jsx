// src/components/MessageBubble.jsx
import React from 'react';

const MessageBubble = ({ message, isUser }) => {
  const bubbleClass = isUser ? 'bg-blue-500 text-white' : 'bg-gray-300 text-black';

  return (
    <div className={`p-3 rounded-lg mb-2 max-w-md ${bubbleClass} self-${isUser ? 'end' : 'start'}`}>
      {message}
    </div>
  );
};

export default MessageBubble;
