import React from 'react';
import styled from 'styled-components';

const HeaderContainer = styled.header`
  text-align: center;
  padding: 40px 20px;
  color: white;
`;

const Title = styled.h1`
  font-size: 3rem;
  font-weight: 700;
  margin: 0 0 10px 0;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
  
  @media (max-width: 768px) {
    font-size: 2rem;
  }
`;

const Subtitle = styled.p`
  font-size: 1.2rem;
  font-weight: 300;
  margin: 0;
  opacity: 0.9;
  
  @media (max-width: 768px) {
    font-size: 1rem;
  }
`;

const Description = styled.p`
  font-size: 1rem;
  font-weight: 400;
  margin: 20px auto 0;
  opacity: 0.8;
  max-width: 600px;
  line-height: 1.6;
  
  @media (max-width: 768px) {
    font-size: 0.9rem;
  }
`;

function Header() {
  return (
    <HeaderContainer>
      <Title>RapWizIL</Title>
      <Subtitle>ניתוח חרוזים בראפ עברי</Subtitle>
      <Description>
        כלי מתקדם לניתוח וויזואליזציה של חרוזים, סכמות חריזה ודפוסים לשוניים בראפ עברי.
        הכניסו את הטקסט שלכם וגלו את המבנה החרוזי והפואטי שלו.
      </Description>
    </HeaderContainer>
  );
}

export default Header;
