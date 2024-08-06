import tkinter as tk
import time
import winsound


def animate_text(label, text):
    for char in text:
        label.config(text=label.cget("text") + char)
        root.update()
        time.sleep(0.1)  

def clear_text():
    label2.config(text="")
    label3.config(text="")
    label4.config(text="")

def clear_text2():
    label5.config(text="")
    label6.config(text="")
    label7.config(text="")
    label8.config(text="")
    label9.config(text="")
    label10.config(text="")


def on_button_click():
    button.place_forget()  
    root.after(10, clear_text2) 

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("DARK NET")
root.geometry("800x600")
root.configure(bg='black')


label1 = tk.Label(root, text="", font=("Courier New", 95), bg='black', fg="white")
label1.place(x=80, y=50)

label2 = tk.Label(root, text="", font=("Courier New", 50), bg='black', fg="white")
label2.place(x=80, y=230)

label3 = tk.Label(root, text="", font=("Courier New", 50), bg='black', fg="white")
label3.place(x=80, y=330)

label4 = tk.Label(root, text="", font=("Courier New", 50), bg='black', fg="white")
label4.place(x=80, y=430)

winsound.PlaySound(r'Typing Sound Effect', winsound.SND_FILENAME)

animate_text(label1, "DARK NET")
animate_text(label2, "1 here you only pay with bitcoins")
animate_text(label3, "2 you can buy a monkey, and so on")
animate_text(label4, "3 We are not responsible for any damages")



root.after(10, clear_text)  

label5 = tk.Label(root, text="", font=("Courier New", 60), bg='black', fg="white")
label5.place(x=80, y=230)

label6 = tk.Label(root, text="", font=("Courier New", 50), bg='black', fg="white")
label6.place(x=80, y=330)

label7 = tk.Label(root, text="", font=("Courier New", 50), bg='black', fg="white")
label7.place(x=80, y=430)

label8 = tk.Label(root, text="", font=("Courier New", 50), bg='black', fg="white")
label8.place(x=80, y=530)

label9 = tk.Label(root, text="", font=("Courier New", 50), bg='black', fg="white")
label9.place(x=80, y=630)

label10 = tk.Label(root, text="", font=("Courier New", 50), bg='black', fg="white")
label10.place(x=80, y=730)

animate_text(label5, "Agreement to Site Rules:")
animate_text(label6, "You must agree to comply with ")
animate_text(label7, "all rules and regulations stated on our site")
animate_text(label8, "Responsibility for Actions: You agree to be ")
animate_text(label9, "fully responsible for all your actions and ")
animate_text(label10, "transactions made on our website.")

button = tk.Button(root, text="I agree", bg="white",width=8, height=3, command=on_button_click)
button.place(relx=0.5, rely=0.9, anchor='center')

root.mainloop()