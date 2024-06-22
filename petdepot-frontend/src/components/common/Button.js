import React from 'react';

const Button = ({ onClick, children, type = 'button', className = '' }) => (
  <button type={type} onClick={onClick} className={`btn ${className}`}>
    {children}
  </button>
);

export default Button;
