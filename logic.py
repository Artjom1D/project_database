import sqlite3

def connect_to_db():
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    con.execute("PRAGMA foreign_keys = ON")
    return con, cur


#pievienot datubazē

def add_zoo(name, open):
    con, cur = connect_to_db()

    if open.lower() == 'open':
        open = True
    elif open.lower() == 'closed':
        open = False
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
    if has_vacation.lower() == 'yes':
        has_vacation = True
    elif has_vacation.lower() == 'no':
        has_vacation = False
    cur.execute('''INSERT INTO employee (zoo_id, name, surname, has_vacation, vacation_id) VALUES (?, ?, ?, ?, ?)''', (zoo_id, name, surname, has_vacation, vacation_id))
    con.commit()
    con.close()

def add_vacation(employee_id, start_date, end_date):
    con, cur = connect_to_db()
    cur.execute('''INSERT INTO vacation (employee_id, start_date, end_date) VALUES (?, ?, ?)''', (employee_id, start_date, end_date))
    con.commit()
    con.close()


def search_zoo(value):
    con, cur = connect_to_db()
    cur.execute("""SELECT id, name, open FROM zoo
                WHERE name LIKE ?""", ('%' + value + '%',))
    results = cur.fetchall()
    con.close()
    return results

def search_location(value):
    con, cur = connect_to_db()
    cur.execute("""SELECT location.id, pet.name, zoo.name, location.ticket_id FROM location
                JOIN pet_group ON location.pet_id = pet_group.pet_id
                JOIN pet ON pet_group.pet_id = pet.id
                JOIN zoo ON location.zoo_id = zoo.id
                WHERE pet.name LIKE ? OR zoo.name LIKE ? OR location.ticket_id LIKE ?""", ('%' + value + '%', '%' + value + '%', '%' + value + '%'))
    results = cur.fetchall()
    con.close()
    return results

def search_petgroup(value):
    con, cur = connect_to_db()
    cur.execute("""SELECT pet_group.id, pet.name, pet_group.amount_of_species FROM pet_group
                JOIN pet ON pet_group.pet_id = pet.id
                WHERE pet.name LIKE ? OR pet_group.amount_of_species LIKE ?""", ('%' + value + '%', '%' + value + '%'))
    results = cur.fetchall()
    con.close()
    return results

def search_pet(value):
    con, cur = connect_to_db()
    cur.execute("""SELECT pet.id, pet.name, pet.color, food.pr_name FROM pet
                JOIN food ON pet.feed_id = food.id
                WHERE pet.name LIKE ? OR pet.color LIKE ?""", ('%' + value + '%', '%' + value + '%'))
    results = cur.fetchall()
    con.close()
    return results

def search_food(value):
    con, cur = connect_to_db()
    cur.execute("""SELECT id, pr_name, price, available_amount, next_order FROM food
                WHERE pr_name LIKE ?""", ('%' + value + '%',))
    results = cur.fetchall()
    con.close()
    return results

def search_veterinary(value):
    con, cur = connect_to_db()
    cur.execute("""SELECT veterinary_records.id, pet.name, diagnosis, doctor_suggestion, last_visit FROM veterinary_records
                JOIN pet ON veterinary_records.pet_id = pet.id
                WHERE pet.name LIKE ? OR diagnosis LIKE ? OR doctor_suggestion LIKE ? OR last_visit LIKE ?""", ('%' + value + '%', '%' + value + '%', '%' + value + '%', '%' + value + '%'))
    results = cur.fetchall()
    con.close()
    return results

def search_tickets(value):
    con, cur = connect_to_db()
    cur.execute("""SELECT id, name, price FROM tickets
                WHERE name LIKE ?""", ('%' + value + '%',))
    results = cur.fetchall()
    con.close()
    return results

def search_events(value):
    con, cur = connect_to_db()
    cur.execute("""SELECT events.id, events.name, events.start_date, zoo.name, tickets.name FROM events
                JOIN zoo ON events.zoo_place_id = zoo.id
                JOIN tickets ON events.ticket_id = tickets.id
                WHERE events.name LIKE ?""", ('%' + value + '%',))
    results = cur.fetchall()
    con.close()
    return results

def search_employee(value):
    con, cur = connect_to_db()
    cur.execute("""SELECT employees.id, employees.name, employees.surname, zoo.name FROM employees
                JOIN zoo ON employees.zoo_id = zoo.id
                WHERE employees.name LIKE ? OR employees.surname LIKE ?""", ('%' + value + '%', '%' + value + '%'))
    results = cur.fetchall()
    con.close()
    return results

def search_vacation(value):
    con, cur = connect_to_db()
    cur.execute("""SELECT id, start_date, end_date FROM vacation
                WHERE start_date LIKE ? OR end_date LIKE ?""", ('%' + value + '%', '%' + value + '%'))
    results = cur.fetchall()
    con.close()
    return results


#mainiit un dzeest ierakstus

def _resolve(cur, sql, value):
    row = cur.execute(sql, (value,)).fetchone()
    return row[0] if row else value

def update_zoo(record_id, name, open):
    con, cur = connect_to_db()
    if open.lower() == 'open':
        open = True
    elif open.lower() == 'closed':
        open = False
    cur.execute('''UPDATE zoo SET name = ?, open = ? WHERE id = ?''', (name, open, record_id))
    con.commit()
    con.close()

def delete_zoo(record_id):
    con, cur = connect_to_db()
    cur.execute('''DELETE FROM zoo WHERE id = ?''', (record_id,))
    con.commit()
    con.close()

def update_location(record_id, pet_name, zoo_name, ticket_name):
    con, cur = connect_to_db()
    pet_id = _resolve(cur, '''SELECT pet_group.id FROM pet_group JOIN pet ON pet_group.pet_id = pet.id WHERE pet.name = ?''', pet_name)
    zoo_id = _resolve(cur, '''SELECT id FROM zoo WHERE name = ?''', zoo_name)
    ticket_id = _resolve(cur, '''SELECT id FROM tickets WHERE name = ?''', ticket_name)
    cur.execute('''UPDATE location SET pet_id = ?, zoo_id = ?, ticket_id = ? WHERE id = ?''', (pet_id, zoo_id, ticket_id, record_id))
    con.commit()
    con.close()

def delete_location(record_id):
    con, cur = connect_to_db()
    cur.execute('''DELETE FROM location WHERE id = ?''', (record_id,))
    con.commit()
    con.close()

def update_pet_group(record_id, pet_name, amount_of_species):
    con, cur = connect_to_db()
    pet_id = _resolve(cur, '''SELECT id FROM pet WHERE name = ?''', pet_name)
    cur.execute('''UPDATE pet_group SET pet_id = ?, amount_of_species = ? WHERE id = ?''', (pet_id, amount_of_species, record_id))
    con.commit()
    con.close()

def delete_pet_group(record_id):
    con, cur = connect_to_db()
    cur.execute('''DELETE FROM pet_group WHERE id = ?''', (record_id,))
    con.commit()
    con.close()

def update_pet(record_id, name, color, food_name):
    con, cur = connect_to_db()
    feed_id = _resolve(cur, '''SELECT id FROM food WHERE pr_name = ?''', food_name)
    cur.execute('''UPDATE pet SET name = ?, color = ?, feed_id = ? WHERE id = ?''', (name, color, feed_id, record_id))
    con.commit()
    con.close()

def delete_pet(record_id):
    con, cur = connect_to_db()
    cur.execute('''DELETE FROM pet WHERE id = ?''', (record_id,))
    con.commit()
    con.close()

def update_food(record_id, pr_name, price, available_amount, next_order):
    con, cur = connect_to_db()
    cur.execute('''UPDATE food SET pr_name = ?, price = ?, available_amount = ?, next_order = ? WHERE id = ?''', (pr_name, price, available_amount, next_order, record_id))
    con.commit()
    con.close()

def delete_food(record_id):
    con, cur = connect_to_db()
    cur.execute('''DELETE FROM food WHERE id = ?''', (record_id,))
    con.commit()
    con.close()

def update_veterinary_records(record_id, pet_name, diagnosis, doctor_suggestion, last_visit):
    con, cur = connect_to_db()
    pet_id = _resolve(cur, '''SELECT id FROM pet WHERE name = ?''', pet_name)
    cur.execute('''UPDATE veterinary_records SET pet_id = ?, diagnosis = ?, doctor_suggestion = ?, last_visit = ? WHERE id = ?''', (pet_id, diagnosis, doctor_suggestion, last_visit, record_id))
    con.commit()
    con.close()

def delete_veterinary_records(record_id):
    con, cur = connect_to_db()
    cur.execute('''DELETE FROM veterinary_records WHERE id = ?''', (record_id,))
    con.commit()
    con.close()

def update_tickets(record_id, name, price):
    con, cur = connect_to_db()
    cur.execute('''UPDATE tickets SET name = ?, price = ? WHERE id = ?''', (name, price, record_id))
    con.commit()
    con.close()

def delete_tickets(record_id):
    con, cur = connect_to_db()
    cur.execute('''DELETE FROM tickets WHERE id = ?''', (record_id,))
    con.commit()
    con.close()

def update_events(record_id, name, start_date, end_date, zoo_name, ticket_name):
    con, cur = connect_to_db()
    zoo_id = _resolve(cur, '''SELECT id FROM zoo WHERE name = ?''', zoo_name)
    ticket_id = _resolve(cur, '''SELECT id FROM tickets WHERE name = ?''', ticket_name)
    cur.execute('''UPDATE events SET name = ?, start_date = ?, end_date = ?, zoo_place_id = ?, ticket_id = ? WHERE id = ?''', (name, start_date, end_date, zoo_id, ticket_id, record_id))
    con.commit()
    con.close()

def delete_events(record_id):
    con, cur = connect_to_db()
    cur.execute('''DELETE FROM events WHERE id = ?''', (record_id,))
    con.commit()
    con.close()

def update_employees(record_id, zoo_name, name, surname, has_vacation, vacation_id):
    con, cur = connect_to_db()
    zoo_id = _resolve(cur, '''SELECT id FROM zoo WHERE name = ?''', zoo_name)
    if has_vacation.lower() == 'yes':
        has_vacation = True
    elif has_vacation.lower() == 'no':
        has_vacation = False
    cur.execute('''UPDATE employees SET zoo_id = ?, name = ?, surname = ?, has_vacation = ?, vacation_id = ? WHERE id = ?''', (zoo_id, name, surname, has_vacation, vacation_id, record_id))
    con.commit()
    con.close()

def delete_employees(record_id):
    con, cur = connect_to_db()
    cur.execute('''DELETE FROM employees WHERE id = ?''', (record_id,))
    con.commit()
    con.close()

def update_vacation(record_id, start_date, end_date):
    con, cur = connect_to_db()
    cur.execute('''UPDATE vacation SET start_date = ?, end_date = ? WHERE id = ?''', (start_date, end_date, record_id))
    con.commit()
    con.close()

def delete_vacation(record_id):
    con, cur = connect_to_db()
    cur.execute('''DELETE FROM vacation WHERE id = ?''', (record_id,))
    con.commit()
    con.close()
