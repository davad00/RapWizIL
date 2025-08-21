import React, { useState } from 'react';
import styled from 'styled-components';

const VisualizationContainer = styled.div`
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

const TabContainer = styled.div`
  display: flex;
  margin-bottom: 20px;
  border-bottom: 2px solid #f0f0f0;
`;

const Tab = styled.button`
  padding: 10px 20px;
  border: none;
  background: none;
  font-family: 'Rubik', sans-serif;
  font-size: 1rem;
  cursor: pointer;
  border-bottom: 2px solid transparent;
  transition: all 0.3s ease;
  
  ${props => props.active && `
    border-bottom-color: #667eea;
    color: #667eea;
    font-weight: 600;
  `}
  
  &:hover {
    color: #667eea;
  }
`;

const LyricsContainer = styled.div`
  flex: 1;
  overflow-y: auto;
  max-height: 400px;
`;

const LineContainer = styled.div`
  margin-bottom: 15px;
  padding: 10px;
  border-radius: 8px;
  transition: background-color 0.2s ease;
  
  &:hover {
    background-color: rgba(102, 126, 234, 0.05);
  }
`;

const LineNumber = styled.span`
  display: inline-block;
  width: 30px;
  color: #999;
  font-size: 0.9rem;
  margin-left: 10px;
`;

const LineText = styled.div`
  display: inline;
  font-size: 1.1rem;
  line-height: 1.6;
`;

const RhymeWord = styled.span`
  padding: 2px 6px;
  border-radius: 4px;
  font-weight: 600;
  transition: all 0.2s ease;
  cursor: pointer;
  
  ${props => {
    const colors = {
      'A': '#FF6B6B',
      'B': '#4ECDC4',
      'C': '#45B7D1',
      'D': '#96CEB4',
      'E': '#FECA57',
      'F': '#FF9FF3',
      'G': '#54A0FF',
      'H': '#5F27CD'
    };
    const color = colors[props.rhymeGroup] || '#ddd';
    return `
      background-color: ${color}20;
      border: 2px solid ${color}60;
      color: #333;
    `;
  }}
  
  &:hover {
    transform: scale(1.05);
    ${props => {
      const colors = {
        'A': '#FF6B6B',
        'B': '#4ECDC4',
        'C': '#45B7D1',
        'D': '#96CEB4',
        'E': '#FECA57',
        'F': '#FF9FF3',
        'G': '#54A0FF',
        'H': '#5F27CD'
      };
      const color = colors[props.rhymeGroup] || '#ddd';
      return `background-color: ${color}40;`;
    }}
  }
`;

const StatisticsContainer = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 15px;
  margin-top: 20px;
`;

const StatCard = styled.div`
  background: #f8f9fa;
  padding: 15px;
  border-radius: 8px;
  text-align: center;
`;

const StatValue = styled.div`
  font-size: 1.5rem;
  font-weight: 700;
  color: #667eea;
  margin-bottom: 5px;
`;

const StatLabel = styled.div`
  font-size: 0.9rem;
  color: #666;
`;

const RhymeSchemeDisplay = styled.div`
  font-size: 1.2rem;
  font-weight: 600;
  letter-spacing: 3px;
  text-align: center;
  padding: 15px;
  background: #f8f9fa;
  border-radius: 8px;
  margin-bottom: 20px;
  color: #333;
`;

const RhymeGroupsContainer = styled.div`
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-top: 20px;
`;

const RhymeGroup = styled.div`
  background: #f8f9fa;
  padding: 15px;
  border-radius: 8px;
  flex: 1;
  min-width: 200px;
`;

const RhymeGroupTitle = styled.h4`
  margin: 0 0 10px 0;
  color: #333;
  font-size: 1.1rem;
`;

const RhymeGroupWords = styled.div`
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
`;

const RhymeGroupWord = styled.span`
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.9rem;
  font-weight: 500;
  
  ${props => {
    const colors = {
      'A': '#FF6B6B',
      'B': '#4ECDC4',
      'C': '#45B7D1',
      'D': '#96CEB4',
      'E': '#FECA57',
      'F': '#FF9FF3',
      'G': '#54A0FF',
      'H': '#5F27CD'
    };
    const color = colors[props.group] || '#ddd';
    return `
      background-color: ${color}30;
      color: #333;
    `;
  }}
`;

function LyricsVisualization({ analysis }) {
  const [activeTab, setActiveTab] = useState('lyrics');

  if (!analysis) {
    return (
      <div style={{ textAlign: 'center', color: '#666', padding: '40px' }}>
        אין נתונים להצגה
      </div>
    );
  }

  if (analysis.error) {
    return (
      <div style={{ textAlign: 'center', color: '#e74c3c', padding: '40px' }}>
        שגיאה: {analysis.error}
      </div>
    );
  }

  const renderLyricsView = () => (
    <>
      {analysis.rhyme_scheme && (
        <RhymeSchemeDisplay>
          סכמת החריזה: {analysis.rhyme_scheme}
        </RhymeSchemeDisplay>
      )}
      
      <LyricsContainer>
        {analysis.lines?.map((line, index) => (
          <LineContainer key={index}>
            <LineNumber>{line.line_number}</LineNumber>
            <LineText>
              {line.text.split(' ').map((word, wordIndex) => {
                const isEndWord = line.end_word && word.includes(line.end_word.text);
                const rhymeGroup = line.rhyme_group;
                
                if (isEndWord && rhymeGroup && rhymeGroup !== '-') {
                  return (
                    <React.Fragment key={wordIndex}>
                      <RhymeWord 
                        rhymeGroup={rhymeGroup}
                        title={`חרוז ${rhymeGroup}: ${line.end_word?.phonetic || ''}`}
                      >
                        {word}
                      </RhymeWord>
                      {wordIndex < line.text.split(' ').length - 1 && ' '}
                    </React.Fragment>
                  );
                }
                
                return (
                  <React.Fragment key={wordIndex}>
                    {word}
                    {wordIndex < line.text.split(' ').length - 1 && ' '}
                  </React.Fragment>
                );
              })}
            </LineText>
          </LineContainer>
        ))}
      </LyricsContainer>
      
      {analysis.rhyme_groups && Object.keys(analysis.rhyme_groups).length > 0 && (
        <RhymeGroupsContainer>
          {Object.entries(analysis.rhyme_groups).map(([group, words]) => (
            <RhymeGroup key={group}>
              <RhymeGroupTitle>חרוז {group}</RhymeGroupTitle>
              <RhymeGroupWords>
                {words.map((word, index) => (
                  <RhymeGroupWord key={index} group={group}>
                    {word}
                  </RhymeGroupWord>
                ))}
              </RhymeGroupWords>
            </RhymeGroup>
          ))}
        </RhymeGroupsContainer>
      )}
    </>
  );

  const renderStatsView = () => (
    <StatisticsContainer>
      <StatCard>
        <StatValue>{analysis.statistics?.total_lines || 0}</StatValue>
        <StatLabel>שורות</StatLabel>
      </StatCard>
      
      <StatCard>
        <StatValue>{analysis.statistics?.total_words || 0}</StatValue>
        <StatLabel>מילים</StatLabel>
      </StatCard>
      
      <StatCard>
        <StatValue>{analysis.statistics?.unique_rhymes || 0}</StatValue>
        <StatLabel>חרוזים ייחודיים</StatLabel>
      </StatCard>
      
      <StatCard>
        <StatValue>{analysis.rhyme_scheme || 'לא זוהה'}</StatValue>
        <StatLabel>סכמת חריזה</StatLabel>
      </StatCard>
    </StatisticsContainer>
  );

  return (
    <VisualizationContainer>
      <Title>ניתוח החרוזים</Title>
      
      <TabContainer>
        <Tab 
          active={activeTab === 'lyrics'} 
          onClick={() => setActiveTab('lyrics')}
        >
          טקסט מנותח
        </Tab>
        <Tab 
          active={activeTab === 'stats'} 
          onClick={() => setActiveTab('stats')}
        >
          סטטיסטיקות
        </Tab>
      </TabContainer>
      
      {activeTab === 'lyrics' ? renderLyricsView() : renderStatsView()}
    </VisualizationContainer>
  );
}

export default LyricsVisualization;
