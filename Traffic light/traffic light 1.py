# LAMPU ISYARAT
# Feb 2021

import machine
import utime

# Takrif RED, YELLOW & GREEN LEDs sbg OUTPUTs
led_red    = machine.Pin(15, machine.Pin.OUT)  # Merah  = GPIO 15 (pin 20)
led_yellow = machine.Pin(14, machine.Pin.OUT)  # Kuning = GPIO 14 (pin 19)
led_green  = machine.Pin(13, machine.Pin.OUT)  # Hijau  = GPIO 13 (pin 17)

# Gelung utama
while True:
    led_red.value(1)       # Merah nyala
    utime.sleep(5)         # selama 5 saat  
    led_yellow.value(1)    # Kuning nyala sama
    utime.sleep(2)         # 2 saat
    led_red.value(0)       # Padam merah
    led_yellow.value(0)    # Padam kuning
    led_green.value(1)     # Hijau nyala
    utime.sleep(5)         # Selama 5 saat
    led_green.value(0)     # Padam hijau
    led_yellow.value(1)    # Kuning nyala
    utime.sleep(5)         # 5 saat
    led_yellow.value(0)    # Padam kuning
                           # Ulang
