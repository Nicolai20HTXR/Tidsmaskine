#important imports
import pygame
import pygame_gui
import sys
import requests
import urllib.parse


#Funny header for get request
headers = {'content-type': '*/*', 'Accept-Charset': 'UTF-8'}

image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/HD_transparent_picture.png/120px-HD_transparent_picture.png"
img_data = requests.get(image_url).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)

#Initialize pygame
pygame.init()

#Declare various variables
WIDTH, HEIGHT = 1500, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Input in PyGame Year movie gross")

manager = pygame_gui.UIManager((WIDTH, HEIGHT))

text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 275), (900, 50)), manager=manager,
                                               object_id='#main_text_entry')

clock = pygame.time.Clock()



def main():
    titleOfFilm=""
    font = pygame.font.SysFont('Calibri', 35)
    while True:
        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                if(event.text.isnumeric()):
                    if(int(event.text)>=1913 and int(event.text)<=2022):
                        # print(event.text)
                        url = f'https://en.wikipedia.org/wiki/{event.text}_in_film'
                        r = requests.get(url, headers=headers)
                        rText= r.content.decode()
                        rankTextPos= rText.find(">Rank<")
                        rankTitlePos= rText[rankTextPos:rankTextPos+250].find("title=")
                        rankLinkPos= rText[rankTextPos:rankTextPos+250].find("href=")
                        titleOfFilm = rText[rankTextPos+rankTitlePos+6:rankTextPos+rankTitlePos+200].split('"')[1]
                        linkToPage = rText[rankTextPos+rankLinkPos+6:rankTextPos+rankLinkPos+200].split('"')[0]
                        # print(rText[rankTextPos+rankLinkPos+6:rankTextPos+rankLinkPos+200].split('"')[0])
                        url2 = f'https://en.wikipedia.org{linkToPage}'
                        print(urllib.parse.unquote(linkToPage))
                        r2 = requests.get(url2, headers=headers)
                        rText2= r2.content.decode()
                        imageLinkPos = rText2.find('"og:image"')
                        linkToImage = rText2[imageLinkPos+20:imageLinkPos+15+500].split('"')[0]
                        print(linkToImage)
                        print(titleOfFilm)
                        image_url = linkToImage
                        img_data = requests.get(image_url).content
                        with open('image_name.jpg', 'wb') as handler:
                            handler.write(img_data)
                    else:
                        print("number er ikke i mellem årstallene")
                else: 
                    print("Pls give a number")
                

            manager.process_events(event)
        
        manager.update(UI_REFRESH_RATE)

        SCREEN.fill((99, 107, 120))

        manager.draw_ui(SCREEN)

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

        SCREEN.blit(img, (100,300))
        text = font.render(titleOfFilm, True,(0,0,0))
        SCREEN.blit(text,(50,50))


        pygame.display.update()
    

main()