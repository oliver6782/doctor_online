import React from 'react';

const Input = ({ type = 'text', value, onChange, placeholder = '', className = '' }) => (
  <input
    type={type}
    value={value}
    onChange={onChange}
    placeholder={placeholder}
    className={`input ${className}`}
  />
);

export default Input;
