import sqlite3
from turtle import position


def connect_to_db():
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    con.execute("PRAGMA foreign_keys = ON")
    return con, cur


#pievienot datubazē

def add_zoo(name, open):
    con, cur = connect_to_db()
    cur.execute('''INSERT INTO zoo (name, open) VALUES (?, ?)''', (name, open))
    con.commit()
    con.close()

def add_location(pet_id, zoo_id, ticket_id):
    con, cur = connect_to_db()
    cur.execute('''INSERT INTO location (pet_id, zoo_id, ticket_id) VALUES (?, ?, ?)''', (pet_id, zoo_id, ticket_id))
    con.commit()
    con.close()

def add_pet_group(pet_id, amount_of_species):
    con, cur = connect_to_db()
    cur.execute('''INSERT INTO pet_group (pet_id, amount_of_species) VALUES (?, ?)''', (pet_id, amount_of_species))
    con.commit()
    con.close()

def add_pet(name, color, feed_id):
    con, cur = connect_to_db()
    cur.execute('''INSERT INTO pet (name, color, feed_id) VALUES (?, ?, ?)''', (name, color, feed_id))
    con.commit()
    con.close()

def add_food(pr_name, price, available_amount, next_order):
    con, cur = connect_to_db()
    cur.execute('''INSERT INTO food (pr_name, price, available_amount, next_order) VALUES (?, ?, ?, ?)''', (pr_name, price, available_amount, next_order))
    con.commit()
    con.close()

def add_veterinary_records(pet_id, diagnosis, doctor_suggestion, last_visit):
    con, cur = connect_to_db()
    cur.execute('''INSERT INTO veterinary_records (pet_id, diagnosis, doctor_suggestion, last_visit) VALUES (?, ?, ?, ?)''', (pet_id, diagnosis, doctor_suggestion, last_visit))
    con.commit()
    con.close()

def add_tickets(name, price):
    con, cur = connect_to_db()
    cur.execute('''INSERT INTO tickets (name, price) VALUES (?, ?)''', (name, price))
    con.commit()
    con.close()

def add_event(name, start_date, end_date, zoo_place_id, ticket_id):
    con, cur = connect_to_db()
    cur.execute('''INSERT INTO event (name, start_date, end_date, zoo_place_id, ticket_id) VALUES (?, ?, ?, ?, ?)''', (name, start_date, end_date, zoo_place_id, ticket_id))
    con.commit()
    con.close()

def add_employee(zoo_id, name, surname, has_vacation, vacation_id):
    con, cur = connect_to_db()
    cur.execute('''INSERT INTO employee (zoo_id, name, surname, has_vacation, vacation_id) VALUES (?, ?, ?, ?, ?)''', (zoo_id, name, surname, has_vacation, vacation_id))
    con.commit()
    con.close()

def add_vacation(employee_id, start_date, end_date):
    con, cur = connect_to_db()
    cur.execute('''INSERT INTO vacation (employee_id, start_date, end_date) VALUES (?, ?, ?)''', (employee_id, start_date, end_date))
    con.commit()
    con.close()
