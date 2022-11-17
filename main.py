#important imports
import pygame
import pygame_gui
import sys
import requests

<<<<<<< Updated upstream
backgroundColor = (99, 107, 107)

=======
#Funny header for get request
>>>>>>> Stashed changes
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

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
                print(event.text)
                url = f'https://en.wikipedia.org/wiki/{event.text}_in_film'
                r = requests.get(url, headers=headers)
                rankTextPos= r.content.decode().find(">Rank<")
                rankTitlePos= r.content.decode()[rankTextPos:rankTextPos+250].find("title=")
                titleOfFilm = r.content.decode()[rankTextPos+rankTitlePos+6:rankTextPos+rankTitlePos+200].split('"')[1]
                print(titleOfFilm)
                

            manager.process_events(event)
        
        manager.update(UI_REFRESH_RATE)

        SCREEN.fill(backgroundColor)

        manager.draw_ui(SCREEN)

        text = font.render(titleOfFilm, True,(0,0,0))
        SCREEN.blit(text,(50,50))

        pygame.display.update()
    

main()