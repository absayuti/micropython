"""
--------------------------------------------------------------------------------
LAMPU ISYARAT (x2) dan 2 BUTANG Lintasan
Perkakasan: Raspberry Pico Pi, Buzzer, LED (2 set: merah, kuning, hijau x2 set)
            Resistor (220 Ohm x6), Push button switch (x2), jumper wires.
Perisian:   Thonny

AB Sayuti HM Saman, Feb 2021
--------------------------------------------------------------------------------
"""

import machine
import utime
import _thread

# Takrif RED, YELLOW & GREEN LEDs sbg OUTPUT
led_red     = machine.Pin(15, machine.Pin.OUT)  # Merah  = GPIO 15 (pin 20)
led_yellow  = machine.Pin(14, machine.Pin.OUT)  # Kuning = GPIO 14 (pin 19)
led_green   = machine.Pin(13, machine.Pin.OUT)  # Hijau  = GPIO 13 (pin 17)
led_red2    = machine.Pin(11, machine.Pin.OUT)  # Merah  = GPIO 11 (pin 15)
led_yellow2 = machine.Pin(10, machine.Pin.OUT)  # Kuning = GPIO 10 (pin 14)
led_green2  = machine.Pin(9, machine.Pin.OUT)   # Hijau  = GPIO 9 (pin 12)

# Takrif BUZZER sebagai OUTPUT di GPIO 12 (pin 16), GPIO 8 (pin 11)
buzzer  = machine.Pin(12, machine.Pin.OUT)
buzzer2 = machine.Pin(8, machine.Pin.OUT)

# Takrif suis BUTANG sebagai INPUT dgn perintang PULL DOWN
# GPIO 16 (pin 21), GPIO 17 (pin 22)
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
button2 = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Status butang disimpan dalam pemblehubah global berikut
global button_pressed, button2_pressed
button_pressed = False
button2_pressed = False

# Thread utk membaca/mengesan BUTANG dan set pembolehubah berkenaan
def button_reader_thread():
    global button_pressed, button2_pressed    
    while True:
        if button.value() == 1:
            button_pressed = True
            buzzer.value(1)
            utime.sleep(0.2)
            buzzer.value(0)
        if button2.value() == 1:
            button2_pressed = True
            buzzer2.value(1)
            utime.sleep(0.2)
            buzzer2.value(0)
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
    
    ## Set lampu isyarat + butang #1 ##
    if button_pressed == True:  #### Jika BUTANG ditekan
        led_red.value(1)        # Nyalakan MERAH
        for i in range(20):     # Bunyikan buzzer berulang-kali
            buzzer.toggle()     
            utime.sleep(0.2)      
        global button_pressed   # Apabila selesai...
        button_pressed = False  # Reset status BUTANG         

    ## Set lampu isyarat + butang #2 ##
    if button2_pressed == True:  #### Jika BUTANG ditekan
        led_red2.value(1)        # Nyalakan MERAH
        for i in range(20):      # Bunyikan buzzer berulang-kali
            buzzer2.toggle()     
            utime.sleep(0.2)      
        global button2_pressed   # Apabila selesai...
        button2_pressed = False  # Reset status BUTANG         

                                ### Kitaran warna cara Malaysia
    led_red.value(1)            # Merah #1 nyala
    led_green2.value(0)         # Hijau #2 nyala
    utime.sleep(5)              # selama 5 saat  
    led_green2.value(0)         # Padam hijau #2
    led_yellow2.value(1)        # Kuning #2 nyala
    utime.sleep(2)              # selama 2 saat  
    led_red.value(0)            # Padam merah #1
    led_green.value(1)          # Hijau #1 nyala
    led_yellow2.value(0)        # Padam kuning #2
    led_red2.value(1)           # Merah #2 nyala
    utime.sleep(5)              # Selama 5 saat

    led_yellow.value(1)         # Kuning #1 nyala
    utime.sleep(2)              # 5 saat
    led_yellow.value(0)         # Padam kuning
