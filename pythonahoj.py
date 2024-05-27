import tkinter as tk

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg='white')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

label = tk.Label(root, text="AHOJ", font=("Helvetica", 72), bg='white')
label.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()