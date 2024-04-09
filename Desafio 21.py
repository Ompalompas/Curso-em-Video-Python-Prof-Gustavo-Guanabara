##Desafio 21
#Dica: Buscar aprender os principais módulos de python
from pygame import mixer,event
mixer.init()
mixer.music.load('som1.mp3')
mixer.music.play()
input()
event.wait()