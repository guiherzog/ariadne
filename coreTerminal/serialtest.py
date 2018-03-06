import serial
import os

ser = serial.Serial('/dev/ttyACM0',9600)
while True:
    read_serial=ser.readline().decode().strip('\r\n')
    # print(read_serial)
    # This will start the camera, take a picture and send to AWS Rekognition
    if (read_serial == 'FT_1'):
        os.system('mpg123 -q audio/main.mp3')
        print('Playing Main audio')
    # This will be a static audio, maybe to be used by the orientation system
    if (read_serial == 'FT_2'):
        print('Playing Exit audio')
    # This will generate a static text to give instructions about the room of a user
    if (read_serial == 'FT_3'):
        print('Playing MyRoom audio')
    # This will be a static audio, telling where the user is (the terminal location).
    if (read_serial == 'FT_4'):
        print('Playing Location audio')
    # This will wait for a voice command where the user will choose a place to go.    
    if (read_serial == 'FT_5'):
        print('Playing Search audio')
    # This will ask for the DB about the schedule of a user and play it using a text-to-speech plugin.
    if (read_serial == 'FT_6'):
        print('Playing Schedule audio')
    # This will alert a web-socket in the emergency room telling the name of the patient and showing a picture of him.     
    if (read_serial == 'FT_7'):
        print('Playing SOS audio')
