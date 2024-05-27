import tkinter as tk

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("Error Message")
root.geometry("800x600")
root.configure(bg='blue')



label1 = tk.Label(root, text=":(", fg='white')
label1 = tk.Label(root, text=":(", font=("Arial", 95), bg='blue')
label1.place(x=80, y=50)

label2 = tk.Label(root, text="Your PC run into a problem, and needs to restart. Were just collecting some error info", font=("Arial", 20), bg='blue')
label2.place(x=80, y=400)
label2 = tk.Label(root, text="0% complete", font=("Arial", 20), bg='blue')
label2.place(x=80, y=500)

root.mainloop()

transformation = tkinter.PhotoImage(file='D:\jakub pc hecker\Jakub\qrcode.png')
tk.Canvas.create_image(x=80, y=600, image=transformation)
import tkinter

canvas = tkinter.Canvas()
canvas.pack()

obr = tkinter.PhotoImage(file='D:\jakub pc hecker\Jakub\qrcode.png')
for x in range(80,):
    canvas.create_image(x, 150, image=obr)

tkinter.mainloop()




