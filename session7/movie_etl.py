from pymongo import MongoClient
import pymysql

mongo_client = MongoClient('localhost', 27017)

mysql_client = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='@gmail.com',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = mysql_client.cursor()

movie_database = mongo_client.get_database('mongo_pratice')
movie_collection = movie_database.get_collection('movies')

movie_data = movie_collection.find({'actors': {'$exists': True}})

# for movie in movie_data:
#     cursor.execute(f'''
#         INSERT INTO first_mysql_db.movie (
#             title,
#             writer
#         ) VALUES (
#             "{movie['title']}",
#             "{movie['writer']}"
#         )
#     ''')

# for movie in movie_data:
#     for actor in movie["actors"]:
#         cursor.execute(f'''
#             INSERT INTO first_mysql_db.actor (
#                 name,
#                 age
#             ) VALUES (
#                 "{actor}",
#                 "20"
#             )
#         ''')


for movie in movie_data:
    cursor.execute(f'''
        SELECT id FROM first_mysql_db.movie WHERE title="{movie['title']}"
    ''')
    movie_id = cursor.fetchone()
    for actor in movie["actors"]:
        cursor.execute(f'''
            SELECT id FROM first_mysql_db.actor WHERE name="{actor}"
        ''')
        actor_id = cursor.fetchone()
        cursor.execute(f'''
            INSERT INTO first_mysql_db.movie_actor (
                movie_id,
                actor_id
            ) VALUES (
                {movie_id['id']},
                {actor_id['id']}
            )
        ''')



mysql_client.commit()
