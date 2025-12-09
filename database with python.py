# class PartyAnimal:
#     def __init__(self):
#         self.x = 0
#         print("I'm constructed")

#     def party(self):
#         self.x = self.x + 1
#         print('x changed to', self.x)

#     def __del__(self):
#         print("I'm destructed when x changed to", self.x)


# an = PartyAnimal()
# print(type(an))
# an.party()
# an.party()
# an.party()
# an = 20
# print(type(an))
# print('Now an is', an)

#############################################################
#############################################################

# class PartyAnimal:
#     def __init__(self, z):
#         self.x = 0
#         self.name = z
#         print(self.name, 'constructed!')

#     def party(self):
#         self.x = self.x + 1
#         print(self.name,'party count', self.x)

# a = PartyAnimal('Sally')
# a.party()

# b = PartyAnimal('Jimmy')
# b.party()

# a.party()
# a.party()
# a.party()
# a.party()
# a.party()

# b.party()

#############################################################
#############################################################


# import sqlite3

# conn = sqlite3.connect('emaildb.sqlite')
# cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Counts')

# cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# fname = input('Enter file name: ')
# if (len(fname) < 1): fname = 'mbox-short.txt'
# fh = open(fname)
# for line in fh:
#     if not line.startswith('From: '): continue
#     pieces = line.rstrip().split('@')
#     org = pieces[1]
#     cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    
# conn.commit()
# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

# for row in cur.execute(sqlstr):
#     print(str(row[0]),(row[1]))

# cur.close()

#############################################################
#############################################################


# import sqlite3

# conn = sqlite3.connect('trackdb.sqlite')
# cur = conn.cursor()

# # Make some fresh tables using executescript()
# cur.executescript('''
# DROP TABLE IF EXISTS Artist;
# DROP TABLE IF EXISTS Album;
# DROP TABLE IF EXISTS Track;
# DROP TABLE IF EXISTS Genre;

# CREATE TABLE Artist (
#     id  INTEGER PRIMARY KEY,
#     name    TEXT UNIQUE
# );

# CREATE TABLE Album (
#     id  INTEGER PRIMARY KEY,
#     artist_id  INTEGER,
#     title   TEXT UNIQUE
# );
                  
# CREATE TABLE Genre (
#     id  INTEGER PRIMARY KEY,
#     name   TEXT UNIQUE
# );

# CREATE TABLE Track (
#     id  INTEGER PRIMARY KEY,
#     title TEXT  UNIQUE,
#     album_id  INTEGER,
#     genre_id INTEGER,
#     len INTEGER, rating INTEGER, count INTEGER
# );
# ''')

# handle = open('tracks.csv')

# # Another One Bites The Dust,Queen,Greatest Hits,55,100,217103
# #   0                          1      2           3  4   5

# for line in handle:
#     line = line.strip();
#     pieces = line.split(',')
#     if len(pieces) < 7 : continue

#     name = pieces[0]
#     artist = pieces[1]
#     album = pieces[2]
#     count = pieces[3]
#     rating = pieces[4]
#     length = pieces[5]
#     genre = pieces[6]

#     print(name, artist, album, count, rating, length, genre)

#     cur.execute('''INSERT OR IGNORE INTO Artist (name) 
#         VALUES ( ? )''', ( artist, ) )
#     cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
#     artist_id = cur.fetchone()[0]

#     cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
#         VALUES ( ?, ? )''', ( album, artist_id ) )
#     cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
#     album_id = cur.fetchone()[0]

#     cur.execute('''INSERT OR IGNORE INTO Genre (name) 
#         VALUES ( ? )''', ( genre, ) )
#     cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
#     genre_id = cur.fetchone()[0]

#     cur.execute('''INSERT OR REPLACE INTO Track
#         (title, album_id, genre_id, len, rating, count) 
#         VALUES ( ?, ?, ?, ?, ?, ? )''', 
#         ( name, album_id, genre_id, length, rating, count ) )

#     conn.commit()


#############################################################
#############################################################

# import sqlite3

# conn = sqlite3.connect('trackdb.sqlite')
# cur = conn.cursor()
# for row in cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name 
#     FROM Track JOIN Genre JOIN Album JOIN Artist 
#     ON Track.genre_id = Genre.id and Track.album_id = Album.id 
#         AND Album.artist_id = Artist.id
#     ORDER BY Artist.name LIMIT 3'''):
#     print(row[0],row[1])

######################## Roaster #############################
##############################################################

# import json
# import sqlite3

# conn = sqlite3.connect('rosterdb.sqlite')
# cur = conn.cursor()

# # Do some setup
# cur.executescript('''
# DROP TABLE IF EXISTS User;
# DROP TABLE IF EXISTS Member;
# DROP TABLE IF EXISTS Course;

# CREATE TABLE User (
#     id     INTEGER PRIMARY KEY,
#     name   TEXT UNIQUE
# );

# CREATE TABLE Course (
#     id     INTEGER PRIMARY KEY,
#     title  TEXT UNIQUE
# );

# CREATE TABLE Member (
#     user_id     INTEGER,
#     course_id   INTEGER,
#     role        INTEGER,
#     PRIMARY KEY (user_id, course_id)
# )
# ''')

# fname = input('Enter file name: ')
# if len(fname) < 1:
#     fname = 'roster_data.json'

# #   [ "Charley", "si110", 1 ],
# #   [ "Mea", "si110", 0 ],

# str_data = open(fname).read()
# json_data = json.loads(str_data)

# for entry in json_data:

#     name = entry[0]
#     title = entry[1]
#     role = entry[2]

#     print((name, title, role))

#     cur.execute('''INSERT OR IGNORE INTO User (name)
#         VALUES ( ? )''', ( name, ) )
#     cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
#     user_id = cur.fetchone()[0]

#     cur.execute('''INSERT OR IGNORE INTO Course (title)
#         VALUES ( ? )''', ( title, ) )
#     cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
#     course_id = cur.fetchone()[0]

#     cur.execute('''INSERT OR REPLACE INTO Member
#         (user_id, course_id, role) VALUES ( ?, ?, ?)''',
#         ( user_id, course_id, role) )

#     conn.commit()


#############################################################
#############################################################