from clases import *
from typing import List
import copy

class Tulipan(Figura):
     def __init__(self,x,y,w,h):
        super().__init__()
        self.shapeList : List[ItemShape] = []
       
        self.posicion.coordX = x
        self.posicion.coordY = y
        self.dimension.base = w
        self.dimension.altura= h
        #-------------------------------------------------------
        self.mainBase = Rectangulo()
        self.mainBase1 = Rectangulo()
        self.mainBase2 = Rectangulo()
        self.mainBase3 = Rectangulo()
        self.mainBase4 = Rectangulo()
        self.mainBase5 = Rectangulo()
        self.mainBase6 = Rectangulo()
        self.mainBase7 = Rectangulo()
        self.mainBase8 = Rectangulo()
        self.mainBase9 = Rectangulo()
        self.mainBase10 = Rectangulo()
        self.mainBase11 = Rectangulo()
        self.mainBase12 = Rectangulo()
        self.mainBase13 = Rectangulo()
        self.mainBase14 = Rectangulo()
        self.mainBase15 = Rectangulo()
        self.mainBase16 = Rectangulo()
        self.mainBase17 = Rectangulo()
        self.mainBase18 = Rectangulo()
        self.mainBase19 = Rectangulo()
        self.mainBase20 = Rectangulo()
        self.mainBase21 = Rectangulo()
        self.mainBase22 = Rectangulo()
        self.mainBase23 = Rectangulo()
        self.mainBase24 = Rectangulo()
        self.mainBase25 = Rectangulo()
        self.mainBase26 = Rectangulo()
        self.mainBase27 = Rectangulo()
        self.mainBase28 = Rectangulo()
        self.mainBase29 = Rectangulo()
        
        self.mainBase30 = Rectangulo()

        #-------------------------------------------------------

        self.mainBase.posicion = Posicion(0,0)
        self.mainBase.dimension = Dimension(w,h)
        self.mainBase.color = (101, 195, 235)
        
        self.mainBase1.posicion = Posicion(0,60)
        self.mainBase1.dimension = Dimension(w,h)
        self.mainBase1.color = (101, 195, 235)
        
        self.mainBase2.posicion = Posicion(0,120)
        self.mainBase2.dimension = Dimension(w,h)
        self.mainBase2.color = (101, 195, 235)
        
        self.mainBase3.posicion = Posicion(0,180)
        self.mainBase3.dimension = Dimension(w,h)
        self.mainBase3.color = (101, 195, 235)
        
        self.mainBase4.posicion = Posicion(60,60)
        self.mainBase4.dimension = Dimension(w,h)
        self.mainBase4.color = (101, 195, 235)
        
        self.mainBase5.posicion = Posicion(60,120)
        self.mainBase5.dimension = Dimension(w,h)
        self.mainBase5.color = (101, 195, 235)
        
        self.mainBase6.posicion = Posicion(60,180)
        self.mainBase6.dimension = Dimension(w,h)
        self.mainBase6.color = (101, 195, 235)
        
        self.mainBase7.posicion = Posicion(60,240)
        self.mainBase7.dimension = Dimension(w,h)
        self.mainBase7.color = (101, 195, 235)
        #
        self.mainBase8.posicion = Posicion(120,180)
        self.mainBase8.dimension = Dimension(w,h)
        self.mainBase8.color = (23, 122, 163)
        
        self.mainBase9.posicion = Posicion(120,240)
        self.mainBase9.dimension = Dimension(w,h)
        self.mainBase9.color = (23, 122, 163)
        
        self.mainBase10.posicion = Posicion(120,120)
        self.mainBase10.dimension = Dimension(w,h)
        self.mainBase10.color = (23, 122, 163)
        
        self.mainBase11.posicion = Posicion(120,60)
        self.mainBase11.dimension = Dimension(w,h)
        self.mainBase11.color = (23, 122, 163)
        
        self.mainBase12.posicion = Posicion(120,0)
        self.mainBase12.dimension = Dimension(w,h)
        self.mainBase12.color = (101, 195, 235)
        
        self.mainBase13.posicion = Posicion(180,60)
        self.mainBase13.dimension = Dimension(w,h)
        self.mainBase13.color = (101, 195, 235)
        
        self.mainBase14.posicion = Posicion(180,120)
        self.mainBase14.dimension = Dimension(w,h)
        self.mainBase14.color = (101, 195, 235)
        
        self.mainBase15.posicion = Posicion(180,180)
        self.mainBase15.dimension = Dimension(w,h)
        self.mainBase15.color = (101, 195, 235)
        
        self.mainBase16.posicion = Posicion(180,240)
        self.mainBase16.dimension = Dimension(w,h)
        self.mainBase16.color = (101, 195, 235)
        
        self.mainBase17.posicion = Posicion(240,0)
        self.mainBase17.dimension = Dimension(w,h)
        self.mainBase17.color = (101, 195, 235)
        
        self.mainBase18.posicion = Posicion(240,60)
        self.mainBase18.dimension = Dimension(w,h)
        self.mainBase18.color = (101, 195, 235)
        
        self.mainBase19.posicion = Posicion(240,120)
        self.mainBase19.dimension = Dimension(w,h)
        self.mainBase19.color = (101, 195, 235)
        
        self.mainBase20.posicion = Posicion(240,180)
        self.mainBase20.dimension = Dimension(w,h)
        self.mainBase20.color = (101, 195, 235)
        
        #tallo
        self.mainBase21.posicion = Posicion(120,300)
        self.mainBase21.dimension = Dimension(w,h)
        self.mainBase21.color = (27, 102, 48)
        
        self.mainBase22.posicion = Posicion(120,360)
        self.mainBase22.dimension = Dimension(w,h)
        self.mainBase22.color = (27, 102, 48)
        
        self.mainBase23.posicion = Posicion(120,420)
        self.mainBase23.dimension = Dimension(w,h)
        self.mainBase23.color = (27, 102, 48)
        
        self.mainBase24.posicion = Posicion(120,480)
        self.mainBase24.dimension = Dimension(w,h)
        self.mainBase24.color = (27, 102, 48)
        
        self.mainBase25.posicion = Posicion(120,540)
        self.mainBase25.dimension = Dimension(w,h)
        self.mainBase25.color = (27, 102, 48)
        
        self.mainBase26.posicion = Posicion(180,480)
        self.mainBase26.dimension = Dimension(w,h)
        self.mainBase26.color = (27, 102, 48)
        
        self.mainBase27.posicion = Posicion(60,480)
        self.mainBase27.dimension = Dimension(w,h)
        self.mainBase27.color = (27, 102, 48)

        self.mainBase28.posicion = Posicion(0,420)
        self.mainBase28.dimension = Dimension(w,h)
        self.mainBase28.color = (27, 102, 48)
        
        self.mainBase29.posicion = Posicion(240,420)
        self.mainBase29.dimension = Dimension(w,h)
        self.mainBase29.color = (27, 102, 48)
            
        
        
       #-------------------------------------------------------
        self.shapeList.append(ItemShape(shape=self.mainBase, name = "main_base"))
       
        self.shapeList.append(ItemShape(shape=self.mainBase1, name = "main_base"))
    
        self.shapeList.append(ItemShape(shape=self.mainBase2, name = "main_base"))
       
        self.shapeList.append(ItemShape(shape=self.mainBase3, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase4, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase5, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase6, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase7, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase8, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase9, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase10, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase11, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase12, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase13, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase14, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase15, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase16, name = "main_base"))

        self.shapeList.append(ItemShape(shape=self.mainBase17, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase18, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase19, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase20, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase21, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase22, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase23, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase24, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase25, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase26, name = "main_base"))

        self.shapeList.append(ItemShape(shape=self.mainBase27, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase28, name = "main_base"))
        
        self.shapeList.append(ItemShape(shape=self.mainBase29, name = "main_base"))
        

        
     def dibujar(self, x=None, y=None):
        for elementoFigura in self.shapeList:
            elementoFigura.shape.dibujar(offsetX=self.posicion.coordX,offsetY=self.posicion.coordY)
            
     def dibujarContorno(self):
        stroke("blue")
        stroke_weight(2)
        no_fill()
        x = self.posicion.coordX
        y = self.posicion.coordY
        w = self.dimension.base
        h = self.dimension.altura
        rect(x,y,w,h)
        
    
        
    