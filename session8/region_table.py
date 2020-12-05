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
for key in data_source[0]:
    if "Sales" in key:
        cursor.execute(f'''
            SELECT id FROM video_game_sales.region
            WHERE name = "{key}"
        ''')
        region_found = cursor.fetchone()
        # Load
        if not region_found:
            cursor.execute(f'''
                INSERT INTO video_game_sales.region (
                    name
                ) VALUES (
                    "{key}"
                )
            ''')
client.commit()
