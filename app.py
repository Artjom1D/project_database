import tkinter as tk
from tkinter import ttk
from logic import *

#Lodziņu pamatfunkcijas

def addzooFromvlog():
    name_z = name_z_input.get()
    open = open_input.get()
    add_zoo(name_z, open)
    name_z_input.delete(0, tk.END)
    open_input.delete(0, tk.END)

def addlocationFromvlog():
    pet_id_g = pet_id_g_input.get()
    zoo_id_g = zoo_id_g_input.get()
    ticket_id_g = ticket_id_g_input.get()
    add_location(pet_id_g, zoo_id_g, ticket_id_g)
    pet_id_g_input.delete(0, tk.END)
    zoo_id_g_input.delete(0, tk.END)
    ticket_id_g_input.delete(0, tk.END)

def addpetgroupFromvlog():
    pet_id = pet_id_input.get()
    amount_of_species = amount_of_species_g_input.get()
    add_pet_group(pet_id, amount_of_species)
    pet_id_input.delete(0, tk.END)
    amount_of_species_g_input.delete(0, tk.END)

def addpetFromvlog():
    name_p = name_p_input.get()
    color = color_input.get()
    feed_id = feed_id_input.get()
    add_pet(name_p, color, feed_id)
    name_p_input.delete(0, tk.END)
    color_input.delete(0, tk.END)
    feed_id_input.delete(0, tk.END)

def addfoodFromvlog():
    pr_name = pr_name_input.get()
    price = price_input.get()
    available_amount = available_amount_input.get()
    next_order = next_order_input.get()
    add_food(pr_name, price, available_amount, next_order)
    pr_name_input.delete(0, tk.END)
    price_input.delete(0, tk.END)
    available_amount_input.delete(0, tk.END)
    next_order_input.delete(0, tk.END)

def addveterinaryrecordsFromvlog():
    pet_id_rec = pet_id_rec_input.get()
    diagnosis = diagnosis_input.get()
    doctor_suggestion = doctor_suggestion_input.get()
    last_visit = last_visit_input.get()
    add_veterinary_records(pet_id_rec, diagnosis, doctor_suggestion, last_visit)
    pet_id_rec_input.delete(0, tk.END)
    diagnosis_input.delete(0, tk.END)
    doctor_suggestion_input.delete(0, tk.END)
    last_visit_input.delete(0, tk.END)

def addticketsFromvlog():
    name_t = name_t_input.get()
    price_t = price_t_input.get()
    add_tickets(name_t, price_t)
    name_t_input.delete(0, tk.END)
    price_t_input.delete(0, tk.END)

def addeventFromvlog():
    name_e = name_e_input.get()
    start_date_e = start_date_e_input.get()
    end_date_e = end_date_e_input.get()
    zoo_place_id = zoo_place_id_input.get()
    ticket_id_e = ticket_id_e_input.get()
    add_event(name_e, start_date_e, end_date_e, zoo_place_id, ticket_id_e)
    name_e_input.delete(0, tk.END)
    start_date_e_input.delete(0, tk.END)
    end_date_e_input.delete(0, tk.END)
    zoo_place_id_input.delete(0, tk.END)
    ticket_id_e_input.delete(0, tk.END)

def addemployeeFromvlog():
    zoo_id_emp = zoo_id_emp_input.get()
    name_emp = name_emp_input.get()
    surname_emp = surname_emp_input.get()
    has_vacation = has_vacation_input.get()
    vacation_id = vacation_id_input.get()
    add_employee(zoo_id_emp, name_emp, surname_emp, has_vacation, vacation_id)
    zoo_id_emp_input.delete(0, tk.END)
    name_emp_input.delete(0, tk.END)
    surname_emp_input.delete(0, tk.END)
    has_vacation_input.delete(0, tk.END)
    vacation_id_input.delete(0, tk.END)

def addvacationFromvlog():
    emp_id = emp_id_input.get()
    start_date_v = start_date_v_input.get()
    end_date_v = end_date_v_input.get()
    add_vacation(emp_id, start_date_v, end_date_v)
    emp_id_input.delete(0, tk.END)
    start_date_v_input.delete(0, tk.END)
    end_date_v_input.delete(0, tk.END)



vlog = tk.Tk()
vlog.title("Zoo katalogs")
vlog.geometry("1920x1080")

tabs = ttk.Notebook(vlog)
tabs.pack(fill="both", expand=True)

zoo_tab = ttk.Frame(tabs)
location_tab = ttk.Frame(tabs)
petgroup_tab = ttk.Frame(tabs)
pet_tab = ttk.Frame(tabs)
food_tab = ttk.Frame(tabs)
veterinary_tab = ttk.Frame(tabs)
tickets_tab = ttk.Frame(tabs)
event_tab = ttk.Frame(tabs)
employee_tab = ttk.Frame(tabs)
vacation_tab = ttk.Frame(tabs)

tabs.add(zoo_tab, text="Zoo")
tabs.add(location_tab, text="Location")
tabs.add(petgroup_tab, text="Pet Group")
tabs.add(pet_tab, text="Pet")
tabs.add(food_tab, text="Food")
tabs.add(veterinary_tab, text="Veterinary")
tabs.add(tickets_tab, text="Tickets")
tabs.add(event_tab, text="Event")
tabs.add(employee_tab, text="Employee")
tabs.add(vacation_tab, text="Vacation")

label = tk.Label(zoo_tab, text="ZOO", font=("Arial", 24))
label.pack(pady=10)

header = tk.Label(zoo_tab, text="Zoo base", font=("Arial", 30, "bold"))
header.pack(pady=10)

#ZOO pievienot
zoo_block = tk.LabelFrame(
    zoo_tab,
    text="Zoo Information",
    font=("Arial", 18, "bold"),
    padx=10,
    pady=10
)
zoo_block.pack(padx=10, pady=10, fill="x")
tk.Label(zoo_block, text="Zoo Name").pack()
name_z_input = tk.Entry(zoo_block, width=40)
name_z_input.pack(pady=5)

result = tk.Label(zoo_block, text="")
result.pack(pady=5)

tk.Label(zoo_block, text="Open/Closed").pack()
open_input = tk.Entry(zoo_block, width=40)
open_input.pack(pady=5)

result = tk.Label(zoo_block, text="")
result.pack(pady=5)

product_button = tk.Button(zoo_block, text="Pievienot", command=addzooFromvlog)
product_button.pack(pady=10)
header.pack(pady = 20)
#Location pievienot
location_block = tk.LabelFrame(
    location_tab,
    text="Location Information",
    font=("Arial", 18, "bold"),
    padx=10,
    pady=10
)

location_block.pack(padx=10, pady=10, fill="x")
tk.Label(location_block, text="Pet ID").pack()
pet_id_g_input = tk.Entry(location_block, width=40)
pet_id_g_input.pack(pady=5)

result = tk.Label(location_block, text="")
result.pack(pady=5)

tk.Label(location_block, text="Zoo ID").pack()
zoo_id_g_input = tk.Entry(location_block, width=40)
zoo_id_g_input.pack(pady=5)

result = tk.Label(location_block, text="")
result.pack(pady=5)

tk.Label(location_block, text="Ticket ID").pack()
ticket_id_g_input = tk.Entry(location_block, width=40)
ticket_id_g_input.pack(pady=5)
result = tk.Label(location_block, text="")
result.pack(pady=5)

result = tk.Label(location_block, text="")
result.pack(pady=5)

product_button = tk.Button(location_block, text="Pievienot", command=addlocationFromvlog)
product_button.pack(pady=10)
header.pack(pady = 20)
#Pet group pievienot
petgroup_block = tk.LabelFrame(
    petgroup_tab,
    text="Pet Group Information",
    font=("Arial", 18, "bold"),
    padx=10,
    pady=10
)
petgroup_block.pack(padx=10, pady=10, fill="x")
tk.Label(petgroup_block, text="Pet Group ID").pack()
pet_id_input = tk.Entry(petgroup_block, width=40)
pet_id_input.pack(pady=5)

result = tk.Label(petgroup_block, text="")
result.pack(pady=5)

tk.Label(petgroup_block, text="Amount of species").pack()
amount_of_species_g_input = tk.Entry(petgroup_block, width=40)
amount_of_species_g_input.pack(pady=5)

result = tk.Label(petgroup_block, text="")
result.pack(pady=5)

product_button = tk.Button(petgroup_block, text="Pievienot", command=addpetgroupFromvlog)
product_button.pack(pady=10)
header.pack(pady = 20)
#Pet pievienot
pet_block = tk.LabelFrame(
    pet_tab,
    text="Pet Information",
    font=("Arial", 18, "bold"),
    padx=10,
    pady=10
)
pet_block.pack(padx=10, pady=10, fill="x")

tk.Label(pet_block, text="Pet Name").pack()
name_p_input = tk.Entry(pet_block, width=40)
name_p_input.pack(pady=5)

result = tk.Label(pet_block, text="")
result.pack(pady=5)

tk.Label(pet_block, text="Pet Color").pack()
color_input = tk.Entry(pet_block, width=40)
color_input.pack(pady=5)

result = tk.Label(pet_block, text="")
result.pack(pady=5)

tk.Label(pet_block, text="Species").pack()
feed_id_input = tk.Entry(pet_block, width=40)
feed_id_input.pack(pady=5)

result = tk.Label(pet_block, text="")
result.pack(pady=5)

product_button = tk.Button(pet_block, text="Pievienot", command=addpetFromvlog)
product_button.pack(pady=10)
header.pack(pady = 20)
#Food pievienot
food_block = tk.LabelFrame(
    food_tab,
    text="Food Information",
    font=("Arial", 18, "bold"),
    padx=10,
    pady=10
)
food_block.pack(padx=10, pady=10, fill="x")

tk.Label(food_block, text="Product Name").pack()
pr_name_input = tk.Entry(food_block, width=40)
pr_name_input.pack(pady=5)

result = tk.Label(food_block, text="")
result.pack(pady=5)

tk.Label(food_block, text="Price").pack()
price_input = tk.Entry(food_block, width=40)
price_input.pack(pady=5)

result = tk.Label(food_block, text="")
result.pack(pady=5)

tk.Label(food_block, text="Available Amount").pack()
available_amount_input= tk.Entry(food_block, width=40)
available_amount_input.pack(pady=5)

result = tk.Label(food_block, text="")
result.pack(pady=5)

tk.Label(food_block, text="Next Order").pack()
next_order_input= tk.Entry(food_block, width=40)
next_order_input.pack(pady=5)

result = tk.Label(food_block, text="")
result.pack(pady=5)

product_button = tk.Button(food_block, text="Pievienot", command=addfoodFromvlog)
product_button.pack(pady=10)
header.pack(pady = 20)
#Veterinary pievienot

veterinary_block = tk.LabelFrame(
    veterinary_tab,
    text="Veterinary Information",
    font=("Arial", 18, "bold"),
    padx=10,
    pady=10
)
veterinary_block.pack(padx=10, pady=10, fill="x")

tk.Label(veterinary_block, text="Pet ID").pack()
pet_id_rec_input = tk.Entry(veterinary_block, width=40)
pet_id_rec_input.pack(pady=5)

result = tk.Label(veterinary_block, text="")
result.pack(pady=5)

tk.Label(veterinary_block, text="Diagnosis").pack()
diagnosis_input = tk.Entry(veterinary_block, width=40)
diagnosis_input.pack(pady=5)

result = tk.Label(veterinary_block, text="")
result.pack(pady=5)

tk.Label(veterinary_block, text="Doctor Suggestion").pack()
doctor_suggestion_input = tk.Entry(veterinary_block, width=40)
doctor_suggestion_input.pack(pady=5)

result = tk.Label(veterinary_block, text="")
result.pack(pady=5)

tk.Label(veterinary_block, text="Last Visit").pack()
last_visit_input = tk.Entry(veterinary_block, width=40)
last_visit_input.pack(pady=5)

result = tk.Label(veterinary_block, text="")
result.pack(pady=5)

product_button = tk.Button(veterinary_block, text="Pievienot", command=addveterinaryrecordsFromvlog)
product_button.pack(pady=10)
header.pack(pady = 20)
#Tickets pievienot

ticket_block = tk.LabelFrame(
    tickets_tab,
    text="Ticket Information",
    font=("Arial", 18, "bold"),
    padx=10,
    pady=10
)
ticket_block.pack(padx=10, pady=10, fill="x")

tk.Label(ticket_block, text="Ticket Name").pack()
name_t_input = tk.Entry(ticket_block, width=40)
name_t_input.pack(pady=5)

result = tk.Label(ticket_block, text="")
result.pack(pady=5)

tk.Label(ticket_block, text="Price").pack()
price_t_input= tk.Entry(ticket_block, width=40)
price_t_input.pack(pady=5)

result = tk.Label(ticket_block, text="")
result.pack(pady=5)

product_button = tk.Button(ticket_block, text="Pievienot", command=addticketsFromvlog)
product_button.pack(pady=10)
header.pack(pady = 20)
#Event pievienot

event_block = tk.LabelFrame(
    event_tab,
    text="Event Information",
    font=("Arial", 18, "bold"),
    padx=10,
    pady=10
)
event_block.pack(padx=10, pady=10, fill="x")

tk.Label(event_block, text="Event Name").pack()
name_e_input = tk.Entry(event_block, width=40)
name_e_input.pack(pady=5)

result = tk.Label(event_block, text="")
result.pack(pady=5)

tk.Label(event_block, text="Start Date").pack()
start_date_e_input = tk.Entry(event_block, width=40)
start_date_e_input.pack(pady=5)

result = tk.Label(event_block, text="")
result.pack(pady=5)

tk.Label(event_block, text="End Date").pack()
end_date_e_input = tk.Entry(event_block, width=40)
end_date_e_input.pack(pady=5)

result = tk.Label(event_block, text="")
result.pack(pady=5)

tk.Label(event_block, text="Zoo place ID").pack()
zoo_place_id_input = tk.Entry(event_block, width=40)
zoo_place_id_input.pack(pady=5)

result = tk.Label(event_block, text="")
result.pack(pady=5)

tk.Label(event_block, text="Ticket ID").pack()
ticket_id_e_input = tk.Entry(event_block, width=40)
ticket_id_e_input.pack(pady=5)

result = tk.Label(event_block, text="")
result.pack(pady=5)

product_button = tk.Button(event_block, text="Pievienot", command=addeventFromvlog)
product_button.pack(pady=10)
header.pack(pady = 20)
#Employee pievienot
employee_block = tk.LabelFrame(
    employee_tab,
    text="Employee Information",
    font=("Arial", 18, "bold"),
    padx=10,
    pady=10
)
employee_block.pack(padx=10, pady=10, fill="x")

tk.Label(employee_block, text="Zoo ID").pack()
zoo_id_emp_input= tk.Entry(employee_block, width=40)
zoo_id_emp_input.pack(pady=5)

result = tk.Label(employee_block, text="")
result.pack(pady=5)

tk.Label(employee_block, text="Name").pack()
name_emp_input = tk.Entry(employee_block, width=40)
name_emp_input.pack(pady=5)

result = tk.Label(employee_block, text="")
result.pack(pady=5)

tk.Label(employee_block, text="Surname").pack()
surname_emp_input = tk.Entry(employee_block, width=40)
surname_emp_input.pack(pady=5)

result = tk.Label(employee_block, text="")
result.pack(pady=5)

tk.Label(employee_block, text="Has Vacation(Yes/No)").pack()
has_vacation_input = tk.Entry(employee_block, width=40)
has_vacation_input.pack(pady=5)

result = tk.Label(employee_block, text="")
result.pack(pady=5)

tk.Label(employee_block, text="Vacation ID").pack()
vacation_id_input = tk.Entry(employee_block, width=40)
vacation_id_input.pack(pady=5)

result = tk.Label(employee_block, text="")
result.pack(pady=5)

product_button = tk.Button(employee_block, text="Pievienot", command=addemployeeFromvlog)
product_button.pack(pady=10)
header.pack(pady = 20)
#Vacation pievienot

vacation_block = tk.LabelFrame(
    vacation_tab,
    text="Vacation Information",
    font=("Arial", 18, "bold"),
    padx=10,
    pady=10
)
vacation_block.pack(padx=10, pady=10, fill="x")
tk.Label(vacation_block, text="Employee ID").pack()
emp_id_input = tk.Entry(vacation_block, width=40)
emp_id_input.pack(pady=5)

result = tk.Label(vacation_block, text="")
result.pack(pady=5)

tk.Label(vacation_block, text="Start Date").pack()
start_date_v_input = tk.Entry(vacation_block, width=40)
start_date_v_input.pack(pady=5)

result = tk.Label(vacation_block, text="")
result.pack(pady=5)

tk.Label(vacation_block, text="End Date").pack()
end_date_v_input = tk.Entry(vacation_block, width=40)
end_date_v_input.pack(pady=5)

result = tk.Label(vacation_block, text="")
result.pack(pady=5)

product_button = tk.Button(vacation_block, text="Pievienot", command=addvacationFromvlog)
product_button.pack(pady=10)
header.pack(pady = 20)

#Vietne
vlog.mainloop()