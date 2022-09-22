# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 14:42:31 2022

@author: alumno
"""
# from modulos.LDE import ListaDobleEnlazada
# class ColaDoble:
#     def __init__(self):
#         self.items = ListaDobleEnlazada()

#     def estaVacia(self):
#         return self.items.estaVacia()

#     def agregarFrente(self, item):
#         self.items.agregar(item)

#     def agregarFinal(self, item): 
#         self.items.anexar(item)

#     def removerFrente(self):
#         return self.items.extraer(0)

#     def removerFinal(self):
#         return self.items.extraer()

#     def tamano(self):
#         return self.items.tamanio
    
#     def mostrarFrente(self):
#         return self.items.cabeza
    
    
#     def mostrarFinal(self):
#         return self.items.cola

class ColaDoble:
    def __init__(self):
        self.items = []


    def agregarFrente(self, item):
        self.items.append(item)

    def agregarFinal(self, item):
        self.items.insert(0,item)

    def removerFrente(self):
        return self.items.pop()

    def removerFinal(self):   # es necesario remover final y devolver final? 
        return self.items.pop(0)

    def tamano(self):
        return len(self.items)
    
    def devolverFrente(self):
        return self.items[-1]
    
    def devolverFinal(self):
        return self.items[0]
    
    def mezclar(self):
        import random as rd
        rd.shuffle(self.items)
    
    