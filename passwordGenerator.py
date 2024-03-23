import tkinter
import random, string
from tkinter import *
import pyperclip

#Initialize Window

root =tkinter.Tk()
root.geometry("600x600") #size of the window by default
root.resizable(0,0)
bg=tkinter.Frame(root,bg='#e6e6fa')
bg.pack(fill=BOTH,expand=True)

#title of our window
root.title("Random Password Generator")

#Random Password generator function
 
output_pass = StringVar()
 
all_combi = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]  #list of all possible characters
 
def randPassGen():
    password = "" # to store password
    for y in range(pass_len.get()):
        char_type = random.choice(all_combi)   #to randomize the occurance of alphabet, digit or symbol
        password = password + random.choice(char_type)
     
    output_pass.set(password)
 
# Copy to clipboard function
 
def copyPass():
    pyperclip.copy(output_pass.get())
 
#Front-end Designing (GUI)
 
pass_head = Label(bg, text = 'PASSWORD LENGTH', font ='Georgia 16 bold' ).pack(pady=5) #to generate label heading
 
pass_len = IntVar() #integer variable to store the input of length of the password wanted
length = Spinbox(bg, from_ = 6, to_ = 24 , textvariable = pass_len , width = 14, font='Georgia 16').pack()
 
#Generate password button
 
Button(bg, command = randPassGen, text = "GENERATE PASSWORD", font="Georgia 12 bold", bg="#FF69B4", fg='white', activebackground="teal", padx=3, pady=3 ).pack(pady= 18)
 
pass_label = Label(bg, text = 'RANDOM GENERATED PASSWORD', font = 'Georgia 12 bold').pack(pady="20 10")
Entry(bg , textvariable = output_pass, width = 20, font='Georgia 16').pack()
 
#Copy to clipboard button
 
Button(bg, text = 'COPY TO CLIPBOARD', command = copyPass, font="Georgia 12", bg='GREEN', fg='white', activebackground="teal", padx=3, pady=3 ).pack(pady= 18)
 
root.mainloop()  #to bundle pack the code for tkinter
