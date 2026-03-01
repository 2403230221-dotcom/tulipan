from p5 import *
from tulipan import Tulipan


tulipan:Tulipan


def setup():
    global tulipan
    size(800,800)
    tulipan = Tulipan(50,50,60,60)
   
def draw():
    global tulipan
    tulipan.dibujar()
    background(135, 221, 255)



run()