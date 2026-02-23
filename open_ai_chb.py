import tkinter as tk
from openai import OpenAI

# ✅ Best practice → use environment variable
client = OpenAI()

def generate_response():
    user_text = entry.get()

    if not user_text.strip():
        return

    try:
        response = client.responses.create(
            model="gpt-4o-mini",   # ✅ Stable + fast
            input=user_text
        )

        bot_reply = response.output[0].content[0].text

        chat_box.insert(tk.END, "You: " + user_text + "\n")
        chat_box.insert(tk.END, "Bot: " + bot_reply + "\n\n")

        entry.delete(0, tk.END)

    except Exception as e:
        chat_box.insert(tk.END, "ERROR: " + str(e) + "\n\n")


# ✅ GUI Window
root = tk.Tk()
root.title("OpenAI Chatbot")

chat_box = tk.Text(root, height=20, width=50)
chat_box.pack()

entry = tk.Entry(root, width=40)
entry.pack()

submit_button = tk.Button(root, text="Submit", command=generate_response)
submit_button.pack()

root.mainloop()