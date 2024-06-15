// src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import UserRegistrationForm from './components/UserRegistrationForm';
import DoctorRegistrationForm from './components/DoctorRegistrationForm';

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/register/common/" element={<UserRegistrationForm />} />
                <Route path="/register/doctor/" element={<DoctorRegistrationForm />} />
            </Routes>
        </Router>
    );
};

export default App;
