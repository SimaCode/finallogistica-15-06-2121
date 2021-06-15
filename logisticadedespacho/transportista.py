from despacho import *

class Transportista:
    
    def __init__(self,nombre, clave, tipoTrans, cantidadDespachos):
        self.nombre = nombre
        self.clave = clave
        self.tipoTrans = tipoTrans
        self.cantidadDespachos = cantidadDespachos
        self.despachos = []
        
    def setNombre(self, nombre):
        self.nombre = nombre

    def setClave(self, clave):
        self.clave = clave

    def setTipoTrans(self, tipoTrans):
        self.tipo = tipoTrans
    
    def setCantidadDespachos(self,cantidadDespachos):
        self.cantidadDespachos = cantidadDespachos

    def setDespachos(self,despachos):
        self.despachos = despachos

    def getNombre(self):
        return self.nombre

    def getClave(self):
        return self.clave    

    def getTipoTrans(self):
        return self.tipoTrans    

    def getCantidadDespachos(self):
        return self.cantidadDespachos

    def getDespachos(self):
        return self.despachos

    def addDespacho(self,despacho):
        self.despachos.append(despacho)

    def __str__(self):
        return self.tipo