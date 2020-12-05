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
    if video_game_found and row['Year'] != 'N/A':
        video_game_id = video_game_found['id']
        for key in row:
            if 'Sales' in key:
                cursor.execute(f'''
                    SELECT id FROM video_game_sales.region
                    WHERE name = "{key}"
                ''')
                region_id = cursor.fetchone()['id']

                cursor.execute(f'''
                    SELECT * FROM video_game_sales.video_game_sales 
                    WHERE video_game_id = {video_game_id} 
                    AND region_id = {region_id}
                ''')
                video_game_sales_found = cursor.fetchone()
                if not video_game_sales_found:
                    sales = row[key]
                    cursor.execute(f'''
                        INSERT INTO video_game_sales.video_game_sales (
                            video_game_id,
                            region_id,
                            sales
                        ) VALUES (
                            {video_game_id},
                            {region_id},
                            {sales}
                        );
                    ''')
client.commit()
