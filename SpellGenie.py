'''PYHTON PROJECT
 ================
NAME OF PROJECT: SPELL GENIE-YOUR PERSONAL SPELLING ASSISTANT 

'''
#pip install textblob

#1. Importing the module

from textblob import TextBlob
from tkinter import*

#2. Creating the GUI
#Then we create an empty GUI for adding the widgets.
#CREATING WINDOW
win=Tk()
win.geometry('500x400')
win.resizable(False,False)
win.config(bg='#dae6f6')
win.title('Python Project')
heading=Label(win,text='SpellGenie',font=('Times New Roman',25,'bold'),bg='#dae6f6',fg='#364971')
heading.pack(pady=(50,0))

def correct_spelling():
    word=enter1.get()
    a=TextBlob(word)
    right=str(a.correct())

    cs=Label(win,text='Correct text is:',font=('Times New Roman',25),bg='#dae6f6',fg='#364971')
    cs.place(x=100,y=250)
    spell.config(text=right)


#3. Adding the required widgets  
enter1=Entry(win,justify='center',width=30,font=('Times New Roman',25),bg='white',border=2)
enter1.pack(pady=10)
enter1.focus()
button=Button(win,text='Check',font=('Times New Roman',25,'bold'),fg='white',bg='red',command=correct_spelling)
button.pack()
spell=Label(win,font=('Times New Roman',20),bg='#dae6f6',fg='#364971')
spell.place(x=350,y=250)

win.mainloop()
