# Accessing Database using Python.

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()
cur.execute('Drop Table if EXISTS Counts')
cur.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()

    if row is None:
        cur.execute('''INSERT INTO Counts (email, count) VALUES (?, 1)''', (email,))

    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))

    conn.commit()






import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
list_1 =[]
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    dom = email.find('@')
    org = email[dom+1:len(email)]

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
conn.commit()
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()


 # This application will read an iTunes export file in XML and produce a properly normalized database with this structure:

import xml.etree.ElementTree as ET
import sqlite3
#connects to database, creates a sqlite file
conn = sqlite3.connect('trackdb1.sqlite')
cur  = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
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
    len INTEGER,
    rating INTEGER,
    count INTEGER
);


CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY
    AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
)

''')


fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

#create element tree and find the branch
stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print ('Dict count:', len(all))
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre_name = lookup(entry, 'Genre')

    if name is None or artist is None or album is None or genre_name is None:
        continue

    print (name, artist,genre_name, album, count, rating, length)

    #insert data into table
    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE
    INTO Genre(name)
        VALUES (?)''', (genre_name, ))
    cur.execute('SELECT ID FROM Genre WHERE name = ?', (genre_name, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ?, ? )''',
        ( name, album_id, genre_id, length, rating, count ) )
conn.commit()

# Connecting many courses to many students(many to many relationship).
# student my be connected to many courses or courses may be chosen by many students

import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User(
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Course(
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title    TEXT UNIQUE
);

CREATE TABLE Member(
    user_id      INTEGER,
    course_id    INTEGER,
    role         INTEGER,
    PRIMARY KEY (user_id, course_id)
);

''')

fname = input('Enter file name: ')
if len(fname)< 1:
    fname = 'roster_data.json'

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry (0);
    title = entry[1];

    print((name, title))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES (?)''', (name, ))
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course(title)
        VALUES (?)''',( title, ))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title, ))
    course_id = cur.fecthone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id) VALUES (?, ?)''',
        (user_id, course_id))

    conn.commit()


    import json
import sqlite3

#PART 1: Creating the database
dbname = "roster.sqlite"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.executescript('''
	DROP TABLE IF EXISTS User;
	DROP TABLE IF EXISTS Course;
	DROP TABLE IF EXISTS Member;
	CREATE TABLE User (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name TEXT UNIQUE
	);
	CREATE TABLE Course (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		title TEXT UNIQUE
	);
	CREATE TABLE Member (
		user_id INTEGER,
		course_id INTEGER,
		role INTEGER,
		PRIMARY KEY(user_id, course_id)
	)
''')
#Note: if we don't add UNIQUE after "User.name" and "Course.title",
#the IGNORE statement won't work and therefore we'll have duplicates


#PART 2: DESERIALIZING THE data
#The JSON data we're going to process is stored in an array form, with each
#item being also an array of three elements: one corresponding to the username
#one corresponding to the course name, and one indicating if the user is instructor
#None of them has any field title.

filename = "roster_data.json"
jsondata = open(filename)
data = json.load(jsondata)

#PART 3: INSERTING DATA
for entry in data:
	user = entry[0]
	course = entry[1]
	instructor = entry[2]

	#Inserting user
	user_statement = """INSERT OR IGNORE INTO User(name) VALUES( ? )"""
	SQLparams = (user, )
	cur.execute(user_statement, SQLparams)

	#Inserting course
	course_statement = """INSERT OR IGNORE INTO Course(title) VALUES( ? )"""
	SQLparams = (course, )
	cur.execute(course_statement, SQLparams)

	#Getting user and course id
	courseID_statement = """SELECT id FROM Course WHERE title = ?"""
	SQLparams = (course, )
	cur.execute(courseID_statement, SQLparams)
	courseID = cur.fetchone()[0]

	userID_statement = """SELECT id FROM User WHERE name = ?"""
	SQLparams = (user, )
	cur.execute(userID_statement, SQLparams)
	userID = cur.fetchone()[0]

	#Inserting the entry
	member_statement = """INSERT INTO Member(user_id, course_id, role)
		VALUES(?, ?, ?)"""
	SQLparams = (userID, courseID, instructor)
	cur.execute(member_statement, SQLparams)

#Saving the changes
conn.commit()

#PART 4: Testing and obtaining the results
test_statement = """
SELECT hex(User.name || Course.title || Member.role ) AS X FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X
"""
cur.execute(test_statement)
result = cur.fetchone()
print("RESULT: " + str(result))

#Closing the connection
cur.close()
conn.close()



# This application will read roster data in JSON format, parse the file, and then produce an SQLite database that contains a User, Course, and Member table and populate the tables from the data file


import json
import sqlite3

#PART 1: Creating the database
dbname = "roster3.sqlite"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.executescript('''
	DROP TABLE IF EXISTS User;
	DROP TABLE IF EXISTS Course;
	DROP TABLE IF EXISTS Member;
	CREATE TABLE User (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name TEXT UNIQUE
	);
	CREATE TABLE Course (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		title TEXT UNIQUE
	);
	CREATE TABLE Member (
		user_id INTEGER,
		course_id INTEGER,
		role INTEGER,
		PRIMARY KEY(user_id, course_id)
	)
''')
#Note: if we don't add UNIQUE after "User.name" and "Course.title",
#the IGNORE statement won't work and therefore we'll have duplicates


#PART 2: DESERIALIZING THE data
#The JSON data we're going to process is stored in an array form, with each
#item being also an array of three elements: one corresponding to the username
#one corresponding to the course name, and one indicating if the user is instructor
#None of them has any field title.

filename = "roster_data.json"
jsondata = open(filename)
data = json.load(jsondata)

#PART 3: INSERTING DATA
for entry in data:
	user = entry[0]
	course = entry[1]
	instructor = entry[2]

	#Inserting user
	user_statement = """INSERT OR IGNORE INTO User(name) VALUES( ? )"""
	SQLparams = (user, )
	cur.execute(user_statement, SQLparams)

	#Inserting course
	course_statement = """INSERT OR IGNORE INTO Course(title) VALUES( ? )"""
	SQLparams = (course, )
	cur.execute(course_statement, SQLparams)

	#Getting user and course id
	courseID_statement = """SELECT id FROM Course WHERE title = ?"""
	SQLparams = (course, )
	cur.execute(courseID_statement, SQLparams)
	courseID = cur.fetchone()[0]

	userID_statement = """SELECT id FROM User WHERE name = ?"""
	SQLparams = (user, )
	cur.execute(userID_statement, SQLparams)
	userID = cur.fetchone()[0]

	#Inserting the entry
	member_statement = """INSERT INTO Member(user_id, course_id, role)
		VALUES(?, ?, ?)"""
	SQLparams = (userID, courseID, instructor)
	cur.execute(member_statement, SQLparams)

#Saving the changes
conn.commit()

#PART 4: Testing and obtaining the results
test_statement = """
SELECT hex(User.name || Course.title || Member.role ) AS X FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X
"""
cur.execute(test_statement)
result = cur.fetchone()
print("RESULT: " + str(result))

#Closing the connection
cur.close()
conn.close()


# Extracting data from Google API KEY and display it .

import urlib.request, urlib.parse, urlib.error
import https
import sqlite3
import json
import Time
import ssl
import  sys

api_key = False
# If you have a google places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

if api_key is False:
    api_key = 42
    serviceur = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "http://maps.googleaps.com/maps/api/geocode/json?"

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Locations(address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.data")
count = 0
for line i fh:
    if count > 200 :
        print('Retrieve 200 locations, restart to retrieve more')
        break
    address = line.srtip()
    print('')
    cur.execute("SELECT geodata FROM Locations where address= ?",(memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]
        print("Found in database ", address)
        continue
    except:
        pass

    parms = dict()
    parms["address"] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceur + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'character', data[:20].repalce('\n', ' '))
    count = count +1

    try:
        js = json.loads(data)
    except:
        print(data) # We print in case unicode causes an errors
        continue

    if 'status' not in js or (js['status'] != 'OK' and js ['status'] != 'ZERO_ReSULTS'):
        print('===Failure To Retrieve ===')
        print(data)
        break

    cur.execute('''INSERT INTO Locations (address, geodata)
            VALUES (?, ? ) ''', (memoryview(address.encode()), memoryview(data.encode()) ) )
    conn.commit()
    if count % 10 == 0 :
        print ('Pausing for a bit')
        time.sleep(5)

    print("Run geodump.py to read the data from the database so you can visualize it on a map")


# geodump.py,visualization code

import sqlite3
import json
import codecs

conn = sqlite.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM locations ')
fhand = codecs,open('where.js', 'W', "utf-8")
fhand.write("myaData = [\n")
count = 0

for row in cur :
    data = str(row[1].decode())
    try: js = json.loads(str(data))
    except: continue

    if not('status' in js and js['status'] == 'OK') : continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0 : continue
    where = js['results'][0]['formatted_address']
    where = where.replace("'", "")
    try :
        print(where, lat, lng)

        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")
