#crating music database from iphone xml exported file


import xml.etree.ElementTree as ET
import sqlite3

input_file = input('please enter file address')

file = open(input_file)
fh = file.read()
xml = ET.fromstring(fh)
playlist = xml.findall('dict/dict/dict')


# function to find items in every track according to desired item name
def finder(track, desired):
    flag = False
    for item in track:
        if flag:
            return item.text
        if item.text == desired:
            flag = True




#Creating database
conn = sqlite3.connect('.\dbase.sqlite')
cur = conn.cursor()

cur.executescript('''
drop table if exists Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

create table 'Artist' (
    id integer not null primary key autoincrement  unique ,
    name text unique);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);


CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);

''')


#inserting items to database
for track in playlist:
    artist = finder(track, 'Artist')
    track_name = finder(track, 'Name')
    album = finder(track, 'Album')
    genre = finder(track, 'Genre')
    count = finder(track, 'Play Count')
    rating = finder(track, 'Rating')
    length = finder(track, 'Total Time')
    
    if artist == None or track_name == None or album == None or genre == None :
        continue
        
    cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES (?)''', (artist,))
    cur.execute('''SELECT id FROM Artist WHERE name =?''' , (artist,))
    
    artist_id = cur.fetchone()[0]
                               
    cur.execute(''' INSERT OR IGNORE INTO Album (title, artist_id) VALUES (? , ?)''' , (album , artist_id))
    cur.execute(''' SELECT id FROM Album WHERE title = ?''' ,(album,))
    
    album_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES (?)''', (genre,))
    cur.execute('''SELECT id FROM Genre WHERE name = ?''', (genre,))
    genre_id = cur.fetchone()[0]
    
    
    cur.execute(''' INSERT OR IGNORE INTO Track ( title, album_id, genre_id,  len , rating, count) VALUES (? , ? , ?, ?, ?, ?)''' , (track_name, album_id, genre_id , length, rating,count))
      
                               
    cur.execute('''INSERT OR IGNORE INTO Track (title) VALUES (?)''', (track_name,))





#Query serach in database
cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 10
	''')
    
x = cur.fetchall()

for item in x:
    print(item[0],'/', item[1],'/', item[2],'/', item[3])
    print('--------------------------------------------')



    
conn.commit()
