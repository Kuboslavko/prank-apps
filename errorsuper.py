import tkinter as tk
import ctypes

def run_script(event):
    MB_OK = 0x0
    MB_ICONERROR = 0x10

    message = "hahaha mas smolu :)"
    title = "Error"  

    def show_error_box():
        ctypes.windll.user32.MessageBoxW(0, message, title, MB_OK | MB_ICONERROR)
        hwnd = ctypes.windll.user32.FindWindowW(None, title)
        if hwnd:
            ctypes.windll.user32.SetForegroundWindow(hwnd)

    for _ in range(1):
        show_error_box()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("invisible")
root.geometry("800x600")
root.attributes('-alpha', 0.01)  

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

canvas.bind("<Button>", run_script)

root.mainloop()
