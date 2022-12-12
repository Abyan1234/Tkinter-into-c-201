from tkinter import *
window=Tk()
window.title("Interest App")
window.geometry("500x500")
window.configure(bg="white")


def calculate_interest():
    p=float(principal.get())
    r=float(rate.get())
    t=float(time.get())
    i=(p*r*t)/100
    interest=round(i,2)

    Showlabel.destroy()
    message=Label(result_frame,text="Interest on Rs."+str(p)+"at rate of interest"+str(r)+"% for"+str(t)+"years is Rs."+str(interest),bg="grey",font=("Calibri",12))
    message.place(x=20,y=40)
    message.pack()

heading=Label(window,text="Interest Calculator", bg="white", fg="black",font=("Times New Roman",15),bd=1)
heading.place(x=200,y=30)


principal_label=Label(window,text="Your Principal:", bg="white", fg="black",font=("Times New Roman",12),bd=1)
principal_label.place(x=30,y=60)
principal=Entry(window,text="",width=30,bd=2)
principal.place(x=137,y=61)


rate_label=Label(window,text="Your rate:", bg="white", fg="black",font=("Times New Roman",12),bd=1)
rate_label.place(x=30,y=90)
rate=Entry(window,text="",width=30,bd=2)
rate.place(x=137,y=91)

time_label=Label(window,text="Your time:", bg="white", fg="black",font=("Times New Roman",12),bd=1)
time_label.place(x=30,y=120)
time=Entry(window,text="",width=30,bd=2)
time.place(x=137,y=121)


calculate=Button(window,text="Calculate",bg="red",fg="black",font=("Times New Roman",16),bd=2,command=calculate_interest)
calculate.place(x=60,y=151)

result_frame=LabelFrame(window,text="Result",bg="grey",font=("Calibri",12))
result_frame.pack(padx=20,pady=20)
result_frame.place(x=20,y=300)

Showlabel=Label(result_frame,text="Your result will be displayed here",bg="grey",font=("Calibri",12))
result_frame.pack()
result_frame.place(x=20,y=200)

window.mainloop()