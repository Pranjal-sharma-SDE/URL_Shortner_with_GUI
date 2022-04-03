from tkinter import *
import pyshorteners as p


def Shorten():
    if Shorty.get():
        Shorty.delete(0,END)
 
    if my_e.get():
        url= p.Shortener().tinyurl.short(my_e.get())
        Shorty.insert(END, url)
         
        print(p.Shortener().tinyurl.expand(url))

       




root=Tk()
root.title('Pj_URL Shorter')
root.iconbitmap('D:/pysort/tx.ico')
root.geometry("1000x1000")

my_label= Label(root, text="Enter Link To Shortner", font=("Helvetica", 36))
my_label.pack(pady=27) 
my_e = Entry(root,font=("Helvetica", 36))
my_e.pack(pady=27)

my_button= Button(root,text="Shorten Link", command=Shorten, font=("Helvetica", 36))

my_button.pack(pady=27)

shorty_label= Label(root,text="Shorten Link",  font=("Helvetica", 36))
shorty_label.pack(pady=18)

Shorty =Entry(root, font=("Helvetica", 36), justify=CENTER, width=30,bd=0,bg="systembuttonface")
Shorty.pack(pady=27)


root.mainloop()
