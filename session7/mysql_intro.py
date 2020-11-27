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
#     CREATE TABLE first_mysql_db.movie (
#         id INT(11) PRIMARY KEY AUTO_INCREMENT,
#         title varchar(255),
#         writer varchar(255)
#     )
# ''')

# cursor.execute('''
#     CREATE TABLE first_mysql_db.actor (
#         id INT(11) PRIMARY KEY AUTO_INCREMENT,
#         name varchar(255),
#         age varchar(255)
#     )
# ''')

cursor.execute('''
    CREATE TABLE first_mysql_db.movie_actor (
        movie_id INT(11),
        actor_id INT(11),
        FOREIGN KEY (movie_id) REFERENCES first_mysql_db.movie (id),
        FOREIGN KEY (actor_id) REFERENCES first_mysql_db.actor (id)
    )
''')

# ETL
# Extract
# mongo_client = MongoClient('localhost', 27017)
# mongo_db = mongo_client.get_database('kpopdatabase1')
# kpop_collection = mongo_db.get_collection('kpop_idol')

# kpop_data = kpop_collection.find({
#     "profile": {'$exists': True}, 
#     "stage_name": {'$exists': True}
# })

# # Transform
# for d in kpop_data:
#     if "thumbnail" in d:
#         d["profile"] = d["thumbnail"]
#     # Load
#     cursor.execute(f'''
#         INSERT INTO first_mysql_db.kpop_idol (
#             profile, 
#             stage_name, 
#             full_name, 
#             korean_name
#         ) VALUES (
#             "{d['profile']}",
#             "{d['stage_name']}",
#             "{d['full_name']}",
#             "{d['korean_name']}"
#         )
#     ''')

# client.commit()
