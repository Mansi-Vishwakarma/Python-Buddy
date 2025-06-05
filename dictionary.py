import tkinter as tk
from tkinter import messagebox

# Function to load the dictionary data from a file
def load_dictionary():
    dictionary = {}
    try:
        with open("dictionary.txt", "r") as file:
            for line in file:
                word, definition = line.strip().split(":")
                dictionary[word] = definition
    except FileNotFoundError:
        pass  # File doesn't exist yet
    return dictionary

# Function to save the dictionary data to a file
def save_dictionary(dictionary):
    with open("dictionary.txt", "w") as file:
        for word, definition in dictionary.items():
            file.write(f"{word}:{definition}\n")

# Function to add a new word to the dictionary
def add_word():
    word = word_entry.get().strip().lower()
    definition = definition_entry.get().strip()
    
    if not word or not definition:
        messagebox.showerror("Error", "Word and definition cannot be empty.")
        return
    
    dictionary[word] = definition
    save_dictionary(dictionary)
    word_entry.delete(0, tk.END)
    definition_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Word added to the dictionary.")

# Function to search for a word in the dictionary
def search_word():
    word = search_entry.get().strip().lower()
    if word in dictionary:
        definition = dictionary[word]
        messagebox.showinfo("Definition", f"{word}: {definition}")
    else:
        messagebox.showerror("Error", f"{word} not found in the dictionary.")

# Create the main window
window = tk.Tk()
window.title("Dictionary")

# Load the dictionary data
dictionary = load_dictionary()

# Create and configure widgets
word_label = tk.Label(window, text="Word:")
word_entry = tk.Entry(window, width=30)
definition_label = tk.Label(window, text="Definition:")
definition_entry = tk.Entry(window, width=50)
add_button = tk.Button(window, text="Add Word", command=add_word)
search_label = tk.Label(window, text="Search for a Word:")
search_entry = tk.Entry(window, width=30)
search_button = tk.Button(window, text="Search", command=search_word)

# Layout widgets
word_label.grid(row=0, column=0, padx=10, pady=10)
word_entry.grid(row=0, column=1, padx=10, pady=10)
definition_label.grid(row=1, column=0, padx=10, pady=10)
definition_entry.grid(row=1, column=1, padx=10, pady=10)
add_button.grid(row=2, column=1, padx=10, pady=10)
search_label.grid(row=3, column=0, padx=10, pady=10)
search_entry.grid(row=3, column=1, padx=10, pady=10)
search_button.grid(row=4, column=1, padx=10, pady=10)

# Start the main loop
window.mainloop()