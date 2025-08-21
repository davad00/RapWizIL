import React, { useState } from 'react';
import styled from 'styled-components';
import { Toaster, toast } from 'react-hot-toast';
import Header from './components/Header';
import LyricsInput from './components/LyricsInput';
import LyricsVisualization from './components/LyricsVisualization';
import LoadingSpinner from './components/LoadingSpinner';
import { analyzeLyrics } from './utils/api';
import './styles/global.css';

const AppContainer = styled.div`
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  font-family: 'Rubik', sans-serif;
  direction: rtl;
`;

const MainContent = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  display: grid;
  grid-template-columns: 1fr;
  gap: 20px;
  
  @media (min-width: 768px) {
    grid-template-columns: 1fr 1fr;
    padding: 40px 20px;
  }
`;

const ContentCard = styled.div`
  background: rgba(255, 255, 255, 0.95);
  border-radius: 15px;
  padding: 30px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
`;

function App() {
  const [lyrics, setLyrics] = useState('');
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!lyrics.trim()) {
      toast.error('אנא הכניסו טקסט לניתוח');
      return;
    }

    setLoading(true);
    
    try {
      const result = await analyzeLyrics(lyrics);
      
      if (result.success) {
        setAnalysis(result.data);
        toast.success('הניתוח הושלם בהצלחה!');
      } else {
        toast.error(result.error || 'שגיאה בניתוח הטקסט');
        setAnalysis(null);
      }
    } catch (error) {
      console.error('Analysis error:', error);
      toast.error('שגיאה בחיבור לשרת');
      setAnalysis(null);
    } finally {
      setLoading(false);
    }
  };

  const handleClear = () => {
    setLyrics('');
    setAnalysis(null);
  };

  return (
    <AppContainer>
      <Toaster 
        position="top-center"
        toastOptions={{
          duration: 4000,
          style: {
            fontFamily: 'Rubik, sans-serif',
            direction: 'rtl'
          }
        }}
      />
      
      <Header />
      
      <MainContent>
        <ContentCard>
          <LyricsInput
            lyrics={lyrics}
            onLyricsChange={setLyrics}
            onAnalyze={handleAnalyze}
            onClear={handleClear}
            loading={loading}
          />
        </ContentCard>
        
        <ContentCard>
          {loading ? (
            <LoadingSpinner />
          ) : analysis ? (
            <LyricsVisualization analysis={analysis} />
          ) : (
            <div style={{ 
              textAlign: 'center', 
              color: '#666', 
              padding: '60px 20px',
              fontSize: '18px'
            }}>
              הכניסו טקסט ראפ עברי כדי לראות את ניתוח החרוזים
            </div>
          )}
        </ContentCard>
      </MainContent>
    </AppContainer>
  );
}

export default App;
