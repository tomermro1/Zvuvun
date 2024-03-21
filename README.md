***חימוש הזבובון***	

טיל חימוש חדש "זבובון"
פצצות חכמות המסוגלות להגיע אל מטרתן באמצעות תעופה בליסטית.

נגיש לכם מערכת מטה שדה לחישוב מיקום הפגיעה המדויק של החימוש
על בסיס קלט.

שלב 1 לוגיקה עסקית:

סעיפים 1-3, מצורף בקוד assignment.py


סעיף 4:
על מנת לוודא כי המוצר שבנינו מוסר תשובות נכונות ,
נציב קלטים שונים וננסה לבדוק מקרי קצה. 

מקרי הקצה שאני חושב עליהם:
$$R=(v^2  sin⁡(2θ))/g$$
כיוון שנוסחאת המרחק האופקי תלויה בסינוס
זוית של 45 מעלות, אשר מייצגת את הגובה המקסימלי
זוית של 90 מעלות,אשר תאפס את הסינוס
נרצה לבדוק מה יקרה עם התוכנה כאשר נציב נתונים אלו

נוסחאת הגובה האנכי
$$H=(v^2  sin^2⁡θ)/g\$$
זוית של 90 מעלות תיתן את הגובה המירבי
מהירות 0 או קרובה ל0,בדיקה של מהירויות גבוהות
בדיקה של גובה שלילי.
נוכל להתמודד עם  מקרי הקצה על ידי: לבדוק יחידות שהם תואמות לנוסחא, לבדוק שהנוסחאות מיושמות טוב בקוד.
אם יש בעיה כלשהי באחת הנוסחאות במקרי קיצון לחשוב על לטפל במקרי קצה בנפרד באמצעות 
Try except  או בתוך לולאות (if while)

סעיף 5 :
כדאי להשתמש בנוסחאות שמשתמשות בהתחשבות האוויר כמו כוחות גרירה.
או למדוד בצורה איטרטיבית כלומר לא לפי נוסחאות אלא בדרכים של מדידות.
לבדוק שימוש בנוסחאות שבהם משתנים הגורמים הקבועים אותם אנו מכירים 
כי בעולם מושלם כוח הכבידה יכול להשתנות.

שלב 2-ארכיטקטורה:

סעיף 4:

![image](https://github.com/tomermro1/Zvuvun/assets/104527765/b5aa2a4d-092a-4fab-9855-5f7584199c1e)

סעיף 1:מצורף באיור

![סעיף 3](https://github.com/tomermro1/Zvuvun/blob/main/q33.jpg?raw=true)
