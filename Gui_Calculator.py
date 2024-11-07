import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    else:
        current_text = screen_var.get()
        screen_var.set(current_text + text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x600")  # Set the size of the main window

# Create a StringVar to hold the value displayed in the entry widget
screen_var = tk.StringVar()
screen_var.set("")

# Create the entry widget for display
screen = tk.Entry(root, textvar=screen_var, font="Arial 20 bold", bd=8, relief=tk.SUNKEN, bg="lightgray")
screen.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10)

# Create a frame for the buttons
frame = tk.Frame(root)
frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Add buttons to the grid with styling
for i, button in enumerate(buttons):
    b = tk.Button(frame, text=button, font="Arial 20 bold", padx=20, pady=20, bg="white", fg="black", relief=tk.RAISED)
    b.grid(row=i//4, column=i%4, padx=10, pady=10)
    b.bind("<Button-1>", click)

root.mainloop()
