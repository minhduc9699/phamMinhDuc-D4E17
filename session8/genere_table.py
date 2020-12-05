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
    genere_name = row['Genre']
    cursor.execute(f'''
        SELECT id FROM video_game_sales.genere
        WHERE name = "{genere_name}"
    ''')
    platform_found = cursor.fetchone()
    # Load
    if not platform_found:
        cursor.execute(f'''
            INSERT INTO video_game_sales.genere (
                name
            ) VALUES (
                "{genere_name}"
            )
        ''')
client.commit()
