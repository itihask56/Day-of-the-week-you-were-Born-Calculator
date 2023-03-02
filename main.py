import datetime
from tkinter import *


def find():
    date = str(dob_input.get())
    day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    result_label.config(text=f"You were born on {day_name[day]}🤣", font=("Arial", "24", "bold"))


window = Tk()
window.title("Day Finder from DOB")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

dob_label = Label(text="Enter DOB(dd mm yyyy)", font=("Aria", "24", "bold"))
dob_label.grid(column=1, row=0)

dob_input = Entry(width=10)
dob_input.grid(column=1, row=1)

find_button = Button(text="Find", font=("Aria", "24", "bold"), command=find)
find_button.grid(column=1, row=2)

result_label = Label(text="🤔🤔🤔🤔🤔🤔🤔🤔🤔")
result_label.grid(column=1, row=3)
