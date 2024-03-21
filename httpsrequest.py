import requests

# כתובת ה-URL של התוכנה, כאן נניח שהיא בכתובת localhost על פורט 8080
url = 'http://localhost:8080/'

# מידע שתרצה לשלוח לתוכנה בפורמט JSON
data = {'key': 'value'}

# שליחת בקשת POST לתוכנה
response = requests.post(url, json=data)

# בדיקת תגובת השרת
if response.status_code == 200:
    # הדפסת תוכן התגובה במידה והיא 200 (OK)
    print(response.json())
else:
    # הדפסת הודעת שגיאה במידה והתגובה אינה 200
    print('Error:', response.status_code)