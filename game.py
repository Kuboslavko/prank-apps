import ctypes
import time

MB_OK = 0x0
MB_ICONERROR = 0x10

message = "Naozaj chcete spustiť tento súbor"
title = "Error"

def show_error_box():
    ctypes.windll.user32.MessageBoxW(0, message, title, MB_OK | MB_ICONERROR)

for _ in range(1):
    show_error_box()



MB_OK = 0x0
MB_ICONERROR = 0x30

message = "Tento súbor vám môže poškodiť váš počítač, naozaj chcete spustiť tento súbor ! "
title = "Error"

def show_error_box():
    ctypes.windll.user32.MessageBoxW(0, message, title, MB_OK | MB_ICONERROR)

for _ in range(1):
    show_error_box()



MB_OK = 0x0
MB_ICONERROR = 0x10

message = "Varovanie: Tento súbor môže obsahovať škodlivý kód. Odporúčame ho neotvárať."
title = "Windows defender"

def show_error_box():
    ctypes.windll.user32.MessageBoxW(0, message, title, MB_OK | MB_ICONERROR)

for _ in range(1):
    show_error_box()


import ctypes

MB_OK = 0x0
MB_ICONERROR = 0x30  

message = "Súbor bol označený ako potenciálne škodlivý. Odporúčame ho preskúmať pred jeho spustením."
title = "Windows firewall "

def show_error_box():
    ctypes.windll.user32.MessageBoxW(0, message, title, MB_OK | MB_ICONERROR)

for _ in range(1):
    show_error_box()



MB_OK = 0x0
MB_ICONERROR = 0x10

message = "Bezpečnostný systém Windows zistil potenciálnu hrozbu v tomto súbore. Odporúčame ho skontrolovať antivírusovým programom."
title = "Windows defender"

def show_error_box():
    ctypes.windll.user32.MessageBoxW(0, message, title, MB_OK | MB_ICONERROR)

for _ in range(1):
    show_error_box()

MB_OK = 0x0
MB_ICONERROR = 0x10

message = "Bezpečnostný systém Windows zistil nebezpečný obsah v tomto súbore. Odporúčame ho odstrániť."
title = "Windows fire wall"

def show_error_box():
    ctypes.windll.user32.MessageBoxW(0, message, title, MB_OK | MB_ICONERROR)

for _ in range(1):
    show_error_box()



MB_OK = 0x0
MB_ICONERROR = 0x30

message = "Varovanie: Tento súbor môže obsahovať vírus. Otvoriť ho?"
title = "Windows defender"

def show_error_box():
    ctypes.windll.user32.MessageBoxW(0, message, title, MB_OK | MB_ICONERROR)

for _ in range(1):
    show_error_box()

MB_OK = 0x0
MB_ICONERROR = 0x10

message = "Bezpečnostný systém Windows zablokoval prístup k tomuto súboru. Dôvod: možný škodlivý obsah"
title = "Windows defender"

def show_error_box():
    ctypes.windll.user32.MessageBoxW(0, message, title, MB_OK | MB_ICONERROR)

for _ in range(1):
    show_error_box()




