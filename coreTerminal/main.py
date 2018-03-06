import serial
import os

ser = serial.Serial('/dev/ttyACM0',9600)
while True:
    read_serial=ser.readline().decode().strip('\r\n')
    # print(read_serial)
    # This will start the camera, take a picture and send to AWS Rekognition
    if (read_serial == 'FT_1'):
        print('Playing Main audio')
        os.system('''pico2wave -w 4.wav "Hello Mark,

            In this terminal you can: Call for Help, Find the exit, Go to your Room, Know where you are, Search for a Place, Hear your Schedule. 

            To find the exit from the building, press the first small button from the left.
            To go to your room, press the second button from the left.
            To know your location, press the third button from the left.
            To search for a particular place, press the fourth button from the left.
            To hear your schedule, press the fifth button from the left.
            To call for help, press the sixth button from the left." && aplay 4.wav''')
        
    # This will be a static audio, maybe to be used by the orientation system
    if (read_serial == 'FT_2'):
        print('Playing Exit audio')
        os.system('''pico2wave -w 4.wav "You pressed the button “Find exit”

            If you want to leave the building, please use a lift located on your right.
            The exit is on the ground floor.
            To find out more instructions, please use the main terminal on the ground floor, which you can find again when leaving the elevator on your right hand.
" && aplay 4.wav''')
    # This will generate a static text to give instructions about the room of a user
    if (read_serial == 'FT_3'):
        print('Playing MyRoom audio')
    # This will be a static audio, telling where the user is (the terminal location).
    if (read_serial == 'FT_4'):
        print('Playing Location audio')
        os.system('''pico2wave -w 4.wav "You pressed the button What is my location:
                  
                  You are at the Gastrolab in the fourth floor of Building E.

                  On this floor, there is located a part of Department of computer graphics and interaction." && aplay 4.wav''')

    # This will wait for a voice command where the user will choose a place to go.    
    if (read_serial == 'FT_5'):
        print('Playing Search audio')
        os.system('''pico2wave -w 4.wav "You pressed the button “Search for a particular place”

            Please pronounce carefully the name of the place that you want to search for. 

            This feature is not implemented yet." && aplay 4.wav''')
    # This will ask for the DB about the schedule of a user and play it using a text-to-speech plugin.
    if (read_serial == 'FT_6'):
        print('Playing Schedule audio')
        os.system('''pico2wave -w 4.wav "You pressed the button 'Hear Schedule'.

It's 10:10 and your activities for today are:

At 12:00 - Lunch with Liza.

At 16:00 - Dancing Class.

At 18:00 - Listen to Audiobook 'The Foundation'.

At 19:00 - Take your daily pills." && aplay 4.wav''')
    # This will alert a web-socket in the emergency room telling the name of the patient and showing a picture of him.     
    if (read_serial == 'FT_7'):
        print('Playing SOS audio')
        os.system('''pico2wave -w 4.wav "You pressed the button “Call for help”. 

Your assigned Nurse "Elisabeth" has been alerted that you are at the Gastrolab and it's needing help. 

Please do not move and wait for her to arrive." && aplay 4.wav''')
