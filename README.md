# Data Modeling with Postgres

## Overview

This project entails modeling of data with Postgres and Python's pandas and psycopg2 library was used to build an ETL pipeline for a startup called Sparkify.

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to.

To complete the project, the fact and dimension tables was defined for a star schema which focus on a particular analytic.


## Song Dataset
Songs dataset is a subset of [Million Song Dataset](http://millionsongdataset.com/).

**Sample data :**
```
{"num_songs": 1, "artist_id": "ARDNS031187B9924F0", "artist_latitude": 32.67828, "artist_longitude": -83.22295, "artist_location": "Georgia", "artist_name": "Tim Wilson", "song_id": "SONYPOM12A8C13B2D7", "title": "I Think My Wife Is Running Around On Me (Taco Hell)", "duration": 186.48771, "year": 2005}
```

## Log Dataset
Log dataset was gotten from [Event Simulator](https://github.com/Interana/eventsim).

**Sample Record :**
```
{"artist":"Anjulie","auth":"Logged In","firstName":"Jacqueline","gender":"F","itemInSession":6,"lastName":"Lynch","length":194.63791,"level":"paid","location":"Atlanta-Sandy Springs-Roswell, GA","method":"PUT","page":"NextSong","registration":1540223723796.0,"sessionId":389,"song":"Boom","status":200,"ts":1541991804796,"userAgent":"\"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit\/537.78.2 (KHTML, like Gecko) Version\/7.0.6 Safari\/537.78.2\"","userId":"29"}
```

## Database Star Schema

#### Fact Table
**songplays** - records log data associated with song plays i.e. records with page `NextSong`

```
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
```

#### Dimension Tables

**artists**  - artists in music database
```
artist_id, name, location, latitude, longitude
```

**songs**  - songs in music database
```
song_id, title, artist_id, year, duration
```

**time**  - timestamps of records in  **songplays**  broken down into specific units
```
start_time, hour, day, week, month, year, weekday
```

**users** - users in the app
```
user_id, first_name, last_name, gender, level
```

## Project Files

**sql_queries.py:** contains sql queries for dropping and creating tables. Also, contains insertion and song select query.

**create_tables.py:** contains code for setting up database. Running this file creates sparkify_db and also creates the tables.

**etl.ipynb:** a jupyter notebook to analyse dataset before loading.

**etl.py:** read and process song_data and log_data.

**test.ipynb:** a jupyter notebook to connect to postgres database and validate the data loaded.

## Environment
Python 3.6 or above

PostgresSQL 9.5 or above

Jupyter notebook

psycopg2 - PostgreSQL database Python wrapper.

## How to run
The ```create_tables.py``` and ```etl.py``` file should be run independently as below:
```
python create_tables.py
```
```
python etl.py
```
## Reference
[Psycopg](http://initd.org/psycopg/docs/)

[Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
