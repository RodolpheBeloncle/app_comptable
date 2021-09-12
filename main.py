from tkinter import Tk,messagebox
from tkinter import *
import sys
import os
from session import *
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

validate_button = Button(text=button_label, width=20,height=2, command=save)
validate_button.grid(row=4, column=1, columnspan=2)


window.mainloop()







