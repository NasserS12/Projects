# Import Required Library
from tkinter import*
import os



# Create Object
root = Tk()
# Set Geometry
root.geometry('950x450+1500+700')
# Set Title
root.title('Welcome to my App')
# Set Resizable = controls whether the window can be resized or not
root.resizable(False,False)
# Set Config =  main color for Tk window
root.config(bg="gray")

# Load text from external files
# Using BASE_DIR ensures paths work regardless of where the program is run
BASE_DIR = os.path.dirname(__file__)
def load_text(file_name):
    path = os.path.join(BASE_DIR, file_name)
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

# Poems Section
# Each function opens a new window (Toplevel) and loads content from text files
def about_poems():
    win = Toplevel()
    win.geometry('800x400+1500+700')
    win.resizable(False,False)
    win.title("About Poems")
    win.config(bg='gray')
    welcome_text = load_text("Texts/welcome_text/welcome_Poems.txt")
    lbl1 = Label(win,text=welcome_text,font=('arial',14),bg='white')
    lbl1.place(x=150,y=10)
    bt = Button(win,text=("1 About : Hope And Optimism"),font=("arial",14)
                ,command=inside_poem1_hope,highlightbackground="black",highlightthickness=2)
    bt.place(x=310,y=210)
    bt1 = Button(win,text=("2 About : Nature"),font=('arial',14)
                 ,command=inside_poem2_Nature,highlightbackground="black",highlightthickness=2)
    bt1.place(x=310,y=260)
# Inside Optaion Hope
def inside_poem1_hope():
    win1 = Toplevel()
    win1.geometry("900x400+1500+700")
    win1.resizable(False,False)
    win1.title("Hope")
    win1.config(bg='gray')
    lable1 = Label(win1,text=('🌅 Hope And Optimism 🌅'),font=('arial',14),bg='white',fg="#274460")
    lable1.place(x=330,y=20)
    text = load_text('Texts/Poems/hope.txt')
    label2 = Label(win1,text=text,font=('arial',14),fg="#274460")
    label2.place(x=10,y=90)     
# Inside Optaion Nature
def inside_poem2_Nature():
    win2 = Toplevel()
    win2.geometry("900x330+1500+700")
    win2.resizable(False,False)
    win2.title("Nature ")
    win2.config(bg="gray")
    lab1 = Label(win2,text=(" 🌿 The Beauty of Nature 🌿"),font=('arial',14),bg='white',fg="#274460")
    lab1.place(x=320,y=20)
    text = load_text("Texts/Poems/nature.txt")
    lab2 = Label(win2,text=text,font=("arial",14),fg="#274460")
    lab2.place(x=25,y=90)

# Articles Section
# Each function opens a new window (Toplevel) and loads content from text files
def about_Articles():
    win = Toplevel()
    win.geometry("800x400+1500+700")
    win.resizable(False,False)
    win.title("About Articles")
    win.config(bg=("gray"))
    Text = load_text("Texts/welcome_text/welcome_articles.txt")
    label = Label(win,text=Text,font=('arial',14),bg='white')
    label.place(x=150,y=10)
    btn = Button(win,text="1 About : The Journey of Self-Improvement ",font=('arial',12)
                 ,command=inside_article1,highlightbackground="black",highlightthickness=2)
    btn.place(x=250,y=210)
    btn1 = Button(win,text="2 About : The Value of Time ",font=('arial',12)
                  ,command=inside_article2,highlightbackground="black",highlightthickness=2)
    btn1.place(x=250,y=260)
# Inside Optaion Journey
def inside_article1():
    win = Toplevel()
    win.geometry("855x330+1500+700")
    win.resizable(False,False)
    win.title("The Journey")
    win.config(bg="gray")
    Label1 = Label(win,text="🚀 The Journey of Self-Improvement 🚀",font=("arial",14),bg='white',fg="#274460")
    Label1.place(x=260,y=20)
    text = load_text("Texts/Articles/journey.txt")
    Label2 = Label(win,text=text,font=("arial",14),fg="#274460")
    Label2.place(x=50,y=90)
# Inside Optaion Time
def inside_article2():
    win = Toplevel()
    win.geometry("900x350+1500+700")
    win.resizable(False,False)
    win.title("Time")
    win.config(bg="gray")
    Label1 = Label(win,text="⏰ The Value of Time ⏰",font=("arial",14),bg='white',fg="#274460")
    Label1.place(x=340,y=20)
    text = load_text('Texts/Articles/Time.txt')
    Label2 = Label(win,text=text,font=("arial",14),fg="#274460")
    Label2.place(x=50,y=90)

# Quotes Section
# Each function opens a new window (Toplevel) and loads content from text files
def About_Quotes():
    win = Toplevel()
    win.geometry("800x400+1500+700")
    win.resizable(False,False)
    win.title("About Quotes")
    win.config(bg="gray")
    Text = load_text('Texts/welcome_text/welcome_quotes.txt')
    Label1 = Label(win,text=Text,font=("arial",14),bg='white')
    Label1.place(x=120,y=20)
    btn = Button(win,text="1 About : The Power of Quotes",font=("arial",13)
                 ,command=inside_quotes1,highlightbackground="black",highlightthickness=2)
    btn.place(x=250,y=230)
    btn1 = Button(win,text="2 About : The Art of Quotes",font=("arial",14)
                  ,command=inside_quotes2,highlightbackground="black",highlightthickness=2)
    btn1.place(x=250,y=290)
# Inside Optaion Power
def inside_quotes1():
    win = Toplevel()
    win.geometry("900x360+1500+700")  
    win.resizable(False,False)
    win.title("Power of Quotes")
    win.config(bg="gray")
    Label1 = Label(win,text=" 💬 The Power of Quotes 💬",font=("arial",14),bg='white',fg="#274460")
    Label1.place(x=320,y=30)
    text = load_text("Texts/Quotes/power.txt")
    Label2 = Label(win,text=text,font=("arial",14),fg="#274460")
    Label2.place(x=0,y=100)
# Inside Optaion Art
def inside_quotes2():
    win = Toplevel()
    win.geometry("950x380+1500+700")
    win.resizable(False,False)
    win.title("Art of Quotes")
    win.config(bg="gray")
    Label1 = Label(win,text=" 💬 The Art of Quotes 💬",font=("arial",14),bg='white',fg="#274460")
    Label1.place(x=350,y=30)
    text = load_text("Texts/Quotes/art.txt")
    Label2 = Label(win,text=text,font=("arial",14),fg="#274460")
    Label2.place(x=0,y=100)

# Main interface:
# Displays the app title, welcome message, and navigation buttons
label1 = Label(root,text='🌟 Hello and Welcome to Knowledge Collector! 🌟\nBringing Inspiration Your Way\nBy Nasser',font=('arial',15),bg='white')
label1.place(x=250,y=10)
main_Text = load_text('Texts/welcome_text/main_welcome.txt')
label2 = Label(root,text=main_Text,font=('arial',15),bg='gray')
label2.place(x=160,y=100)

bt1 = Button(root,text="1 - Quotes",font=('arial',14)
             ,command=About_Quotes,highlightbackground="black",highlightthickness=2)
bt1.place(x=410,y=230)
bt2 = Button(root,text="2 - Articles",font=('arial',14)
             ,command=about_Articles,highlightbackground="black",highlightthickness=2)
bt2.place(x=410,y=280)
bt3 = Button(root,text="3 - Poems",font=('arial',14)
             ,command=about_poems,highlightbackground="black",highlightthickness=2)
bt3.place(x=410,y=330)

# Execute Tkinter
root.mainloop()


