window.geometry('650x150')
l1 = Label(text=f'{"Given a dictionary with values , write a function that returns a key at random wit a probability proportional to the values"}').grid(row=1)
var1 = StringVar()

A={'a':1,'b':2}                       # first dict
B={'a':1,'b':1}                       # second dict
C=[A,B]                               # list of both dicts
ans = (random.choice(C))              # choose one on random to be given as output
#print(ans)                           # print the selected dict to be operated
def x():
    val1 = sum(ans.values())          # sum of total values in selected list
    vals = list(ans.values())         # list that is selected
    a = []
    for v in vals:                    # loop to deal with each value in list
        fin = (v / val1)              # value divided by total sum (probability)
        i = fin * 100                 # multiplying for percentage
        j = (round(i, 2))             # limiting to 2 values after decimal point
        a.append(float(j))
        a = [f' {j} ' for j in a]
    l3 = Label(window,textvariable=var1).grid(row=7)
    var1.set(a)

l2 = Label(text=f"{ans}").grid(row=5)
b1 = Button(window,text="CALC",command=x).grid(row=3)
window.mainloop()