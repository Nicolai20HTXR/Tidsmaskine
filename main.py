# important imports
import pygame
import pygame_gui
import sys
import requests
import random
import pyttsx3
from main_copy import *

engine = pyttsx3.init()


#Replace old image with transparent
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/HD_transparent_picture.png/120px-HD_transparent_picture.png"
img_data = requests.get(image_url).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)

# Initialize pygame
pygame.init()

# Declare various variables
WIDTH, HEIGHT = 1500, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Input in PyGame Year movie gross")

manager = pygame_gui.UIManager((WIDTH, HEIGHT))

text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 75), (900, 50)), manager=manager,
                                                 object_id='#main_text_entry')

clock = pygame.time.Clock()


def main():
    enterNow = False
    #Replaces old image to transparent/nothing
    img = pygame.image.load("image_name.jpg").convert_alpha()
    font = pygame.font.SysFont('Calibri', 35)
    yearS=""
    titleOfMovie = ""
    widthPic = 0
    heightPic = 0
    picScale = 0

    engine.say("Welcome to the time machine.")
    engine.runAndWait()

    while True:
        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            #If pygame quit, quit running
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #When enter is pressed in the UI text box rectangle
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                    event.ui_object_id == '#main_text_entry'):

                #Checks if input in UI rectangle is a number and within 1913 to 2022
                if (event.text.isnumeric()):
                    if (int(event.text) >= 1913 and int(event.text) <= 2022):

                        #Variable for what year is searched for
                        yearS=f'{event.text}'
                        #Gives variable to function titlePic which return [titleOfMovie,img_data,widthPic,heightPic,picScale]
                        infoOfMovie=titlePic(yearS)

                        #Unwraps the variables
                        titleOfMovie,img_data,widthPic,heightPic,picScale=infoOfMovie
                        # titleOfMovie=infoOfMovie[0]
                        # img_data=infoOfMovie[1]
                        # widthPic=infoOfMovie[2]
                        # heightPic=infoOfMovie[3]
                        # picScale=infoOfMovie[4]

                        #Convert img data to file on pc
                        img = convertImgToPyG(img_data,'image_name.jpg')
                        #Enter is pressed
                        enterNow = True

                    else:
                        print("number er ikke i mellem årstallene")
                else:
                    print("Pls give a number")

            manager.process_events(event)

        #WhileTrue:
        #Updates from refreshrate
        manager.update(UI_REFRESH_RATE)
        #Background color
        SCREEN.fill((99, 107, 120))
        #Movie name and picture placement
        moviePlacement(SCREEN,titleOfMovie,font,img,widthPic,heightPic,picScale)
        #Draws ui on screen
        manager.draw_ui(SCREEN)
        #Display update
        pygame.display.update()

        #Press enter plays text
        if (enterNow == True):
            engine.say("Welcome to " + yearS + ". In this year " + titleOfMovie + " came out.")
            engine.runAndWait()
        #Enter not pressed
        enterNow = False


main()
