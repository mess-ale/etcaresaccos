import axios from 'axios';

export default defineNuxtPlugin(() => {
  const instance = axios.create({
    baseURL: process.env.NUXT_PUBLIC_API_BASE_URL || 'http://127.0.0.1:8000/api/', 
    withCredentials: true, // Include cookies in requests
  });

  return {
    provide: {
      axios: instance,
    },
  };
});