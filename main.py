# important imports
import pygame
import pygame_gui
import sys
import requests
import random
import pyttsx3

headers = {
    "X-RapidAPI-Key": "",
    "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}
url = "https://imdb8.p.rapidapi.com/auto-complete"

def titlePic(search):
    querystring = {"q": f"{search}"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    index = random.randrange(0, 8)
    print(response.json()['d'][index])
    titleOfMovie = response.json()['d'][index]['l']
    picOfMovie = response.json()['d'][index]['i']['imageUrl']
    widthPic = response.json()['d'][index]['i']['width']
    heightPic = response.json()['d'][index]['i']['width']
    picScale = 400/widthPic
    img_data = requests.get(picOfMovie).content

    return [titleOfMovie,img_data,widthPic,heightPic,picScale]


engine = pyttsx3.init()


# Funny header for get request


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
    yearS=""
    titleOfMovie = ""
    picOfMovie = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/HD_transparent_picture.png/120px-HD_transparent_picture.png"
    img = pygame.image.load("image_name.jpg").convert_alpha()
    widthPic = 0
    heightPic = 0
    picScale = 0
    font = pygame.font.SysFont('Calibri', 35)

    engine.say("Welcome to the time machine.")
    engine.runAndWait()

    while True:
        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                    event.ui_object_id == '#main_text_entry'):
                if (event.text.isnumeric()):
                    if (int(event.text) >= 1913 and int(event.text) <= 2022):

                        yearS=f'{event.text}'

                        infoOfMovie=titlePic(yearS)
                        titleOfMovie,img_data,widthPic,heightPic,picScale=infoOfMovie
                        # titleOfMovie=infoOfMovie[0]
                        # img_data=infoOfMovie[1]
                        # widthPic=infoOfMovie[2]
                        # heightPic=infoOfMovie[3]
                        # picScale=infoOfMovie[4]

                        enterNow = True

                        with open('image_name.jpg', 'wb') as handler:
                            handler.write(img_data)

                        try:
                            img = pygame.image.load("image_name.jpg").convert_alpha()
                        except:
                            print("Bad error handling1")
                        try:
                            img = pygame.image.load("image_name.jpg").convert()
                        except:
                            print("Bad error handling2")
                        try:
                            img = pygame.image.load("image_name.jpg")
                        except:
                            print("Bad error handling3")

                    else:
                        print("number er ikke i mellem årstallene")
                else:
                    print("Pls give a number")

            manager.process_events(event)

        manager.update(UI_REFRESH_RATE)

        SCREEN.fill((99, 107, 120))

        manager.draw_ui(SCREEN)

        img = pygame.transform.scale(
            img, (widthPic * picScale * (2/3), heightPic * picScale))
        SCREEN.blit(img, (1100, 200))
        text = font.render(titleOfMovie, True, (0, 0, 0))
        SCREEN.blit(text, (1100, 160))

        pygame.display.update()

        if (enterNow == True):
            engine.say("Welcome to " + yearS + ". In this year " + titleOfMovie + " came out.")
            engine.runAndWait()

        enterNow = False


main()
