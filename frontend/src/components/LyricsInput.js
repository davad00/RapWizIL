import React from 'react';
import styled from 'styled-components';

const InputContainer = styled.div`
  display: flex;
  flex-direction: column;
  height: 100%;
`;

const Title = styled.h2`
  color: #333;
  margin: 0 0 20px 0;
  font-size: 1.5rem;
  font-weight: 600;
`;

const TextArea = styled.textarea`
  flex: 1;
  min-height: 300px;
  padding: 20px;
  border: 2px solid #e0e0e0;
  border-radius: 10px;
  font-family: 'Rubik', sans-serif;
  font-size: 1rem;
  line-height: 1.6;
  direction: rtl;
  resize: vertical;
  transition: border-color 0.3s ease;
  
  &:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
  }
  
  &::placeholder {
    color: #999;
  }
`;

const ButtonContainer = styled.div`
  display: flex;
  gap: 15px;
  margin-top: 20px;
  
  @media (max-width: 480px) {
    flex-direction: column;
  }
`;

const Button = styled.button`
  flex: 1;
  padding: 15px 30px;
  border: none;
  border-radius: 8px;
  font-family: 'Rubik', sans-serif;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  
  &:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }
`;

const AnalyzeButton = styled(Button)`
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  
  &:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
  }
  
  &:active:not(:disabled) {
    transform: translateY(0);
  }
`;

const ClearButton = styled(Button)`
  background: #f5f5f5;
  color: #666;
  border: 1px solid #ddd;
  
  &:hover:not(:disabled) {
    background: #e8e8e8;
    color: #333;
  }
`;

const CharacterCount = styled.div`
  text-align: left;
  margin-top: 10px;
  font-size: 0.9rem;
  color: #666;
  direction: ltr;
`;

const ExampleButton = styled.button`
  background: none;
  border: none;
  color: #667eea;
  font-size: 0.9rem;
  cursor: pointer;
  text-decoration: underline;
  margin-bottom: 10px;
  
  &:hover {
    color: #5a6fd8;
  }
`;

const EXAMPLE_LYRICS = `אני רק רוצה להגיד לך איך
שאת יפה כמו שמיים
אני רק רוצה להגיד לך עכשיו
שאת חלמת שלי תמיד

בלילות אני חושב עליך
ובימים את לא עוזבת
מחכה לרגע שאוכל להגיד
שאת האהבה שלי לעד`;

function LyricsInput({ lyrics, onLyricsChange, onAnalyze, onClear, loading }) {
  const handleExampleClick = () => {
    onLyricsChange(EXAMPLE_LYRICS);
  };

  return (
    <InputContainer>
      <Title>הכניסו טקסט ראפ עברי</Title>
      
      <ExampleButton onClick={handleExampleClick}>
        לחצו כאן לדוגמת טקסט
      </ExampleButton>
      
      <TextArea
        value={lyrics}
        onChange={(e) => onLyricsChange(e.target.value)}
        placeholder="הדביקו או הקלידו כאן את מילות הראפ בעברית...

לדוגמה:
אני רק רוצה להגיד לך איך
שאת יפה כמו שמיים
אני רק רוצה להגיד לך עכשיו
שאת חלמת שלי תמיד"
        disabled={loading}
      />
      
      <CharacterCount>
        {lyrics.length} תווים
      </CharacterCount>
      
      <ButtonContainer>
        <AnalyzeButton 
          onClick={onAnalyze} 
          disabled={loading || !lyrics.trim()}
        >
          {loading ? 'מנתח...' : 'נתח חרוזים'}
        </AnalyzeButton>
        
        <ClearButton 
          onClick={onClear} 
          disabled={loading}
        >
          נקה טקסט
        </ClearButton>
      </ButtonContainer>
    </InputContainer>
  );
}

export default LyricsInput;
