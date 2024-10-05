from tkinter import *
import random
from tkinter import messagebox

window=Tk()
window.title('Jumbled words game')
window.geometry("400x400")
window.config(background="black")

score = 0
answer = ["apple","pencilcase","calculator","bottle","rubber","laptop","book","bookshelf","table","chair","watermelon"]
jumbled_words_2 = ["paelp","clicnepsa","acoctlrlau","bletot","rbrueb","lppaot","boko","oolbesfkh","taebl","chrai","aeowlmnter"]

index = random.randint(0,11)

def jumble():
    global index,score
    index = random.randint(0,11)
    score = 0
    enter_word.delete(0,END)
    jumbled_word.config(text=jumbled_words_2[index-1],fg="white")
    score2.config(text=f"Score:{score}")

def check():
    global index,score
    user_answer = enter_word.get()
    if user_answer == answer[index-1]:
        messagebox.showinfo("correct","You got the correct answer!")
        score += 1
        score2.config(text=f"Score:{score}")
        enter_word.delete(0,END)
        index = random.randint(0,11)
        jumbled_word.config(text=jumbled_words_2[index-1],fg="white")
    else:
        score -= 1
        messagebox.showinfo("wrong","You got it wrong :( try again")
        score2.config(text=f"Score:{score}")
        enter_word.delete(0,END)
        index = random.randint(0,11)
        jumbled_word.config(text=jumbled_words_2[index-1],fg="white")

score2 = Label(window,text="Score:{}".format(score),background="black",fg="white",font=("Aerial",16))
score2.place(x=50,y=300)
jumbled_word_game = Label(window,text="JUMBLED WORD GAME",background="black",fg="white",font=("Aerial",16))
jumbled_word_game.pack(side=TOP)

jumbled_word = Label(window,text=jumbled_words_2[index-1],background="black",fg="white",font=("Aerial",12))
jumbled_word.place(x=175,y=100)

enter_word = Entry(window,width=30)
enter_word.place(x=105,y=150,height=30)

check_button = Button(window,text="Check",command=check)
reset_button = Button(window,text="Reset",command=jumble)
check_button.place(x=175,y=200)
reset_button.place(x=175,y=250)





window.mainloop()