import pymysql

client = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='@gmail.com',
)

cursor = client.cursor()

cursor.execute('CREATE DATABASE video_game_sales')

cursor.execute('''
    CREATE TABLE video_game_sales.platform (
        id INT(11) PRIMARY KEY AUTO_INCREMENT,
        name varchar(255)
    )
''')

cursor.execute('''
    CREATE TABLE video_game_sales.publisher (
        id INT(11) PRIMARY KEY AUTO_INCREMENT,
        name varchar(255)
    )
''')

cursor.execute('''
    CREATE TABLE video_game_sales.region (
        id INT(11) PRIMARY KEY AUTO_INCREMENT,
        name varchar(255)
    )
''')

cursor.execute('''
    CREATE TABLE video_game_sales.genere (
        id INT(11) PRIMARY KEY AUTO_INCREMENT,
        name varchar(255)
    )
''')


cursor.execute('''
     CREATE TABLE video_game_sales.video_game (
        id INT(11) PRIMARY KEY AUTO_INCREMENT,
        name varchar(255),
        year INT(11),
        platform_id INT(11),
        publisher_id INT(11),
        genere_id INT(11),
        FOREIGN KEY (platform_id) REFERENCES video_game_sales.platform (id),
        FOREIGN KEY (publisher_id) REFERENCES video_game_sales.publisher (id),
        FOREIGN KEY (genere_id) REFERENCES video_game_sales.genere (id)
    )
''')


cursor.execute('''
    CREATE TABLE video_game_sales.video_game_sales(
        video_game_id INT(11),
        region_id INT(11),
        sales DECIMAL(9,0),
        FOREIGN KEY (video_game_id) REFERENCES video_game_sales.video_game (id),
        FOREIGN KEY (region_id) REFERENCES video_game_sales.region (id),
        PRIMARY KEY (video_game_id, region_id)
    )
''')
