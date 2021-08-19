songplays_table = """CREATE TABLE IF NOT EXISTS songplays(
    songplay_id SERIAL CONSTRAINT songplay_pk PRIMARY KEY,
    start_time TIMESTAMP REFERENCES time (start_time),
    user_id INT REFERENCES users (user_id),
    level VARCHAR NOT NULL,
    song_id VARCHAR REFERENCES songs (song_id),
    artist_id VARCHAR REFERENCES artists (artist_id),
    session_id INT NOT NULL,
    location VARCHAR,
    user_agent TEXT
)"""

users_table = """CREATE TABLE IF NOT EXISTS users(
    user_id INT NOT NULL CONSTRAINT users_pk PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    gender VARCHAR,
    level VARCHAR
)"""

songs_table = """CREATE TABLE IF NOT EXISTS songs(
    song_id VARCHAR CONSTRAINT songs_pk PRIMARY KEY ,
    title VARCHAR,
    artist_id VARCHAR,
    year INT,
    duration FLOAT
)"""

artists_table = """CREATE TABLE IF NOT EXISTS artists(
    artist_id VARCHAR  CONSTRAINT artist_pk PRIMARY KEY,
    artist_name VARCHAR,
    artist_location VARCHAR,
    artist_latitude FLOAT,
    artist_longitude FLOAT
)"""

time_table = """CREATE TABLE IF NOT EXISTS time(
    start_time TIMESTAMP CONSTRAINT time_pk PRIMARY KEY,
    hour INT NOT NULL CHECK (hour >= 0),
    day INT NOT NULL CHECK (day >= 0),
    week INT NOT NULL CHECK (week >= 0),
    month INT NOT NULL CHECK (month >= 0),
    year INT NOT NULL CHECK (year >= 0),
    weekday VARCHAR NOT NULL
)"""

# INSERT RECORDS

songplay_table_insert = """INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s);"""

user_table_insert = """INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;"""

song_table_insert = """INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING;"""

artist_table_insert = """INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO UPDATE SET
                          artist_location = EXCLUDED.artist_location,
                          artist_latitude = EXCLUDED.artist_latitude,
                          artist_longitude = EXCLUDED.artist_longitude;"""

time_table_insert = """INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)  ON CONFLICT (start_time) DO NOTHING;"""


songplays_table_drop = """DROP TABLE IF EXISTS songplays"""

users_table_drop = """DROP TABLE IF EXISTS users"""

songs_table_drop = """DROP TABLE IF EXISTS songs"""

artists_table_drop = """DROP TABLE IF EXISTS artists"""

time_table_drop = """DROP TABLE IF EXISTS time"""

song_select = """
    SELECT s.song_id, a.artist_id
    FROM songs AS s
    JOIN artists AS a
    ON s.artist_id = a.artist_id
    WHERE s.title = %s AND a.artist_name = %s AND s.duration = %s
"""

create_table_queries = [users_table, songs_table, artists_table, time_table, songplays_table]

drop_table_queries = [songplays_table_drop, users_table_drop, songs_table_drop, artists_table_drop, time_table_drop]
