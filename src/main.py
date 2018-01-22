# Imports
import pygame
import RPi.GPIO as GPIO
import time

# Setup
pygame.mixer.init()
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button to GPIO23

# Main
try:
    while True:
         button_state = GPIO.input(23)
         if button_state == False:
            pygame.mixer.music.load("test.mp3")
            pygame.mixer.music.play()
            print('Audio Started...')
            while pygame.mixer.music.get_busy() == True:
                continue
            time.sleep(0.2)
            print('Audio stopped...')
except:
    GPIO.cleanup()

