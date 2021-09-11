from doctest import master
from tkinter import *
from tkinter import messagebox, ttk
from random import choice, randint, shuffle
import pyperclip
import json

button_label = ""
on_session = False



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    global window
    global validate_button
    global on_session


    name_field = id_entry.get()
    password_field = password_entry.get()
    new_data = {
        "nom": name_field,
        "password": password_field,
    }
    message = "Valider ?"
    if len(name_field) == 0 or len(password_field) == 0:
        messagebox.showinfo(title="Oops", message="Remplisser les champs vides")

    else:

        validation = messagebox.askokcancel(title="Validation", message=message)
        if validation:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json","w") as data_file:
                    json.dump(new_data,data_file,indent=4)
                    validate_button.destroy()
                    # Second Button
                    validate_b = Button(text="Entrez vos Identifiant", width=20, command=save)
                    validate_b.grid(row=4, column=1, columnspan=2)

            else:
                if data["password"] != password_field:
                    messagebox.showinfo(title="Erreur", message="Mauvais mot de passe")

                else:
                    on_session = True
                    window.destroy()

            finally:
                id_entry.delete(0, END)
                password_entry.delete(0, END)


def check_data():
    global button_label

    try:
        with open("data.json","r") as data_file:
            #Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        # Change button Label
        button_label = "Créer Mot de passe"


    else:
        # Change button Label
        button_label = "Entrez vos Identifiant"


# ---------------------------- UI STARTER SETUP ------------------------------- #



#check if any recorded data exist
window = Tk()
window.geometry('+800+200')
window.title("Authentification")
window.config(padx=50,pady=50)


canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

check_data()

#Labels
name_label = Label(text="Nom:")
name_label.grid(row=1, column=0)
password_label = Label(text="Mot de Passe:")
password_label.grid(row=2, column=0)

#Entries
id_entry = Entry(width=21)
id_entry.grid(row=1, column=1)
id_entry.focus()
password_entry = Entry(width=21)
password_entry.grid(row=2, column=1)

# Button

validate_button = Button(text=button_label, width=20, command=save)
validate_button.grid(row=4, column=1, columnspan=2)



window.mainloop()
# ---------------------------- RETURN INPUT VALUE TO LABEL ------------------#
def myInputValue(*args):
    remind_name_label.config(text=f"Dépenses " + var.get())
# ---------------------------- UI STARTER SESSION ------------------------------- #
global open_session
#Open session My_Comptable

if on_session == True:
    open_session = Tk()

# set session
open_session.title("Comptabilité")
open_session.geometry('+800+200')
open_session.geometry('800x800')

#Label first person
name_label = Label(text="Prénom:")
name_label.grid(row=1,column=0)
salary_label = Label(text="Salaire:")
salary_label.grid(row=2,column=0)
total_expense_label = Label(text="Total Dépense:")
total_expense_label.grid(row=3,column=0)
remind_label = Label(text="Reste après dépense: ")
remind_label.grid(row=4,column=0)



#Label second person
name_label2 = Label(text="Prénom:")
name_label2.grid(row=1,column=3)
name_label2.config(padx=20)
salary_label2 = Label(text="Salaire:")
salary_label2.grid(row=2,column=3)
salary_label2.config(padx=20)
total_expense_label2 = Label(text="Total Dépense:")
total_expense_label2.grid(row=3,column=3)
total_expense_label2.config(padx=20)
remind_label2 = Label(text="Reste après dépense: ")
remind_label2.grid(row=4,column=3)
remind_label2.config(padx=20)


separator = ttk.Separator(master, orient=VERTICAL)
separator.place(relx=0.45, rely=0, relheight=0.9, relwidth=0.005)

# Entries first person
var = StringVar()
name_input = Entry(width=21,state=NORMAL,textvariable=var)
name_input.grid(row=1,column=1)
name_input.focus()
month_salary_input = Entry(width=21)
month_salary_input.grid(row=2,column=1)


var.trace("w",myInputValue)
remind_name_label = Label(text="")
remind_name_label.grid(column=0,row=5)

# Entries second person
name_input2 = Entry(width=21)
name_input2.grid(row=1,column=4)
name_input2.focus()
month_salary_input2 = Entry(width=21)
month_salary_input2.grid(row=2,column=4)


#---------------------------------------------




#Text
text = Text(height=5, width=30,highlightthickness=0,bg="#f7f5dd")
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Remarques: ")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.grid(row=8,column=1)


#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid(row=7,column=4)


#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.grid(row=9,column=4)


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(row=12,column=4)


open_session.mainloop()
