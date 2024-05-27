import tkinter as tk

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg='black')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

label = tk.Label(root, text="mas smolu", font=("Helvetica", 72), bg='black')
label.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()