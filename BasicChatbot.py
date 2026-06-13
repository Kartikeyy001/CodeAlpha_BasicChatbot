import tkinter as tk

root = tk.Tk()
root.title("Basic Chatbot")
root.geometry("500x400")

chat_area = tk.Text(root, height=15, width=50)
chat_area.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=10)

def reply():
    user = entry.get().lower()

    chat_area.insert(tk.END, f"You: {user}\n")

    if user == "hello":
        bot = "Hi!"
    elif user == "how are you":
        bot = "I'm fine, thanks!"
    elif user == "bye":
        bot = "Goodbye!"
    else:
        bot = "I don't understand."

    chat_area.insert(tk.END, f"Bot: {bot}\n\n")

    entry.delete(0, tk.END)

send_button = tk.Button(root, text="Send", command=reply)
send_button.pack(side=tk.LEFT)

root.mainloop()
