#Age Calculator with TKINTER window for GUI

from tkinter import *
from datetime import date
root = Tk()
root.geometry('250x200')
root.title('Age Calculator')

def calc():
    today = date.today()                                                          # today's date
    bday = date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get()))   # your birth date
    def ageyr():
        return ((today.year)-(bday.year))                                         # subtracting year
    def agemth():
        return ((today.month)-(bday.month))                                       # subtracting month
    def ageday():
        return ((today.day)-(bday.day))                                           # subtracting days
    Label(text=f"{nameValue.get()} your age is \n{ageyr()}years {agemth()}months & {ageday()}days").grid(row=6, column=2) # display result

nameValue=StringVar()
yearValue=StringVar()
monthValue=StringVar()
dayValue=StringVar()

Label(text='Name').grid(row=1,column=1)
Label(text='Year').grid(row=2,column=1)
Label(text='Month').grid(row=3,column=1)
Label(text='Date').grid(row=4,column=1)

nameEntry = Entry(root,textvariable=nameValue)                                   # enter your name
yearEntry = Entry(root,textvariable=yearValue)                                   # enter your birth year
monthEntry = Entry(root, textvariable=monthValue)                                # enter your birth month number
dayEntry = Entry(root,textvariable=dayValue)                                     # enter your birth date
nameEntry.grid(row=1,column=2,padx=5)
yearEntry.grid(row=2,column=2,padx=5)
monthEntry.grid(row=3,column=2,padx=5)
dayEntry.grid(row=4,column=2,padx=5)
Button(text='CALCULATE AGE',command=calc).grid(row=5,column=2,pady=10)
root.mainloop()