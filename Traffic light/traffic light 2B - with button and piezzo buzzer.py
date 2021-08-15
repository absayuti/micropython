# LAMPU ISYARAT dan BUTANG Lintasan
# Feb 2021

import machine
import utime
import _thread

# Takrif RED, YELLOW & GREEN LEDs sbg OUTPUT
led_red    = machine.Pin(15, machine.Pin.OUT)  # Merah  = GPIO 15 (pin 20)
led_yellow = machine.Pin(14, machine.Pin.OUT)  # Kuning = GPIO 14 (pin 19)
led_green  = machine.Pin(13, machine.Pin.OUT)  # Hijau  = GPIO 13 (pin 17)

# Takrif BUZZER sebagai OUTPUT di GPIO 12 (pin 16)
buzzer = machine.PWM(machine.Pin(12))

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
            buzzer.freq(2000)
            buzzer.duty_u16(32000)
            utime.sleep(0.2)
            buzzer.duty_u16(0)
        utime.sleep(0.01)

# Arahan berikut ini memulakan thread "BUTANG" di atas
_thread.start_new_thread(button_reader_thread, ())

##### Main program starts here #####
led_red.value(0)
led_yellow.value(0)
led_green.value(0)

buzzer.freq(3000)
for i in range(2):
    buzzer.duty_u16(32000)
    utime.sleep(0.2)
    buzzer.duty_u16(0)
    utime.sleep(0.2)

##### Gelung utama #####
while True:
    
    if button_pressed == True:  ##### Jika BUTANG ditekan #####
        led_red.value(1)        # Nyalakan MERAH
        for i in range(10):     # Ulang 10 kali
            print("BUZZ")
            buzzer.freq(1000)
            buzzer.duty_u16(32000) # ...Bunyikan buzzer
            utime.sleep(0.2)      
            buzzer.duty_u16(0)     # ...Padam buzzer
            utime.sleep(0.2)
        global button_pressed   # Apabila selesai...
        button_pressed = False  # Reset status BUTANG         

                                ##### Rutin lazim.... #####
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
    
    ##### Ulang #####
