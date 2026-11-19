import tkinter as tk
from tkinter import ttk, messagebox
from logic import *

#Lodziņu pamatfunkcijas

# šeit glabājas katras tabulas atjaunināšanas funkcija
TABLE_REFRESH = {}

def addzooFromvlog():
    name_z = name_z_input.get()
    open = open_input.get()
    add_zoo(name_z, open)
    name_z_input.delete(0, tk.END)
    open_input.delete(0, tk.END)
    TABLE_REFRESH["zoo"]()

def addlocationFromvlog():
    pet_id_g = pet_id_g_input.get()
    zoo_id_g = zoo_id_g_input.get()
    ticket_id_g = ticket_id_g_input.get()
    add_location(pet_id_g, zoo_id_g, ticket_id_g)
    pet_id_g_input.delete(0, tk.END)
    zoo_id_g_input.delete(0, tk.END)
    ticket_id_g_input.delete(0, tk.END)
    TABLE_REFRESH["location"]()

def addpetgroupFromvlog():
    pet_id = pet_id_input.get()
    amount_of_species = amount_of_species_g_input.get()
    add_pet_group(pet_id, amount_of_species)
    pet_id_input.delete(0, tk.END)
    amount_of_species_g_input.delete(0, tk.END)
    TABLE_REFRESH["petgroup"]()

def addpetFromvlog():
    name_p = name_p_input.get()
    color = color_input.get()
    feed_id = feed_id_input.get()
    add_pet(name_p, color, feed_id)
    name_p_input.delete(0, tk.END)
    color_input.delete(0, tk.END)
    feed_id_input.delete(0, tk.END)
    TABLE_REFRESH["pet"]()

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
    TABLE_REFRESH["food"]()

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
    TABLE_REFRESH["veterinary"]()

def addticketsFromvlog():
    name_t = name_t_input.get()
    price_t = price_t_input.get()
    add_tickets(name_t, price_t)
    name_t_input.delete(0, tk.END)
    price_t_input.delete(0, tk.END)
    TABLE_REFRESH["tickets"]()

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
    TABLE_REFRESH["events"]()

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
    TABLE_REFRESH["employee"]()

def addvacationFromvlog():
    start_date_v = start_date_v_input.get()
    end_date_v = end_date_v_input.get()
    add_vacation(start_date_v, end_date_v)
    start_date_v_input.delete(0, tk.END)
    end_date_v_input.delete(0, tk.END)
    TABLE_REFRESH["vacation"]()

def make_search_table(tab, title, headers, search_func, update_func, delete_func, refresh_key):
    # Izveido meklēšanas lauku un tabulu.
    tk.Label(tab, text=title, font=("Arial", 12, "bold")).pack(pady=5)
    search_entry = tk.Entry(tab, width=40, font=("Arial", 11))
    search_entry.pack(pady=5)

    table_frame = tk.Frame(tab)
    table_frame.pack(pady=5, fill="both", expand=True)

    tree = ttk.Treeview(table_frame, columns=[f"c{i}" for i in range(len(headers))], show="headings", height=10)
    # Iestata pamīšus iekrāsotas rindas.
    tree.tag_configure("even", background="#ffffff")
    tree.tag_configure("odd", background="#f0f5ef")
    for i, h in enumerate(headers):
        tree.heading(f"c{i}", text=h)
        tree.column(f"c{i}", width=130, anchor="w")
    tree.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scrollbar.set)

    # Atjauno tabulas ierakstus pēc meklēšanas.
    def refresh(e=None):
        tree.delete(*tree.get_children())
        for index, row in enumerate(search_func(search_entry.get())):
            tree.insert("", "end", iid=str(row[0]), values=row, tags=("even" if index % 2 == 0 else "odd",))

    # Atgriež izvēlētā ieraksta ID.
    def selected_id():
        sel = tree.selection()
        return int(sel[0]) if sel else None

    # Ielādē izvēlēto ierakstu formā.
    def fill_form():
        record_id = selected_id()
        if record_id is None:
            messagebox.showwarning("Uzmanību", "Vispirms izvēlies rindu tabulā!")
            return
        values = tree.item(tree.selection()[0], "values")

        widgets = form_widgets["entries"]
        for widget, value in zip(widgets, values[1:]):
            widget.delete(0, tk.END)
            widget.insert(0, value)

    # Saglabā formas izmaiņas.
    def update_record():
        record_id = selected_id()
        if record_id is None:
            messagebox.showwarning("Uzmanību", "Vispirms izvēlies rindu tabulā!")
            return
        widgets = form_widgets["entries"]
        if not widgets:
            messagebox.showwarning("Uzmanību", "Forma šai tabulai nav piesaistīta!")
            return
        values = [w.get() for w in widgets]
        if any(v == "" for v in values):
            messagebox.showwarning("Uzmanību", "Nospied 'Ielādēt formā', izmaini datus un tad nospied 'Atjaunināt'!")
            return
        update_func(record_id, *values)
        for w in widgets:
            w.delete(0, tk.END)
        refresh()

    # Dzēš izvēlēto ierakstu pēc apstiprinājuma.
    def delete_record():
        record_id = selected_id()
        if record_id is None:
            messagebox.showwarning("Uzmanību", "Vispirms izvēlies rindu tabulā!")
            return
        if messagebox.askyesno("Apstiprinājums", f"Dzēst ierakstu ar ID {record_id}?"):
            delete_func(record_id)
            refresh()

    button_frame = tk.Frame(tab)
    button_frame.pack(pady=5)
    ttk.Button(button_frame, text="Dzēst", width=12, command=delete_record).pack(side="left", padx=5)
    ttk.Button(button_frame, text="Atjaunināt", width=12, command=update_record).pack(side="left", padx=5)
    ttk.Button(button_frame, text="Ielādēt formā", width=14, command=fill_form).pack(side="left", padx=5)

    form_widgets = {"entries": []}

    search_entry.bind("<KeyRelease>", refresh)
    refresh()

    TABLE_REFRESH[refresh_key] = refresh

    return tree, form_widgets


vlog = tk.Tk()
vlog.title("ZOO | Katalogs")
vlog.geometry("1440x900")
vlog.minsize(1100, 700)
vlog.configure(bg="#f3f6f0")

# Vienota krāsu tēma un stili lietotnes logam, formām, pogām un tabulām.
page_bg = "#f3f6f0"
surface_bg = "#ffffff"
text_color = "#26382e"
muted_color = "#66756b"
forest_green = "#285943"
leaf_green = "#3d7955"
line_color = "#d8e2d9"

vlog.option_add("*Font", ("Segoe UI", 10))
vlog.option_add("*Frame.Background", page_bg)
vlog.option_add("*Label.Background", page_bg)
vlog.option_add("*Label.Foreground", text_color)
vlog.option_add("*Entry.Background", surface_bg)
vlog.option_add("*Entry.Foreground", text_color)
vlog.option_add("*Entry.Relief", "flat")
vlog.option_add("*Entry.BorderWidth", 1)
vlog.option_add("*Entry.HighlightThickness", 1)
vlog.option_add("*Entry.HighlightBackground", line_color)
vlog.option_add("*Entry.HighlightColor", leaf_green)
vlog.option_add("*Button.Background", leaf_green)
vlog.option_add("*Button.Foreground", surface_bg)
vlog.option_add("*Button.ActiveBackground", forest_green)
vlog.option_add("*Button.ActiveForeground", surface_bg)
vlog.option_add("*Button.Relief", "flat")
vlog.option_add("*Button.BorderWidth", 0)
vlog.option_add("*Button.Padx", 12)
vlog.option_add("*Button.Pady", 7)

style = ttk.Style()
style.theme_use("clam")

# Pamatstils un cilņu izskats.
style.configure(".", background=page_bg, foreground=text_color, font=("Segoe UI", 10))
style.configure("TFrame", background=page_bg)
style.configure("TNotebook", background=page_bg, borderwidth=0, tabmargins=[10, 10, 10, 0])
style.configure("TNotebook.Tab", background="#e5ece5", foreground=muted_color, padding=[16, 11], font=("Segoe UI", 10, "bold"))
style.map("TNotebook.Tab",
    background=[("selected", forest_green), ("active", "#d6e4d8")],
    foreground=[("selected", surface_bg), ("active", text_color)]
)

# Kartīšu un tabulu izskats.
style.configure("TLabelframe", background=surface_bg, bordercolor=line_color, relief="solid", borderwidth=1)
style.configure("TLabelframe.Label", background=surface_bg, foreground=forest_green, font=("Segoe UI", 12, "bold"))

style.configure("Treeview",
    background=surface_bg,
    foreground=text_color,
    rowheight=32,
    fieldbackground=surface_bg,
    font=("Segoe UI", 10)
)
style.configure("Treeview.Heading",
    background=forest_green,
    foreground=surface_bg,
    padding=[9, 8],
    font=("Segoe UI", 10, "bold")
)
style.map("Treeview",
    background=[("selected", "#cfe3d3")],
    foreground=[("selected", text_color)]
)

# Pogu izskats.
style.configure("TButton",
    background=leaf_green,
    foreground=surface_bg,
    font=("Segoe UI", 10, "bold"),
    padding=[12, 8],
    relief="flat"
)
style.map("TButton",
    background=[("active", forest_green)],
    foreground=[("active", surface_bg)]
)

# Katrai cilnei izveido ritināmu satura apgabalu ar vertikālu ritjoslu.
tab_canvases = {}

def create_scrollable_tab(notebook, title):
    tab_container = ttk.Frame(notebook)
    canvas = tk.Canvas(tab_container, background=page_bg, highlightthickness=0, borderwidth=0)
    scrollbar = ttk.Scrollbar(tab_container, orient="vertical", command=canvas.yview)
    content = ttk.Frame(canvas)
    content_window = canvas.create_window((0, 0), window=content, anchor="nw")

    content.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind("<Configure>", lambda event: canvas.itemconfigure(content_window, width=event.width))
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    notebook.add(tab_container, text=title)
    tab_canvases[tab_container._w] = canvas
    return content

# Peles ritenītis ritina pašlaik atvērto cilni.
def scroll_current_tab(event):
    canvas = tab_canvases.get(tabs.select())
    if canvas is None:
        return

    if getattr(event, "num", None) == 4:
        direction = -1
    elif getattr(event, "num", None) == 5:
        direction = 1
    else:
        delta = getattr(event, "delta", 0)
        direction = -max(1, abs(delta) // 120) if delta > 0 else max(1, abs(delta) // 120)

    canvas.yview_scroll(direction, "units")
    return "break"

tabs = ttk.Notebook(vlog)
tabs.pack(fill="both", expand=True, padx=14, pady=(8, 14))

zoo_tab = create_scrollable_tab(tabs, "Zoo")
location_tab = create_scrollable_tab(tabs, "Location")
petgroup_tab = create_scrollable_tab(tabs, "Pet Group")
pet_tab = create_scrollable_tab(tabs, "Pet")
food_tab = create_scrollable_tab(tabs, "Food")
veterinary_tab = create_scrollable_tab(tabs, "Veterinary")
tickets_tab = create_scrollable_tab(tabs, "Tickets")
event_tab = create_scrollable_tab(tabs, "Event")
employee_tab = create_scrollable_tab(tabs, "Employee")
vacation_tab = create_scrollable_tab(tabs, "Vacation")

# Piesaista ritināšanu Windows un Linux peles ritenīša notikumiem.
vlog.bind_all("<MouseWheel>", scroll_current_tab)
vlog.bind_all("<Button-4>", scroll_current_tab)
vlog.bind_all("<Button-5>", scroll_current_tab)

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


zoo_tree, zoo_form = make_search_table(
    zoo_tab, "Meklēt Zoo:", ("ID", "Name", "Open"),
    search_zoo, update_zoo, delete_zoo, "zoo"
)
zoo_form["entries"] = [name_z_input, open_input]


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

loc_tree, loc_form = make_search_table(
    location_tab, "Meklēt lokācijas:", ("ID", "Pet Name", "Zoo Name", "Ticket Name"),
    search_location, update_location, delete_location, "location"
)
loc_form["entries"] = [pet_id_g_input, zoo_id_g_input, ticket_id_g_input]

#Pet group pievienot
petgroup_block = tk.LabelFrame(
    petgroup_tab,
    text="Pet Group Information",
    font=("Arial", 18, "bold"),
    padx=10,
    pady=10
)
petgroup_block.pack(padx=10, pady=10, fill="x")
tk.Label(petgroup_block, text="Pet ID").pack()
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

pg_tree, pg_form = make_search_table(
    petgroup_tab, "Meklēt dzīvnieku grupas:", ("ID", "Pet Name", "Amount"),
    search_petgroup, update_pet_group, delete_pet_group, "petgroup"
)
pg_form["entries"] = [pet_id_input, amount_of_species_g_input]

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

tk.Label(pet_block, text="Feed_ID").pack()
feed_id_input = tk.Entry(pet_block, width=40)
feed_id_input.pack(pady=5)

result = tk.Label(pet_block, text="")
result.pack(pady=5)

product_button = tk.Button(pet_block, text="Pievienot", command=addpetFromvlog)
product_button.pack(pady=10)
header.pack(pady = 20)

pet_tree, pet_form = make_search_table(
    pet_tab, "Meklēt dzīvniekus:", ("ID", "Name", "Color", "Feed"),
    search_pet, update_pet, delete_pet, "pet"
)
pet_form["entries"] = [name_p_input, color_input, feed_id_input]

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

food_tree, food_form = make_search_table(
    food_tab, "Meklēt pārtiku:", ("ID", "Product", "Price", "Stock", "Next Order"),
    search_food, update_food, delete_food, "food"
)
food_form["entries"] = [pr_name_input, price_input, available_amount_input, next_order_input]

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

vet_tree, vet_form = make_search_table(
    veterinary_tab, "Meklēt veterināros ierakstus:", ("ID", "Pet Name", "Diagnosis", "Doctor Suggestion", "Last Visit"),
    search_veterinary, update_veterinary_records, delete_veterinary_records, "veterinary"
)
vet_form["entries"] = [pet_id_rec_input, diagnosis_input, doctor_suggestion_input, last_visit_input]

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

ticket_tree, ticket_form = make_search_table(
    tickets_tab, "Meklēt biļetes:", ("ID", "Name", "Price"),
    search_tickets, update_tickets, delete_tickets, "tickets"
)
ticket_form["entries"] = [name_t_input, price_t_input]

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

event_tree, event_form = make_search_table(
    event_tab, "Meklēt pasākumus:", ("ID", "Name", "Start", "End", "Zoo", "Ticket"),
    search_events, update_events, delete_events, "events"
)
event_form["entries"] = [name_e_input, start_date_e_input, end_date_e_input, zoo_place_id_input, ticket_id_e_input]

#Employee pievienot
employee_block = tk.LabelFrame(
    employee_tab,
    text="Employee Information",
    font=("Arial", 18, "bold"),
    padx=10,
    pady=10
)
employee_block.pack(padx=10, pady=10, fill="x")

tk.Label(employee_block, text="Zoo Name").pack()
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

tk.Label(employee_block, text="Vacation").pack()
vacation_id_input = tk.Entry(employee_block, width=40)
vacation_id_input.pack(pady=5)

result = tk.Label(employee_block, text="")
result.pack(pady=5)

product_button = tk.Button(employee_block, text="Pievienot", command=addemployeeFromvlog)
product_button.pack(pady=10)
header.pack(pady = 20)

emp_tree, emp_form = make_search_table(
    employee_tab, "Meklēt darbiniekus:", ("ID", "Name", "Surname", "Zoo"),
    search_employee, update_employees, delete_employees, "employee"
)
emp_form["entries"] = [zoo_id_emp_input, name_emp_input, surname_emp_input, has_vacation_input, vacation_id_input]

#Vacation pievienot

vacation_block = tk.LabelFrame(
    vacation_tab,
    text="Vacation Information",
    font=("Arial", 18, "bold"),
    padx=10,
    pady=10
)
vacation_block.pack(padx=10, pady=10, fill="x")
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

vac_tree, vac_form = make_search_table(
    vacation_tab, "Meklēt atvaļinājumus:", ("ID", "Start", "End"),
    search_vacation, update_vacation, delete_vacation, "vacation"
)
vac_form["entries"] = [start_date_v_input, end_date_v_input]

#Vietne
if __name__ == "__main__":
    vlog.mainloop()
