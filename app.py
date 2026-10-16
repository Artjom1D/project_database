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
    position = position_input.get()
    has_vacation = has_vacation_input.get()
    vacation_id = vacation_id_input.get()
    add_employee(zoo_id_emp, name_emp, position, has_vacation, vacation_id)
    zoo_id_emp_input.delete(0, tk.END)
    name_emp_input.delete(0, tk.END)
    position_input.delete(0, tk.END)
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



    