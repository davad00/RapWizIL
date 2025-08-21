import React from 'react';
import styled, { keyframes } from 'styled-components';

const spin = keyframes`
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
`;

const pulse = keyframes`
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
`;

const LoadingContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  color: #667eea;
`;

const Spinner = styled.div`
  width: 50px;
  height: 50px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #667eea;
  border-radius: 50%;
  animation: ${spin} 1s linear infinite;
  margin-bottom: 20px;
`;

const LoadingText = styled.div`
  font-size: 1.1rem;
  font-weight: 500;
  animation: ${pulse} 1.5s ease-in-out infinite;
  text-align: center;
`;

const LoadingSubtext = styled.div`
  font-size: 0.9rem;
  color: #999;
  margin-top: 10px;
  text-align: center;
`;

function LoadingSpinner() {
  return (
    <LoadingContainer>
      <Spinner />
      <LoadingText>מנתח את הטקסט...</LoadingText>
      <LoadingSubtext>
        מעבד טקסט עברי, מזהה חרוזים ויוצר ויזואליזציה
      </LoadingSubtext>
    </LoadingContainer>
  );
}

export default LoadingSpinner;
