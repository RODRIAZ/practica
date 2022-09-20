# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 20:12:56 2022

@author: rodro
"""

class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None
        self.anterior = None
    
    @property
    def dato(self):
        return self._dato
    
    @dato.setter
    def dato(self, valor):
        self._dato = valor

    @property    
    def siguiente(self):
        return self._siguiente
    
    @siguiente.setter
    def siguiente(self, valor):
        self._siguiente = valor
    
    @property
    def anterior(self):
        return self._anterior
    
    @anterior.setter
    def anterior(self, valor):
        self._anterior = valor
        
"""+-++-+-+-+-+-+-++-+--+-+-+-++-"""        

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self._tamanio = 0
    
    @property
    def cabeza(self):
        return self._cabeza
    
    @cabeza.setter
    def cabeza(self, valor):
        self._cabeza = valor
    
    @property
    def cola(self):
        return self._cola
    
    @cola.setter
    def cola(self, valor):
        self._cola = valor
    
    @property
    def tamanio(self):     
         return  self._tamanio

        

    def estaVacia(self): 
      return self.cabeza == None   
 
    

    def agregar(self, item):
        temp = Nodo(item)
        if self.cabeza == None:  
            self.cabeza = temp
            self.cola = temp
        else:  
            temp.siguiente = self.cabeza
            self.cabeza.anterior = temp  
            self.cabeza = temp
        self._tamanio += 1 
    

        
    def anexar(self, item): 
        temp = Nodo(item)
        if self.cabeza == None:  
            self.cabeza = temp
            return
        else:
            apuntador = self.cabeza  
            while apuntador.siguiente != None:  
                apuntador = apuntador.siguiente
            apuntador.siguiente = temp
            temp.anterior = apuntador
            self.cola = temp
        self._tamanio += 1 



    def insertar(self, posicion, item):
        nuevoNodo = Nodo(item)
        if  0 < posicion > self._tamanio:
            raise IndexError
        
        if posicion == 0:
            self.agregar(item)
        
        elif posicion == self.tamanio:
             self.anexar(item)
        
        else:
            temp = self.cabeza
            for nodo in range(posicion-1):  
                temp = temp.siguiente 
            nuevoNodo.anterior = temp     
            nuevoNodo.siguiente = temp.siguiente
            if temp.siguiente != None:
                temp.siguiente.anterior = nuevoNodo
            temp.siguiente = nuevoNodo
    
    
    
    def extraer(self, posicion=-1):
        
        num = None
        if  0 < posicion > self._tamanio:
            raise IndexError
        
        if posicion == self._tamanio or  posicion == -1:
            num = self.cola.dato
            self.cola.anterior.siguiente = None
            self.cola = self.cola.anterior
        
        elif posicion == 0:
            num = self.cabeza.dato
            self.cabeza.siguiente.anterior = None
            self.cabeza =  self.cabeza.siguiente    
            
        else:
            temp = self.cabeza
            for nodo in range(posicion):  
                temp = temp.siguiente
            num =temp.dato
            temp.anterior.siguiente = temp.siguiente
            temp.siguiente.anterior = temp.anterior
        return print(num)
            
     
    
    def copiar(self):
        copia = ListaDobleEnlazada()
        temp = self.cabeza
        for nodo in range(self.tamanio):
            copia.anexar(temp.dato)
            temp = temp.siguiente
        return copia
        
    
    
    def invertir(self):
             if self.cabeza is None:
                 print("la lista esta vacia")
                 return
             p = self.cabeza
             q = p.siguiente
             p.siguiente = None
             p.anterior = q
             
             while q is not None:
                 q.anterior = q.siguiente
                 q.siguiente = p
                 p = q
                 q = p.anterior
             self.cabeza = p
            
    
    
    def concatenar(self, ListaDobleEnlazada):
        if self.cabeza == None:
            return ListaDobleEnlazada
        elif ListaDobleEnlazada.cabeza == None:
            return self
        else:
            self.cola.siguiente = ListaDobleEnlazada.cabeza
            ListaDobleEnlazada.cabeza.anterior = self.cola
            self.cola = ListaDobleEnlazada.cola
            self._tamanio = self._tamanio + ListaDobleEnlazada._tamanio
            return self



    def ordenar(self):
        for i in range(self.tamanio):
            actual=self.cabeza.siguiente
            aux=None
            while actual != None:
                if actual.anterior.dato > actual.dato:
                    aux = actual.anterior.dato
                    actual.anterior.dato = actual.dato
                    actual.dato = aux
                actual = actual.siguiente
        
                
                               
    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()

        return encontrado


        
    def mostrar (self):
        if self.cabeza == None:
            print("lista vacia")
        else:
            apuntador = self.cabeza
            while apuntador != None:
                print(apuntador.dato)
                apuntador = apuntador.siguiente                
                
                
                
    def __iter__(self):
         nodo = self.cabeza
         while nodo :
             yield nodo
             nodo = nodo.siguiente
