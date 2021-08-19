import os
import glob
import json
import psycopg2
import numpy as np
import pandas as pd
from sql_queries import songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert, song_select
from datetime import datetime


def process_song_file(cur, filepath):
    """
    Process songs files and insert records into the Postgres database.
    :param cur: cursor reference
    :param filepath: complete list of file path for the file to load
    """
    song_list = []
    for file in filepath:
        with open(file) as file_open:
            file_load = json.load(file_open)
            song_list.append(file_load)

    df = pd.DataFrame(song_list)

    for value in df.values:
        num_songs, artist_id, artist_latitude, artist_longitude, artist_location, artist_name, song_id, title, duration, year = value

        # insert song record
        song_data = (song_id, title, artist_id, year, duration)
        cur.execute(song_table_insert, song_data)

        # insert artist record
        artist_data = (artist_id, artist_name, artist_location, artist_latitude, artist_longitude)
        cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    Process logs files and insert records into the Postgres database.
    :param cur: cursor reference
    :param filepath: complete list of file path for the file to load
    """

    for file in filepath:
        df = pd.read_json(file, lines=True)
        df = df[df['page'] == "NextSong"].astype({'ts': 'datetime64[ms]'})

        for value in df.values:
            artist, auth, first_name, gender, item_in_session, last_name, \
            length, level, location, method, page, registration, \
            session_id, song, status, ts, user_agent, user_id = value

            time_data = (ts, ts.hour, ts.day, ts.weekofyear, ts.month, ts.year, ts.day_name())

            # insert time record
            cur.execute(time_table_insert, time_data)

            # insert artist record
            user_data = (user_id, first_name, last_name, gender, level)
            cur.execute(user_table_insert, user_data)

            start_time = ts

            cur.execute(song_select, (song, artist, length))
            results = cur.fetchone()

            if results:
                song_id, artist_id = results
            else:
                song_id, artist_id = None, None

            # insert songplay record
            songplay_data = (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
            cur.execute(songplay_table_insert, songplay_data)



def process_data(cur, conn, filepath, func):
    """
    Driver function to load data from songs and event log files into Postgres database.
    :param cur: a database cursor reference
    :param conn: database connection reference
    :param filepath: parent directory where the files exists
    :param func: function to call
    """
    # get all files matching extension from directory

    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    all_filepath = all_files
    func(cur, all_filepath)

def main():
    """
    Driver function for loading songs and log data into Postgres database
    """
    conn = psycopg2.connect("user=postgres \
                            host=127.0.0.1 \
                            port=5432 \
                            dbname=sparkify_db \
                            password=passryme1")
    cur = conn.cursor()
    conn.set_session(autocommit=True)

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()
    cur.close()
    print("Finished processing!!!")

if __name__ == "__main__":
    main()
