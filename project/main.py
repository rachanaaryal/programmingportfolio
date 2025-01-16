import random
import json
import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

# Initialize the main window
root = tk.Tk()
root.title("Chameli - Student Assistant")
root.geometry("600x700")  # Larger window size
root.resizable(True, True)

# Try to load the messages file
try:
    with open("chameli_messages.json", "r") as file:
        messages = json.load(file)
except FileNotFoundError:
    print("Error: chameli_messages.json file not found!")
    messages = {"messages": []}

def chatbot_response(user_input):
    # Check time request
    if "time" in user_input.lower():
        current_time = datetime.now().strftime("%H:%M")
        return f"The current time is {current_time}"
    
    # Check other patterns
    for message in messages["messages"]:
        for pattern in message["patterns"]:
            if pattern.lower() in user_input.lower():
                return random.choice(message["responses"])
    
    return "I'm sorry, I don't understand that. You can type 'help' to see what I can do!"

def handle_user_input():
    user_input = user_entry.get()
    if not user_input:  # If input is empty
        return
    
    current_time = datetime.now().strftime("%H:%M")
    chat_window.insert(tk.END, f"[{current_time}] You: {user_input}\n")
    user_entry.delete(0, tk.END)
    
    # Exit commands
    if user_input.lower() in ["bye", "quit", "exit"]:
        chat_window.insert(tk.END, "Chameli: Goodbye! Have a great day!\n")
        root.after(2000, root.destroy)
        return
    
    response = chatbot_response(user_input)
    chat_window.insert(tk.END, f"[{current_time}] Chameli: {response}\n")
    chat_window.see(tk.END)  # Auto-scroll to the latest message

def save_chat():
    try:
        with open("chat_history.txt", "w") as file:
            file.write(chat_window.get("1.0", tk.END))
        chat_window.insert(tk.END, "Chameli: Chat history has been saved!\n")
    except:
        chat_window.insert(tk.END, "Chameli: Sorry, couldn't save the chat.\n")

def clear_chat():
    chat_window.delete("1.0", tk.END)
    chat_window.insert(tk.END, "Chameli: Hi! How can I assist you today?\n")

def on_enter(event):
    handle_user_input()

# Create the chat window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=30)
chat_window.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
chat_window.insert(tk.END, "Chameli: Hi! I'm Chameli, your student assistant. Type 'help' to see what I can do!\n")

# Create the input field
user_entry = tk.Entry(root, width=40)
user_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
user_entry.bind("<Return>", on_enter)

# Create buttons
send_button = tk.Button(root, text="Send", command=handle_user_input)
send_button.grid(row=1, column=2, padx=5, pady=10)

save_button = tk.Button(root, text="Save Chat", command=save_chat)
save_button.grid(row=2, column=0, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear Chat", command=clear_chat)
clear_button.grid(row=2, column=1, padx=5, pady=5)

# Run the application
root.mainloop()