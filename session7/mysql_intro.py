import pymysql
from pymongo import MongoClient

client = pymysql.connect(
    host='localhost', 
    port=3306,
    user='root',
    password='@gmail.com'
)

cursor = client.cursor()

# cursor.execute('CREATE DATABASE first_mysql_db')

# cursor.execute('''
#     CREATE TABLE first_mysql_db.kpop_idol (
#         id INT(11) PRIMARY KEY AUTO_INCREMENT,
#         profile varchar(500),
#         stage_name varchar(500),
#         full_name varchar(500),
#         korean_name varchar(500)
#     )
# ''')

cursor.execute('''
    INSERT INTO first_mysql_db.kpop_idol (
        profile, 
        stage_name, 
        full_name, 
        korean_name
    ) VALUES (
        "https://dbkpop.com/db/k-pop-idols-born-in-2002",
        "PSY",
        "PSYYYYY",
        "khong biet tieng han"
    )
''')

client.commit()
