import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections
class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        self.chat_area.pack(expand=True, fill=tk.BOTH)
        self.user_input = tk.Entry(root, width=40)
        self.user_input.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.X)
        send_button = tk.Button(root, text="Send", command=self.send_message)
        send_button.pack(side=tk.RIGHT, padx=10, pady=10)
        
        self.chat = Chat(ChatbotResponses.pairs, reflections)

    def send_message(self):
        user_message = self.user_input.get()
        self.user_input.delete(0, tk.END)
        response = self.chat.respond(user_message)
        self.chat_area.insert(tk.END, f"You: {user_message}\n")
        self.chat_area.insert(tk.END, f"Chatbot: {response}\n")
        self.chat_area.yview(tk.END)

class ChatbotResponses:
    pairs = [
        ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
        ['bye|goodbye', ['Goodbye!', 'Bye! Have a great day']],
        ['your name?', ['I am a Chatbot.', 'My name is Chatbot.']],
        ['What is your name?', ['I am a Chatbot.', 'My name is Chatbot.']],
        ["how are you?",["I am good and you."]],
        ["I am also good", ["great!"]],
        ["what is programming langauage?", ["A programming language is a formalized system of communication used for instructing computers. It consists of a set of rules and syntax that allows humans to create software and applications by providing specific instructions to the computer."]],
        ["what is python?",["Python is a versatile and user-friendly programming language widely used for web development, data analysis, artificial intelligence, and more."]],
        ["what is AI?",["AI, or Artificial Intelligence, refers to machines or software that can perform tasks requiring human-like intelligence, such as learning, problem-solving, and decision-making."]]
        
    ]

root = tk.Tk()
chatbot = ChatbotGUI(root)
root.mainloop()
