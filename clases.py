from p5 import *
from dataclasses import dataclass

#Clases base
class Borde:
    def __init__(self, color=(0,0,0), grosor=2):
        self._color = color
        self._grosor = grosor

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def grosor(self):
        return self._grosor

    @grosor.setter
    def grosor(self, value):
        self._grosor = value
    
    def __str__(self):
        return f"Borde[color = {self.color}, grosor = {self.grosor}]"    

class Posicion:
    def __init__(self, coordX=0, coordY=0):
        self._coordX = coordX
        self._coordY = coordY

    @property
    def coordX(self):
        return self._coordX

    @coordX.setter
    def coordX(self, value):
        self._coordX = value

    @property
    def coordY(self):
        return self._coordY

    @coordY.setter
    def coordY(self, value):
        self._coordY = value
    
    def __str__(self):
        return f"Posicion[x={self.coordX}, y={self.coordY}]"

class Dimension:
    def __init__(self, base=100, altura=100):
        self._base = base
        self._altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        self._base = value

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, value):
        self._altura = value
#Fin de clases base

#Clase padre Figura
class Figura:
    def __init__(self, \
            borde=None, \
            posicion=None, \
            dimension=None, \
            color=(255,255,255),
            speed = None,
            escala = None #nuevo parámetro
            ):
        self._borde = borde if borde is not None else Borde();
        self._posicion = posicion if posicion is not None else Posicion();
        self._dimension = dimension if dimension is not None else Dimension();
        self._color = color;
        self._speed = speed if speed is not None else 5;
        #nueva 
        self._escala = escala if escala is not None else 1;


    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, newSpeed):
        self._speed = newSpeed
        
    @property
    def borde(self):
        return self._borde;

    @borde.setter
    def borde(self, value):
        self._borde = value;

    @property
    def posicion(self):
        return self._posicion;

    @posicion.setter
    def posicion(self, value):
        self._posicion = value

    @property
    def dimension(self):
        return self._dimension;

    @dimension.setter
    def dimension(self, value):
        self._dimension = value;

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value;
        
    @property
    def escala(self):
        return self._escala;
    
    @escala.setter
    def escala(self, newValue):
        self._escala = newValue;    
    
    #Actualización método: Se agregan los parámetros x, y, para saber si tiene dependencias externas
    # def dibujar(self): ejemplos de llamado -> dibujar(), dibujar(x=0,y=0)
    #se crea el método abstract, sin implementación
    def dibujar(self, x=None, y=None, offsetX = None, offsetY= None):
        ...
    
    def moverHorizontal(self, strDireccion="RIGHT"):
        if strDireccion.upper() == "LEFT":
            self.posicion.coordX -= self._speed
        elif strDireccion.upper() == "RIGHT":
            self.posicion.coordX += self._speed
            
    def moverVertical(self, strDireccion="DOWN"):
        if strDireccion.upper() == "DOWN":
            self.posicion.coordY += self._speed
        elif strDireccion.upper() == "UP":
            self.posicion.coordY -= self._speed
    
        
    
#Fin de la clase padre Figura

#Clases de objetos
#Clase Rectangulo
class Rectangulo(Figura):
    def dibujar(self, x=None, y=None, offsetX = None, offsetY= None):
        #define grosor de borde
        grosor = self.borde.grosor
        #define color de borde
        colorBorde=self.borde.color
        #define color de relleno
        colorRelleno = self.color
        #define origen en x
        origenX = x if x is not None else self.posicion.coordX
        #define origen en y
        origenY = y if y is not None else self.posicion.coordY
        
        origenX = (self.posicion.coordX + offsetX) if offsetX is not None else x
        origenY = (self.posicion.coordY + offsetX) if offsetY is not None else y
        
        #define pixeles de la base
        base = self.dimension.base * self._escala #Actualzación
        #define pixeles de la altura
        altura = self.dimension.altura * self._escala #Actualzación
        
        stroke(*colorBorde)
        stroke_weight(grosor)
        fill(*colorRelleno)
        rect(origenX, origenY, base, altura)

    
#Fin de clase Rectangulo    

#Clase Elipse
class Elipse(Figura):
    
    def dibujar(self, x=None, y=None):
        #define grosor de borde
        grosor = self.borde.grosor
        #define color de borde
        colorBorde=self.borde.color
        #define color de relleno
        colorRelleno = self.color
        #define origen en x
        origenX = x if x is not None else self.posicion.coordX
        #define origen en y
        origenY = y if y is not None else self.posicion.coordY
        #define pixeles de la base
        base = self.dimension.base * self.escala
        #define pixeles de la altura
        altura = self.dimension.altura * self.escala
        
        stroke(*colorBorde)
        stroke_weight(grosor)
        fill(*colorRelleno)
        ellipse(origenX, origenY, base, altura)
        
        
#Fin de la clase Elipse
#Se crea la clase ItemShape
@dataclass
class ItemShape():
    shape: Figura;
    name: str;
#fin de la clase ItemShape
#Fin de clases objetos