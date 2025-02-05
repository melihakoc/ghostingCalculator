import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage


def calculate_ghosting_probability():
    score = 0

    # Example scoring logic
    if response_time_var.get() == "More than a day":
        score += 30
    elif response_time_var.get() == "A few hours":
        score += 10

    if online_no_reply_var.get() == "Yes":
        score += 40

    if excuse_var.get() == "Yes, frequently":
        score += 20

    if watched_story_var.get() == "Yes":
        score += 20

    if watched_reels_var.get() == "No":
        score += 15

    if sent_reels_var.get() == "More than a week ago" or sent_reels_var.get() == "N/A":
        score += 25

    if likes_stories_var.get() == "No":
        score += 15

    if bad_influence_trip_var.get() == "Yes":
        score += 30

    if relationship_status_var.get() == "Situationship":
        score += 25
    elif relationship_status_var.get() == "Flirt":
        score += 15

    # Normalize score to percentage
    ghosting_probability = min(score, 100)

    result_message = f"Ghosting Probability: {ghosting_probability}%\n"
    if ghosting_probability < 30:
        result_message += "You're probably safe! 🫡"
    elif ghosting_probability < 60:
        result_message += "Might be losing interest... 😬"
    else:
        result_message += "They're definitely ghosting you. 💀"

    messagebox.showinfo("Result", result_message)


# GUI Setup
root = tk.Tk()
root.title("Are They Ghosting Me?")
root.geometry("450x550")
root.configure(bg="#ffb6c1")

# Styling
label_style = {"bg": "#ffb6c1", "fg": "#6d001a", "font": ("Arial", 12, "bold")}
button_style = {"bg": "#ff1493", "fg": "#ffffff", "font": ("Arial", 12, "bold"), "padx": 10, "pady": 5}

# Question 1
response_time_var = tk.StringVar(value="Less than an hour")
tk.Label(root, text="How long has it been since they last replied?", **label_style).pack(pady=5)
tk.OptionMenu(root, response_time_var, "Less than an hour", "A few hours", "More than a day").pack()

# Question 2
online_no_reply_var = tk.StringVar(value="No")
tk.Label(root, text="Are they online but not responding?", **label_style).pack(pady=5)
tk.OptionMenu(root, online_no_reply_var, "No", "Yes").pack()

# Question 3
excuse_var = tk.StringVar(value="No")
tk.Label(root, text="Have they made excuses for not meeting up?", **label_style).pack(pady=5)
tk.OptionMenu(root, excuse_var, "No", "Yes, once", "Yes, frequently").pack()

# Question 4
watched_story_var = tk.StringVar(value="No")
tk.Label(root, text="Have they watched your stories but ignored your texts?", **label_style).pack(pady=5)
tk.OptionMenu(root, watched_story_var, "No", "Yes").pack()

# New Questions
watched_reels_var = tk.StringVar(value="No")
tk.Label(root, text="Did they watch the reels you sent them?", **label_style).pack(pady=5)
tk.OptionMenu(root, watched_reels_var, "No", "Yes").pack()

sent_reels_var = tk.StringVar(value="N/A")
tk.Label(root, text="When was the last time they sent reels?", **label_style).pack(pady=5)
tk.OptionMenu(root, sent_reels_var, "Today", "This week", "More than a week ago", "N/A").pack()

likes_stories_var = tk.StringVar(value="Yes")
tk.Label(root, text="Do they still like your stories?", **label_style).pack(pady=5)
tk.OptionMenu(root, likes_stories_var, "Yes", "No").pack()

bad_influence_trip_var = tk.StringVar(value="No")
tk.Label(root, text="Are they on a trip with the bad influence friend?", **label_style).pack(pady=5)
tk.OptionMenu(root, bad_influence_trip_var, "No", "Yes").pack()

relationship_status_var = tk.StringVar(value="Boyfriend")
tk.Label(root, text="What's your relationship status?", **label_style).pack(pady=5)
tk.OptionMenu(root, relationship_status_var, "Boyfriend", "Flirt", "Situationship").pack()

# Heart-shaped button image
heart_image = PhotoImage(file="heart_button.png")
heart_button = tk.Button(root, text="Check", image=heart_image, command=calculate_ghosting_probability, borderwidth=0)
heart_button.pack(pady=10)

root.mainloop()
