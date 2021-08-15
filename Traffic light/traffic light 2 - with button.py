"""
--------------------------------------------------------------------------------
LAMPU ISYARAT dan BUTANG Lintasan
Perkakasan: Raspberry Pico Pi, Buzzer, LED (x3), Resistor (220 Ohm x3),
            Push button switch, jumper wires.
Perisian:   Thonny

AB Sayuti HM Saman, Feb 2021
--------------------------------------------------------------------------------
"""

import machine
import utime
import _thread

# Takrif RED, YELLOW & GREEN LEDs sbg OUTPUT
led_red    = machine.Pin(15, machine.Pin.OUT)  # Merah  = GPIO 15 (pin 20)
led_yellow = machine.Pin(14, machine.Pin.OUT)  # Kuning = GPIO 14 (pin 19)
led_green  = machine.Pin(13, machine.Pin.OUT)  # Hijau  = GPIO 13 (pin 17)

# Takrif BUZZER sebagai OUTPUT di GPIO 12 (pin 16)
buzzer = machine.Pin(12, machine.Pin.OUT)

# Takrif suis BUTANG sebagai INPUT dgn perintang PULL DOWN
# GPIO 16 (pin 21)
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Status butang disimpan dalam pemblehubah global berikut
global button_pressed
button_pressed = False

# Thread utk membaca/mengesan BUTANG dan set pembolehubah berkenaan
def button_reader_thread():
    global button_pressed
    while True:
        if button.value() == 1:
            button_pressed = True
            buzzer.value(1)
            utime.sleep(0.2)
            buzzer.value(0)
        utime.sleep(0.01)

# Arahan berikut ini memulakan thread "BUTANG" di atas
_thread.start_new_thread(button_reader_thread, ())

""" Main program starts here """
led_red.value(0)             # Reset/padam semua warna
led_yellow.value(0)
led_green.value(0)

for i in range(4):           # Beep 2 kali utk menandakan permulaan prgm
    buzzer.toggle()
    utime.sleep(0.2)

""" Gelung utama """
while True:
    
    if button_pressed == True:  #### Jika BUTANG ditekan
        led_red.value(1)        # Nyalakan MERAH
        for i in range(20):     # Bunyikan buzzer berulang-kali
            buzzer.toggle()     
            utime.sleep(0.2)      
        global button_pressed   # Apabila selesai...
        button_pressed = False  # Reset status BUTANG         

                                #### Rutin lazim....
    led_red.value(1)            # Merah nyala
    utime.sleep(5)              # selama 5 saat  
    led_yellow.value(1)         # Kuning nyala sama
    utime.sleep(2)              # 2 saat
    led_red.value(0)            # Padam merah
    led_yellow.value(0)         # Padam kuning
    led_green.value(1)          # Hijau nyala
    utime.sleep(5)              # Selama 5 saat
    led_green.value(0)          # Padam hijau
    led_yellow.value(1)         # Kuning nyala
    utime.sleep(5)              # 5 saat
    led_yellow.value(0)         # Padam kuning
