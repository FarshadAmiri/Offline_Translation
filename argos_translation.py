import argostranslate.translate
import tkinter as tk
from tkinter import *
from tkinter.constants import *

def translate_argos_en_fa(article_en):
    result = argostranslate.translate.translate(article_en, 'en', 'fa',)
    return result


window = tk.Tk()
# window.geometry("1150x300")
window.resizable(False, False)
window.title("English to Persian Translator")

# Create two text areas
input_text = tk.Text(window, height=20, width=60, font=("Arial", 12), padx=4, pady=4, wrap='word', yscrollcommand=True,)
output_text = tk.Text(window, height=20, width=60, font=("Arial", 12), padx=4, pady=4, wrap='word', yscrollcommand=True, state='disabled')
output_text.tag_configure('tag-right', justify='right')

# Pack the text areas next to each other
# input_text.pack(side=tk.LEFT)
# output_text.pack(side=tk.RIGHT)

# Function to translate the text
def translate():
    english_text = input_text.get("1.0", "end-1c")
    persian_text = translate_argos_en_fa(english_text)
    output_text.configure(state='normal')
    output_text.delete("1.0", "end-1c")
    output_text.insert("1.0", persian_text, "tag-right",)
    output_text.configure(state='disabled')
    
# Define the copy function
def copy():
    # Copy the translated text to the clipboard
    window.clipboard_append(output_text.get("1.0", "end-1c"))
    
#Define a function to clear the input_text content
def clear_text():
   input_text.delete('1.0', tk.END)
    

# Add buttons
input_clear_button = tk.Button(window,text="Clear", command=clear_text, font=('Arial Rounded MT Bold',13),)
translate_button = tk.Button(window, text="Translate", command=translate, font=('Arial Rounded MT Bold', 13),)
copy_button = tk.Button(window, text="Copy", command=copy, font=('Arial Rounded MT Bold', 13),)


# Create the labels for the input and output text areas
input_label = tk.Label(window, text="English (Input)")
output_label = tk.Label(window, text="Persian (Output)")

# Grid the widgets
input_label.grid(row=0, column=0, columnspan=5, sticky="nsew")
output_label.grid(row=0, column=5, columnspan=5, sticky="nsew")
input_text.grid(row=1, column=0, columnspan=4,)
output_text.grid(row=1, column=5, columnspan=4,)
input_clear_button.grid(row=2, column=0, columnspan=1 ,sticky="nsew")
translate_button.grid(row=2, column=1, columnspan=4 ,sticky="nsew")
copy_button.grid(row=2, column=5, columnspan=5 , sticky="nsew")

window.mainloop()