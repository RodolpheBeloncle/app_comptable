from main import *
from tkinter import *
from tkinter import messagebox
from tkinter import Tk




# ---------------------------- RETURN INPUT VALUE TO LABEL ------------------#
def myInputValue(*args):
    remind_name_label.config(text=f"Dépenses " + var.get())
# ---------------------------- UI STARTER SESSION ------------------------------- #

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


    # Entries first person
    var = StringVar()
    name_input = Entry(width=21,state=NORMAL,textvariable=var)
    name_input.grid(row=1,column=1)
    name_input.focus()
    salary_var = IntVar()
    month_salary_input = Entry(width=21,textvariable=salary_var)
    month_salary_input.grid(row=2,column=1)


    #Label id_name
    var.trace("w",myInputValue)
    remind_name_label = Label(text="")
    remind_name_label.config(pady=100)
    remind_name_label.grid(column=0,row=5)

    # Entries second person
    name_input2 = Entry(width=21)
    name_input2.grid(row=1,column=4)
    name_input2.focus()
    month_salary_input2 = Entry(width=21)
    month_salary_input2.grid(row=2,column=4)

    date_label = Label(text="Date")
    date_label.place(x=10,y=250)

    intitule_label = Label(text="Intitulé")
    intitule_label.place(x=70,y=250)

    cost_label = Label(text="Coût")
    cost_label.place(x=225,y=250)


    def addBox():
        print("ADD")

        # I use len(all_entries) to get number of next free column
        next_row = len(all_entries)
        next_date = len(all_dates)
        next_check = len(all_checkBox)
        next_cost = len(all_cost)


        # add entry intitule in second row
        ent_intit = Entry(frame_for_boxes)
        ent_intit.config(width=15)
        ent_intit.grid(row=next_row, column=0)
        all_entries.append(ent_intit)

        # add entry date in second row
        ent_date = Entry(frame_for_dates)
        ent_date.config(width=4)
        ent_date.grid(row=next_date,column=0)
        all_dates.append(ent_date)

        # add checkbox in second row
        checkbutton = Checkbutton(frame_for_checkBox)
        checkbutton.grid(row=next_check,column=0)
        all_checkBox.append(checkbutton)


        intvar = IntVar()
        vars.append(intvar)
        ent_cost = Entry(frame_for_cost, text="", width=4, textvariable=vars[-1])
        ent_cost.grid(row=next_cost, column=0)
        all_cost.append(ent_cost)


    #------------------------------------

    def showEntries():

        total = 0
        for number, date in enumerate(all_dates):
            print(date.get())

        for number, ent in enumerate(all_entries):
            print(ent.get())


        for number, cost in enumerate(all_cost):
            print(type(cost.get()))

        for value in (vars):
            print(value.get())
            total += int(value.get())
        total_expense_label.config(text=f"Total Dépense: {total} euros ")
        result = int(salary_var.get()) - total
        remind_label.config(text=f"Reste après dépenses {result}")

    all_entries = []
    all_dates = []
    all_checkBox = []
    all_cost = []
    vars = []

    add_input = Button(text="+", command=addBox)
    add_input.place(x=270,y=250)

    showButton = Button(text='resumé', command=showEntries)
    showButton.place(x=300,y=250)


    frame_for_dates = Frame()
    frame_for_dates.place(x=10,y=280)

    frame_for_boxes = Frame()
    frame_for_boxes.place(x=70,y=280)

    frame_for_checkBox = Frame()
    frame_for_checkBox.place(x=270,y=280)

    frame_for_cost = Frame()
    frame_for_cost.place(x=225,y=280)

    open_session.mainloop()
    #---------------------------------------------
