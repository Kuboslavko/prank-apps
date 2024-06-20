import ctypes
import time

MB_OK = 0x0
MB_ICONERROR = 0x10

message = "hahaha mas smolu :)"
title = "Error"

def show_error_box():
    ctypes.windll.user32.MessageBoxW(0, message, title, MB_OK | MB_ICONERROR)

for _ in range(5):
    show_error_box()
    time.sleep(0.5)  

print("5 error windows have been shown.")

#dalsia moznost textu An unexpected error has occurred.
