import random

BACKGROUND_COLOR = "#B1DDC6"

import  tkinter
from tkinter import *
import  pandas
import random

data = pandas.read_csv("data/french_words.csv")
to_learn  = data.to_dict(orient="records")

def next_card():
    global current_card , flip_timer
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title , text="French" , fill="black")
    canvas.itemconfig( card_word,text = current_card["French"]  , fill="black")
    canvas.itemconfig(background, image=card_front_image)

    # time after which the card the flip
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    #text on the english side
    canvas.itemconfig(card_title ,text="English" , fill="white" )
    canvas.itemconfig(card_word, text=current_card["English"] , fill="white")

    #image on the english side
    canvas.itemconfig(background , image=card_back_image)



window= tkinter.Tk()
window.title("Flash Card Project")
window.config(pady=50 , padx=50 , bg=BACKGROUND_COLOR )

#time after which the card the flip
flip_timer=window.after(3000 , func=flip_card)

#image on the card of the french side
canvas = Canvas(width=800 , height=526)
card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")
background = canvas. create_image(400 , 263 , image = card_front_image )
canvas.config(bg=BACKGROUND_COLOR  , highlightthickness=0)

#text on the card  of french side
card_title = canvas.create_text(400 , 150 , text="Title" , font=("Ariel", 40 , "italic"))
card_word = canvas.create_text(400 , 263 , text="Word" , font=("Ariel", 60 , "bold"))

canvas.grid(row=0 , column=0 , columnspan=2)

unknown_image = PhotoImage(file= "images/wrong.png")
unknown_button = Button(image= unknown_image , command=next_card)
unknown_button.config(highlightthickness=0)
unknown_button.grid(row=1 , column=0)

known_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_image , command=next_card )
known_button.config(highlightthickness=0)
known_button.grid(row=1 , column=1)



next_card()



window.mainloop()

