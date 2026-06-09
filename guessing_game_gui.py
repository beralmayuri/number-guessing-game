import tkinter as tk
import random

number = random.randint(1, 100)
attempts = 7

def check_guess():
    global attempts
    guess = int(entry.get())
    attempts = attempts - 1
    
    if guess > number:
        result_label.config(text=f"Too high! 🔺 Attempts left: {attempts}")
    elif guess < number:
        result_label.config(text=f"Too low! 🔻 Attempts left: {attempts}")
    else:
        result_label.config(text="Correct! You got it 🎉")
        button.config(state="disabled")
        return
    
    if attempts == 0:
        result_label.config(text=f"Game Over! The number was {number} 😢")
        button.config(state="disabled")

window = tk.Tk()
window.title("Number Guessing Game")

title = tk.Label(window, text="Number Guessing Game 🎮", font=("Arial", 20, "bold"))
title.pack(pady=20)

label = tk.Label(window, text="Guess a number between 1 and 100:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=10)

button = tk.Button(window, text="Guess", font=("Arial", 12), command=check_guess)
button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

window.mainloop()