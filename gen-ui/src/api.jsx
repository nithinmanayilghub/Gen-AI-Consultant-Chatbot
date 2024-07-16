import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000',
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API error:', error);
    throw error;
  }
); 

export default api;
