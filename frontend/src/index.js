import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

// Create the root element
const root = ReactDOM.createRoot(document.getElementById('root'));

// Render the app
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// Performance monitoring disabled for simplicity
// If you want to enable it, install web-vitals: npm install web-vitals
