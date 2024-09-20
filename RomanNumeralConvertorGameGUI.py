# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:01:30 2021

@author: Ahaan
"""

import tkinter as tk
from tkinter import messagebox
import random
import time

numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
game_list = ["III", "VII", "CII", "CXVI", "DCCCI", "MDI", "XCIX", "XLIX", "MDCCCLXXXIV", "MMMMDCCCXCI"]
points = 3
current_numeral = None

def validate_roman_numeral(numeral):
    valid_chars = set("IVXLCDM")
    for char in numeral:
        if char not in valid_chars:
            return False
    return True

def roman_to_decimal(numeral):
    values = [numerals[x] for x in numeral]
    add = 0
    for x in range(len(numeral)):
        val_x = values[x]
        if x != 0:
            val_xn = values[x - 1]
            if val_x > val_xn:
                add += (val_x - 2 * val_xn)
            else:
                add += val_x
        else:
            add += val_x
    return add

def start_game():
    global current_numeral, points
    current_numeral = random.choice(game_list).upper()
    if not validate_roman_numeral(current_numeral):
        messagebox.showerror("Error", "Invalid Roman numeral in game list.")
        return
    numeral_label.config(text=f"What is {current_numeral} as a decimal number?")
    points_label.config(text=f"Points: {points}")

def check_answer():
    global points, current_numeral
    try:
        answer = int(answer_entry.get())
        correct_answer = roman_to_decimal(current_numeral)
        
        if answer == correct_answer:
            messagebox.showinfo("Correct!", "Congratulations! You guessed the right answer.")
            points += 1
        else:
            messagebox.showerror("Incorrect", f"The correct answer for {current_numeral} is {correct_answer}.")
            points -= 1
            
        if points == 0:
            restart = messagebox.askyesno("Game Over", "You have 0 points. Do you want to restart?")
            if restart:
                points = 3
                start_game()
            else:
                root.quit()
        else:
            start_game()
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid decimal number.")
    
    points_label.config(text=f"Points: {points}")
    answer_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Roman Numeral Game")

welcome_label = tk.Label(root, text="Welcome to the Roman Numeral Game", font=("Arial", 16), pady=10)
welcome_label.pack()

numeral_label = tk.Label(root, text="Press Start to begin!", font=("Arial", 14), pady=10)
numeral_label.pack()

answer_entry = tk.Entry(root, font=("Arial", 14))
answer_entry.pack()

points_label = tk.Label(root, text=f"Points: {points}", font=("Arial", 14), pady=10)
points_label.pack()

start_button = tk.Button(root, text="Start Game", font=("Arial", 14), command=start_game)
start_button.pack(pady=10)

submit_button = tk.Button(root, text="Submit Answer", font=("Arial", 14), command=check_answer)
submit_button.pack(pady=10)

root.mainloop()
