import pyexcel
import pymysql

client = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='@gmail.com',
)

cursor = client.cursor()

# Extract 
data_source = pyexcel.get_records(file_name='vgsales.csv')
for row in data_source:
    publisher_name = row['Publisher']
    cursor.execute(f'''
        SELECT id FROM video_game_sales.publisher
        WHERE name = "{publisher_name}"
    ''')
    platform_found = cursor.fetchone()
    # Load
    if not platform_found:
        cursor.execute(f'''
            INSERT INTO video_game_sales.publisher (
                name
            ) VALUES (
                "{publisher_name}"
            )
        ''')
client.commit()
