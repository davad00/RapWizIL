# RapWizIL - Hebrew Rap Visualization Tool

🎵 **ניתוח חרוזים בראפ עברי** - כלי מתקדם לויזואליזציה וניתוח של דפוסים חרוזיים בראפ עברי

## תכונות עיקריות

- 🔍 **ניתוח חרוזים אוטומטי** - זיהוי חרוזים וקיבוץ לפי דמיון פונטי
- 🎨 **ויזואליזציה אינטראקטיבית** - הדגשת חרוזים בצבעים שונים
- 📊 **סכמות חריזה** - זיהוי וייצוג של סכמות חריזה (AABB, ABAB וכו')
- 🔤 **תעתיק פונטי** - המרה לכתב פונטי לצורך ניתוח מדויק
- 📈 **סטטיסטיקות מפורטות** - מידע על מספר שורות, מילים וחרוזים

## טכנולוגיות

### Backend
- **Python 3.8+** עם Flask
- **Phonikud** - מנוע לתעתיק פונטי עברי
- **NLTK** - עיבוד שפה טבעית
- **Flask-CORS** - תמיכה ב-Cross-Origin Requests

### Frontend
- **React 18** - ממשק משתמש מודרני
- **Styled Components** - עיצוב מתקדם
- **D3.js** - ויזואליזציה אינטראקטיבית
- **Axios** - תקשורת עם השרת

## התקנה והרצה

### דרישות מקדימות
- Node.js 16+ 
- Python 3.8+
- npm או yarn

### התקנה מהירה

1. **שכפול הפרויקט**
   ```bash
   git clone https://github.com/yourusername/rapwizil.git
   cd rapwizil
   ```

2. **התקנת כל התלויות**
   ```bash
   npm run install:all
   ```

3. **הרצת הפרויקט**
   ```bash
   npm run dev
   ```

הפרויקט יפתח בכתובת: http://localhost:3000

### התקנה ידנית

#### Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```

#### Frontend
```bash
cd frontend
npm install
npm start
```

## שימוש

1. **הכניסו טקסט ראפ עברי** באזור הטקסט
2. **לחצו על "נתח חרוזים"** כדי להתחיל את הניתוח
3. **צפו בתוצאות** - החרוזים יודגשו בצבעים שונים
4. **עברו ללשונית "סטטיסטיקות"** למידע מפורט

### דוגמת שימוש

```
אני רק רוצה להגיד לך איך
שאת יפה כמו שמיים
אני רק רוצה להגיד לך עכשיו  
שאת חלמת שלי תמיד
```

## API Documentation

### POST /analyze
ניתוח טקסט ראפ עברי

**Request:**
```json
{
  "lyrics": "טקסט ראפ עברי כאן..."
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "lines": [...],
    "rhyme_scheme": "AABB",
    "rhyme_groups": {...},
    "statistics": {...}
  }
}
```

### GET /health
בדיקת תקינות השרת

## פיתוח

### הוספת תכונות חדשות

1. **Backend** - הוסיפו פונקציונליות ב-`hebrew_nlp.py`
2. **Frontend** - צרו קומפוננטות חדשות ב-`src/components/`
3. **API** - הוסיפו endpoints ב-`app.py`

### בדיקות

```bash
# Backend tests
cd backend
python -m pytest

# Frontend tests  
cd frontend
npm test
```

## פריסה (Deployment)

### Heroku
```bash
# התקנת Heroku CLI
npm install -g heroku

# יצירת אפליקציה
heroku create rapwizil

# פריסה
git push heroku main
```

### Docker
```bash
# בניית הדוקר
docker build -t rapwizil .

# הרצה
docker run -p 3000:3000 rapwizil
```

## תרומה לפרויקט

1. צרו Fork של הפרויקט
2. צרו branch חדש (`git checkout -b feature/amazing-feature`)
3. בצעו commit לשינויים (`git commit -m 'Add amazing feature'`)
4. דחפו ל-branch (`git push origin feature/amazing-feature`)
5. פתחו Pull Request

## רישיון

הפרויקט הזה מופץ תחת רישיון MIT. ראו `LICENSE` לפרטים נוספים.

## תמיכה

- 📧 **אימייל**: support@rapwizil.com
- 🐛 **באגים**: [GitHub Issues](https://github.com/yourusername/rapwizil/issues)
- 💬 **דיונים**: [GitHub Discussions](https://github.com/yourusername/rapwizil/discussions)

## יוצרים

- **RapWizIL Team** - פיתוח ועיצוב
- **השראה**: [rapviz](https://github.com/michaelfromyeg/rapviz) by michaelfromyeg

## הכרת תודה

תודה מיוחדת ל:
- צוות [resources.nnlp-il.mafat.ai](https://resources.nnlp-il.mafat.ai) על המשאבים לעיבוד עברית
- פרויקט Phonikud על ה-G2P engine
- קהילת הראפ הישראלית על ההשראה

---

**RapWizIL** - הופך את הראפ העברי לוויזואלי 🎨🎵