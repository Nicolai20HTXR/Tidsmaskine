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

def moviePlacement(SCREEN,titleOfMovie,font,img,widthPic,heightPic,picScale):
    img = pygame.transform.scale(
        img, (widthPic * picScale * (2/3), heightPic * picScale))
    SCREEN.blit(img, (1100, 200))
    text = font.render(titleOfMovie, True, (0, 0, 0))
    SCREEN.blit(text, (1100, 160))

def convertImgToPyG(img_data,nameOfFile):
    with open('image_name.jpg', 'wb') as handler:
        handler.write(img_data)

    try:
        img = pygame.image.load(nameOfFile).convert_alpha()
    except:
        print("Bad error handling1")
    try:
        img = pygame.image.load(nameOfFile).convert()
    except:
        print("Bad error handling2")
    try:
        img = pygame.image.load(nameOfFile)
    except:
        print("Bad error handling3")
    return img