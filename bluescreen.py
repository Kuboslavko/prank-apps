import tkinter as tk

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("Error Message")
root.geometry("800x600")
root.configure(bg='blue')



label1 = tk.Label(root, text=":(", fg='white')
label1 = tk.Label(root, text=":(", font=("Segoe UI", 95), bg='blue',fg="white")
label1.place(x=80, y=50)

label2 = tk.Label(root, text="Your PC run into a problem, and needs to restart. Were just collecting some error info", font=("Arial", 20), bg='blue',fg="white")
label2.place(x=80, y=400)
label2 = tk.Label(root, text="0% complete", font=("Segoe UI", 20), bg='blue',fg="white")
label2.place(x=80, y=500)

root.mainloop()


#obr = Image.open('qrcode.png')
#obr1 = Image.open('qrcode.png')
#obr2 = Image.open('qrcode.png')
#obr1.save('qrcode.png')

#upgrade (stare treba vymazat)

#img = Image.open("qrcode.png")
#img = img.resize((250, 250), Image.Resampling.NEAREST)

#obr = ImageTk.PhotoImage(img)

#tk.Label(root, image=obr).place(x=80,y=700)

#root.mainloop()





