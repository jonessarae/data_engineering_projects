# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
                                                               
user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id varchar(255) PRIMARY KEY, \
                                                          first_name varchar(255), \
                                                          last_name varchar(255), \
                                                          gender varchar(1), \
                                                          level varchar(50));""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id varchar(255) PRIMARY KEY, \
                                                          title varchar(255), \
                                                          artist_id varchar(255) NOT NULL, \
                                                          year int, \
                                                          duration double precision);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id varchar(255) PRIMARY KEY, \
                                                              name varchar(255), \
                                                              location varchar(255), \
                                                              latitude double precision, \
                                                              longitude double precision);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time timestamp PRIMARY KEY, \
                                                         hour int, \
                                                         day int, \
                                                         week int, \
                                                         month int, \
                                                         year int, \
                                                         weekday varchar(10));""")

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id serial PRIMARY KEY, \
                                                                  start_time timestamp NOT NULL, \
                                                                  user_id varchar(255) NOT NULL, \
                                                                  level varchar(50), \
                                                                  song_id varchar(255), \
                                                                  artist_id varchar(255), \
                                                                  session_id bigint NOT NULL, \
                                                                  location varchar(255), \
                                                                  user_agent text);""")
# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time, user_id, level, song_id, \
                            artist_id, session_id, location, user_agent) \
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) \
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (user_id) DO UPDATE SET first_name=users.first_name, last_name=users.last_name, \
                        gender=users.gender, level=users.level""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) \
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (song_id) DO UPDATE SET title=songs.title, artist_id=songs.artist_id, \
                        year=songs.year, duration=songs.duration """)

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude) \
                          VALUES (%s, %s, %s, %s, %s)
                          ON CONFLICT (artist_id) DO UPDATE SET name=artists.name, location=artists.location, \
                          latitude=artists.latitude, longitude=artists.longitude""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) \
                          VALUES (%s, %s, %s, %s, %s, %s, %s)
                          ON CONFLICT (start_time) DO NOTHING""")

# FIND SONGS

song_select = ("""SELECT s.song_id songid, s.artist_id artistid \
                  FROM songs s INNER JOIN artists a ON s.artist_id = a.artist_id \
                  WHERE s.title = %s AND a.name = %s AND s.duration = %s""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
