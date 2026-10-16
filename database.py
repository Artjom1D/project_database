import sqlite3
    
con = sqlite3.connect("data.db")

cur = con.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS zoo (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            open BOOLEAN NOT NULL
)''')


#------------------------------
#Viss, kas saistīts ar dzīvniekiem
cur.execute('''CREATE TABLE IF NOT EXISTS location (
            id INTEGER PRIMARY KEY,
            pet_id INTEGER NOT NULL,
            zoo_id INTEGER NOT NULL,
            ticket_id INTEGER NOT NULL,
            FOREIGN KEY (pet_id) REFERENCES pet_group (id),
            FOREIGN KEY (zoo_id) REFERENCES zoo (id),
            FOREIGN KEY (ticket_id) REFERENCES tickets (id)
)''')

cur.execute('''CREATE TABLE IF NOT EXISTS pet_group(

            id INTEGER PRIMARY KEY,
            pet_id INTEGER NOT NULL,
            amount_of_species INTEGER,
            FOREIGN KEY (pet_id) REFERENCES pet (id)
)''')

cur.execute('''CREATE TABLE IF NOT EXISTS pet (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            color TEXT NOT NULL,
            feed_id INTEGER NOT NULL,
            FOREIGN KEY (feed_id) REFERENCES food (id)
)''')

cur.execute('''CREATE TABLE IF NOT EXISTS food (
            id INTEGER PRIMARY KEY,
            pr_name TEXT NOT NULL,
            price REAL NOT NULL,
            available_amount REAL NOT NULL,
            next_order DATE
)''')

cur.execute('''CREATE TABLE IF NOT EXISTS veterinary_records (
            id INTEGER PRIMARY KEY,
            pet_id INTEGER NOT NULL,
            diagnosis TEXT NOT NULL,
            doctor_suggestion TEXT NOT NULL,
            last_visit DATE NOT NULL,
            FOREIGN KEY (pet_id) REFERENCES pet (id)
)''')

#------------------------------

cur.execute('''CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL
)''')

cur.execute('''CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            start_date DATE NOT NULL,
            end_date DATE NOT NULL,
            zoo_place_id INTEGER NOT NULL,
            ticket_id INTEGER NOT NULL,
            FOREIGN KEY (zoo_place_id) REFERENCES zoo (id),
            FOREIGN KEY (ticket_id) REFERENCES tickets (id)
)''')

cur.execute('''CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            zoo_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            has_vacation BOOLEAN NOT NULL,
            vacation_id INTEGER,
            FOREIGN KEY (zoo_id) REFERENCES zoo (id),
            FOREIGN KEY (vacation_id) REFERENCES vacation (id)
)''')
cur.execute('''CREATE TABLE IF NOT EXISTS vacation (
            id INTEGER PRIMARY KEY,
            start_date DATE NOT NULL,
            end_date DATE NOT NULL
)''')