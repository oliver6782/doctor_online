import apiClient from './apiClient';

export const registerDoctor = async (doctorData) => {
  try {
    const response = await apiClient.post('register/doctor/', doctorData);
    return response.data;
  } catch (error) {
    console.error('Failed to register doctor:', error);
    throw error;
  }
};

export const fetchDoctors = async () => {
  try {
    const response = await apiClient.get('/doctor');
    return response.data;
  } catch (error) {
    console.error('Failed to fetch doctors:', error);
    throw error;
  }
};
