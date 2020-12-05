import pyexcel
import pymysql

client = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='@gmail.com',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = client.cursor()

# Extract
data_source = pyexcel.get_records(file_name='vgsales.csv')
for row in data_source:
    video_game_name = row['Name']
    cursor.execute(f'''
        SELECT id FROM video_game_sales.video_game
        WHERE name = "{video_game_name}"
    ''')
    video_game_found = cursor.fetchone()
    if not video_game_found and row['Year'] != 'N/A':
        video_game_year = row['Year']

        cursor.execute(f'''
            SELECT id FROM video_game_sales.platform
            WHERE name = "{row['Platform']}"
        ''')
        platform_id = cursor.fetchone()['id']

        cursor.execute(f'''
            SELECT id FROM video_game_sales.genere
            WHERE name = "{row['Genre']}"
        ''')
        genere_id = cursor.fetchone()['id']

        cursor.execute(f'''
            SELECT id FROM video_game_sales.publisher
            WHERE name = "{row['Publisher']}"
        ''')
        publisher_id = cursor.fetchone()['id']
        cursor.execute(f'''
            INSERT INTO video_game_sales.video_game (
                name,
                platform_id,
                genere_id,
                publisher_id,
                year
            ) VALUES (
                "{video_game_name}",
                {platform_id},
                {genere_id},
                {publisher_id},
                {video_game_year}
            );
        ''')
client.commit()
