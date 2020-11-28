import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
# root.geometry('500*500')
root.title('Dice Simulator')

Line = tkinter.Label(root, text="")
Line.pack()

simulatorLabel = tkinter.Label(root, text="Dice Simulator Using Python", fg="light green", bg="dark green", font="Helvetica 16 bold italic")
simulatorLabel.pack()

#images which will be simulated
dice = ['DiceImages/dice1.png', 'DiceImages/dice2.png', 'DiceImages/dice3.png', 'DiceImages/dice4.png', 'DiceImages/dice5.png', 'DiceImages/dice6.png']

DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage

ImageLabel.pack(expand=True)

def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    ImageLabel.configure(image=DiceImage)
    ImageLabel.image = DiceImage

button = tkinter.Button(root, text="Roll the Dice", fg='blue', command=rolling_dice)
button.pack( expand=True)

root.mainloop()
