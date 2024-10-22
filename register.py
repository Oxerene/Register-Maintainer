from tkinter import *
from tkinter import ttk

menu_items = {
    '00 - Lunch Thali' : 40,
    '01 - Dinner Thali' : 40,
    '02 - Normal Thali' : 40,
    '03 - Outsider Thali' : 52,
    '04 - Amritsari Thali' : 60,
    '05 - Non-Veg Thali' : 65,
    '10 - Poha' : 20,
    '11 - Egg bhurji' : 20,
    '12 - Half fried Egg' : 20,
    '13 - Bread Omelette' : 20,
    '14 - Bread Butter' : 15,
    '15 - Plain Paratha' : 10,
    '16 - Aloo Parantha' : 15,
    '17 - Paneer Parantha' : 20,
    '18 - Mix Parantha' : 15,
    '20 - Paneer bhurji' : 30,
    '21 - Cheese chili' : 30,
    '22 - Manchurian' : 35,
    '23 - Grilled sandwich  (Small)' : 25,
    '24 - Grilled sandwich (Large)' : 40,
    '25 - Paneer grilled sandwich  (Small)' : 30,
    '26 - Paneer grilled sandwich (Large)' : 50,
    '27 - Fried rice' : 40,
    '28 - Egg fried rice' : 45,
    '29 - Butter maggi' : 20,
    '30 - Veg maggi' : 25,
    '31 - Plain maggi' : 15,
    '32 - Masala idli' : 40,
    '33 - Spring rolls' : 35,
    '34 - Honey chili cauliflower' : 50, 
    '35 - Honey chili potato' : 45,
    '36 - Paneer finger' : 50,
    '37 - Cutlet' : 20,
    '38 - Mushroom chili' : 20,
    '39 - Mushroom duplex' : 30,
    '40 - Mix pakoda' : 30,
    '41 - Paneer pakoda' : 40,
    '50 - Hot coffee' : 25,
    '51 - Cold Coffee (Small)' : 15,
    '52 - Cold Coffee (Large)' : 25,
    '53 - Milk tea' : 25,
    '54 - Tea' : 20,
    '55 - Ice tea' : 15,
    '56 - Born vita shake' : 25,
    '57 - Chocolate shake' : 35,
    '58 - Lassi (Namkeen)' : 20,
    '59 - Lassi (Meethi)' : 20,
    '60 - Banana Shake (Small)' : 30,
    '61 - Banana Shake (Large)' : 50,
}
menu_items_list = [i for i in sorted(menu_items.keys())]
final_items_list = {}

# Search function used to filter combobox items based on their code assigned in menu items 
def search(event):
    value = event.widget.get()  # Checks the value in the searchbox of Combobox that was entered
    
    if value == '':
        menu_item_drop['values'] = menu_items_list
    else:
        data = []

        for item in menu_items_list:
            if item.startswith(value):
                data.append(item)
            elif value.lower() in item.lower():
                data.append(item)
        menu_item_drop['values'] = data
    
# adding the item to a new final dictionary
def add_item():
    curr = menu_item_drop.current()
    if curr != -1:
        final_items_list[clicked_item.get()] = qty_var.get() * rate_var.get()
        update_listbox()
    qty_var.set(1)
    clicked_item.set('')
    menu_item_drop['values'] = menu_items_list

# adds the custom input provided to the entry box
def add_custom_item():
    val = cust_var.get()
    if val != '':
        final_items_list[val] = qty_var.get() * rate_var.get()
        update_listbox()
    cust_var.set('')
    clicked_item.set('')
    menu_item_drop['values'] = menu_items_list

# deletes the last item in the listbox
def del_item():
    item_to_del = listbox_items.get(END).split(':')[0]
    try:
        final_items_list.pop(item_to_del.strip())
    except:
        pass
    update_listbox()
    clicked_item.set('')
    menu_item_drop['values'] = menu_items_list
    qty_var.set(1)

# deletes the item currently selected in the combobox
def del_this():
    curr = menu_item_drop.current()
    if curr != -1:
        try:
            final_items_list.pop(clicked_item.get())
            update_listbox()
        except:
            pass
    qty_var.set(1)
    clicked_item.set('')
    menu_item_drop['values'] = menu_items_list

# gets total amount for the items that are added in real-time
def get_total():
    val_sum = 0
    for val in final_items_list.values():
        val_sum += val
    sum_var.set(val_sum)

# updates items each time there are  changes made to the list
def update_listbox():
    listbox_items.delete(0, END)
    for item in final_items_list:
        listbox_items.insert(END, '{} : Rs {}'.format(item, final_items_list[item]))
    item_count.set(len(final_items_list))
    get_total()

# updates the Amt. in its entry box each time a new item is selected in Combobox
def update_label(event):
    curr = menu_item_drop.current()
    val = event.widget.get()
    if curr != -1:
        rate_var.set(menu_items[val])
    

display = Tk()  
display.title('Register Calculator')
display.geometry("800x460")
display.maxsize(800, 460)
display.minsize(800, 460)

frame1 = Frame(display)
frame1.pack(anchor='w')

menu_label = ttk.Label(frame1, text='Choose Menu Item : ', font=('Ariel', 12))
menu_label.pack(side=LEFT)

# A variable to store the selected item in combobox
clicked_item = StringVar()
clicked_item.set('')
menu_item_drop = ttk.Combobox(frame1, textvariable= clicked_item, values= menu_items_list)
menu_item_drop.pack(side=LEFT, fill=X, expand=True, padx= 10)
menu_item_drop.config(width=30)


cust_var = StringVar()
cust_var.set('')
cust_label = ttk.Label(frame1, text='Add Custom Item : ', font=('Ariel', 12))
cust_label.pack(side=LEFT)
cust_item_entry = ttk.Entry(frame1, textvariable= cust_var, width=33)
cust_item_entry.pack(side=LEFT, padx=4)
add_cust = ttk.Button(frame1, text= 'Add Custom', command= add_custom_item)
add_cust.pack(side=LEFT)


# each time a new item is selected in combobox it updates the amt for the item b calling update_label function
menu_item_drop.bind('<<ComboboxSelected>>', update_label)

# Used as a filter to search for specific items whenever a key input is made in the combobox
menu_item_drop.bind('<KeyRelease>', search)

frame2 = Frame(display)
frame2.pack(fill = X, pady= 10)

# stores/updates quantity in a Integer variable 
qty_var = IntVar()
qty_var.set(1)
qty_label = ttk.Label(frame2, text='Qty. : ', font=('Ariel', 12))
qty_label.pack(side=LEFT)
qty_entry = ttk.Entry(frame2, textvariable=qty_var, width=5)
qty_entry.pack(side= LEFT)
amt_label = Label(frame2, text='Amt. :', font=('Ariel', 12))
amt_label.pack(side=LEFT, padx= 10)

# stores/updates rate for the item in a Integer variable
rate_var = IntVar()
rate_var.set(0)
rate_entry = ttk.Entry(frame2, textvariable=rate_var, width=10)
rate_entry.pack(side=LEFT)


frame3 = Frame(display)
frame3.pack(fill=X)

# adds item to the final list by calling the function add_item
add_item = ttk.Button(frame3, text='Add Item', command= add_item)
add_item.pack(padx=140, side=LEFT)

# deletion button used to delete a specific item in the final list
del_this = ttk.Button(frame3, text='Delete Above Entry', command=del_this)
del_this.pack(side=LEFT)

# deletion button to delete the last item added to the final list
del_last = ttk.Button(frame3, text='Delete Last Entry', command=del_item)
del_last.pack(side= LEFT)


frame4 = Frame(display)
frame4.pack(fill=BOTH)

# shaows the final list of items in the listbox foro convinience
listbox_items = Listbox(frame4, font=('Ariel', 12))
listbox_items.pack(side=LEFT, fill=BOTH, expand=True, pady=40)
scroll_listbox = ttk.Scrollbar(frame4)
scroll_listbox.pack(side=LEFT, fill=BOTH, pady=40)

#binds listbox to scrollbar and scrollbar to listbox
listbox_items.config(yscrollcommand=scroll_listbox.set)
scroll_listbox.config(command=listbox_items.yview)


frame5 = Frame(display)
frame5.pack(fill=X)

# Shows the Amount sum of all the item added to the final list in real-time
sum_var = IntVar()
sum_var.set(0)
sum_entry = ttk.Entry(frame5, textvariable= sum_var, width= 15)
sum_entry.pack(side=RIGHT, padx= 5)
get_sum = ttk.Label(frame5, text='Total Amt. :')
get_sum.config(font=('Ariel', 13))
get_sum.pack(side=RIGHT)

# Shows the count of all the item added to the final list in real-time
item_count = IntVar()
item_count.set(0)
total_items = ttk.Entry(frame5, textvariable=item_count, width=10)
total_items.pack(side=RIGHT, padx=5)
total_item_label = ttk.Label(frame5, text='Total Items : ', font=('Ariel', 12))
total_item_label.pack(side=RIGHT)

# mainloop
display.mainloop()