songplays_table = """CREATE TABLE IF NOT EXISTS songplays(
    songplay_id INT  NOT NULL UNIQUE,
    start_time INT,
    user_id INT,
    level VARCHAR,
    song_id INT,
    artist_id INT,
    session_id INT,
    location VARCHAR,
    user_agent VARCHAR,
    PRIMARY KEY(songplay_id)
)"""

users_table = """CREATE TABLE IF NOT EXISTS users(
    user_id INT NOT NULL UNIQUE,
    first_name VARCHAR,
    last_name VARCHAR,
    gender VARCHAR,
    level VARCHAR,
    PRIMARY KEY(user_id)
)"""

songs_table = """CREATE TABLE IF NOT EXISTS songs(
    song_id INT NOT NULL UNIQUE,
    title VARCHAR,
    artist_id INT,
    year INT,
    duration INT,
    PRIMARY KEY(song_id)
)"""

artists_table = """CREATE TABLE IF NOT EXISTS artists(
    artist_id INT NOT NULL UNIQUE,
    name VARCHAR,
    location VARCHAR,
    latitude INT,
    longitude INT,
    PRIMARY KEY(artist_id)
)"""

time_table = """CREATE TABLE IF NOT EXISTS time(
    start_time INT,
    hour INT,
    day INT,
    week INT,
    month INT,
    year INT,
    weekday VARCHAR
)"""

songplays_table_drop = """DROP TABLE IF EXISTS songplays"""

users_table_drop = """DROP TABLE IF EXISTS users"""

songs_table_drop = """DROP TABLE IF EXISTS songs"""

artists = """DROP TABLE IF EXISTS artists"""

time = """DROP TABLE IF EXISTS time"""
