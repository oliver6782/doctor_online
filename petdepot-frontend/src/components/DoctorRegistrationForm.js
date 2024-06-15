// src/components/DoctorRegistrationForm.js

import React, { useState } from 'react';
import axios from 'axios';

const DoctorRegistrationForm = () => {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
        specialization: '',
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('/api/register/doctor/', formData)
            .then(response => {
                console.log('Doctor registered successfully:', response.data);
            })
            .catch(error => {
                console.error('There was an error registering the doctor!', error);
            });
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                name="username"
                placeholder="Username"
                value={formData.username}
                onChange={handleChange}
            />
            <input
                type="email"
                name="email"
                placeholder="Email"
                value={formData.email}
                onChange={handleChange}
            />
            <input
                type="password"
                name="password"
                placeholder="Password"
                value={formData.password}
                onChange={handleChange}
            />
            <input
                type="text"
                name="specialization"
                placeholder="Specialization"
                value={formData.specialization}
                onChange={handleChange}
            />
            <button type="submit">Register</button>
        </form>
    );
};

export default DoctorRegistrationForm;
