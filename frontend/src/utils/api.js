import axios from 'axios';

// API configuration
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 30000, // 30 seconds timeout for analysis
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for logging
api.interceptors.request.use(
  (config) => {
    console.log(`API Request: ${config.method?.toUpperCase()} ${config.url}`);
    return config;
  },
  (error) => {
    console.error('API Request Error:', error);
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => {
    console.log(`API Response: ${response.status} ${response.config.url}`);
    return response;
  },
  (error) => {
    console.error('API Response Error:', error);
    
    if (error.code === 'ECONNABORTED') {
      throw new Error('הבקשה ארכה יותר מדי זמן. אנא נסו שוב.');
    }
    
    if (error.response) {
      // Server responded with error status
      const message = error.response.data?.error || 
                     error.response.data?.message || 
                     'שגיאה בשרת';
      throw new Error(message);
    } else if (error.request) {
      // Request was made but no response received
      throw new Error('לא ניתן להתחבר לשרת. אנא בדקו את החיבור לאינטרנט.');
    } else {
      // Something else happened
      throw new Error('שגיאה לא צפויה. אנא נסו שוב.');
    }
  }
);

/**
 * Analyze Hebrew rap lyrics
 * @param {string} lyrics - The Hebrew lyrics text to analyze
 * @returns {Promise<Object>} Analysis results
 */
export const analyzeLyrics = async (lyrics) => {
  try {
    const response = await api.post('/analyze', {
      lyrics: lyrics.trim()
    });
    
    return response.data;
  } catch (error) {
    console.error('Error analyzing lyrics:', error);
    throw error;
  }
};

/**
 * Check API health status
 * @returns {Promise<Object>} Health status
 */
export const checkHealth = async () => {
  try {
    const response = await api.get('/health');
    return response.data;
  } catch (error) {
    console.error('Error checking health:', error);
    throw error;
  }
};

/**
 * Get basic API info
 * @returns {Promise<Object>} API info
 */
export const getApiInfo = async () => {
  try {
    const response = await api.get('/');
    return response.data;
  } catch (error) {
    console.error('Error getting API info:', error);
    throw error;
  }
};

export default api;
