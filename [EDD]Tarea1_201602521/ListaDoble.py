from NodoDoble import *
import os
class ListaDoble:
    
     #si ya importe la clase aqui entonces ya puedo utilizar sus atributos
    def __init__(self):
        #self.PrimerNodo=NodoDoble()#esto ya no tiene sentido pero por pasados lenguajes de programacion lo dejare
        self.PrimerNodo=None
        self.UltimoNodo=None
        self.contador=0#Sirve para llevar un control del tamano de la lista
        self.contadorGrafica=0#Sirve para poder cambiar de nombre entre documentos e imagenes

    def Insertar_Final(self,valor):
        
        self.NuevoNodo=NodoDoble()#creo el nuevo nodo
        self.NuevoNodo.dato=valor#le asigno el valor al nuevo nodo 
        if self.PrimerNodo is None:#si el primero es null
            self.PrimerNodo=self.NuevoNodo
            self.PrimerNodo.Siguiente=None
            self.PrimerNodo.anterior=None
            self.UltimoNodo=self.PrimerNodo
            self.contador+=1#cuando vuelva a insertar en index tendra ya otro valor
            
        else:
         self.UltimoNodo.Siguiente=self.NuevoNodo
         self.NuevoNodo.anterior=self.UltimoNodo
         self.NuevoNodo.Siguiente=None
         self.UltimoNodo=self.NuevoNodo
         self.contador+=1#cuando vuelva a insertar en index tendra ya otro valor

    def Insertar_Inicio(self,Valor):
        self.NuevoNodo=NodoDoble() #creo el nuevo nodo
        self.NuevoNodo.dato=Valor#le asigno el valor al nuevo nodo
        if self.PrimerNodo is None:#si el primero es null
            self.PrimerNodo=self.NuevoNodo
            self.PrimerNodo.Siguiente=None
            self.PrimerNodo.anterior=None
            self.UltimoNodo=self.PrimerNodo
            self.contador+=1#cuando vuelva a insertar en index tendra ya otro valor
            
        else:
           self.PrimerNodo.anterior=self.NuevoNodo#apunta al anterior del primero que estaba en la lista que sera el nuevo
           self.NuevoNodo.Siguiente=self.PrimerNodo#el nuevo en su siguiente apunta al primero
           self.NuevoNodo.anterior=None#el nuevo en su anterior apunta null
           self.PrimerNodo=self.NuevoNodo#y el nuevo ahora sera el primero
           self.contador+=1#Sirve para saber el tamano de la lista 
            

    def Imprimir_Lista(self):
        self.NodoAux=NodoDoble()
        self.NodoAux=self.PrimerNodo
        while self.NodoAux is not None:

            print(self.NodoAux.dato,end='')
            if self.NodoAux.Siguiente is not None:
                print('->',end='')
            self.NodoAux=self.NodoAux.Siguiente
            
    def Insertar_Pos(self,indice,Valor):
        contadorAux=0
        self.NodoAux=NodoDoble()
        self.NodoAux2=NodoDoble()
        self.NodoCreado=NodoDoble()
        self.NodoAux=self.PrimerNodo
        self.NodoAux2=None
        if indice >= 0 and indice < self.contador :
            while self.NodoAux is not None:
                if  indice==0 and contadorAux==0:#si el indice enviado es 0 entonces hay que insertar en la posicion del primero de la lista y correr el primero a segundo
                    self.NodoCreado.dato=Valor#le asigno el valor al nuevo nodo creado
                    self.PrimerNodo=self.NodoCreado#por ende el primero sera ahora el nuevo
                    self.NodoAux.anterior=self.PrimerNodo#este NodoAux Esta apuntando al primero que ahora es segundo, ahora apunta en su anterior al nuevoNodo que es ahora el primero
                    self.PrimerNodo.Siguiente=self.NodoAux#Este primero es ya el NuevoNodo que ingrese entonces apunto al nodoAux que era antes el primero pero ahora esta como segundo
                    self.contador+=1#sirve para notificar que ya se a aumentado la lista en uno mas
                elif contadorAux==indice: #si no es el primero entonces es el segundo,tercero,etc....
                    self.NodoCreado.dato=Valor#le asigno el valor al nuevo nodo creado
                    self.NodoAux2.Siguiente=self.NodoCreado#como el nodo Aux2 esta siempre apuntando detras del nodoAux entonces tengo el puntero de atras antes de implantar el nuevo nodo en medio de los dos
                    self.NodoCreado.anterior=self.NodoAux2#el NuevoNodo Apuntara a NodoAux2 y asi me aseguro de tener conectada la estructura que este antes del nuevo nodo
                    self.NodoAux.anterior=self.NodoCreado#ahora este Esta despues del nuevo Nodo entonces en su anterior apunto al nuevo
                    self.NodoCreado.Siguiente=self.NodoAux#y el nodo nuevo en su siguiente apunta al NodoAux el cual tenia esa posicion que ahora ocupa el Nuevo Nodo
                    self.contador+=1#sirve para aumenta el tamano que posee la lista
                self.NodoAux2=self.NodoAux
                self.NodoAux=self.NodoAux.Siguiente    
                contadorAux+=1#si ingresa de indice 2 y contador empieza en 0 lo unico que hace esto es llegar al numero y hasta ese momento entrar al else if y asi insertar en esa posicion


        elif indice<0:
            print('No Pueda Haber Index negativo No Se Inserto El Valor Que Establecio')        
        
        elif indice>self.contador:
            print('Error se ha excedido Index de la lista No Se Inserto El Valor Que Establecio')

    def Obtener_Pos(self,indice):
        self.NodoAux=NodoDoble()
        self.NodoAux=self.PrimerNodo
        contadorAux=0
        if indice >= 0 and indice < self.contador :
            while self.NodoAux is not None:
                if  indice==0 and contadorAux==0:#si el indice enviado es 0 entonces hay que devolver el valor de la primera posicion
                    print('El Valor En El Index: '+str(indice)+' es:')
                    print(self.NodoAux.dato)
                
                    self.contador+=1#sirve para verificar si ya he llegado al indice
                elif contadorAux==indice: #si no es el primero entonces es el segundo,tercero,etc....
                    print('El Valor En El Index: '+str(indice)+' es:')
                    print(self.NodoAux.dato)

                    self.contador+=1#sirve para aumenta el tamano que posee la lista

                self.NodoAux=self.NodoAux.Siguiente    
                contadorAux+=1#si ingresa de indice 2 y contador empieza en 0 lo unico que hace esto es llegar al numero y hasta ese momento entrar al else if y asi insertar en esa posicion


        elif indice<0:
            print('No Pueda Haber Index negativo No Se Puede Mostrar Valor Que Establecio')        
        
        elif indice>self.contador:
            print('Error se ha excedido Index de la lista No Se Puede Mostrar El Valor Que Establecio')

    def Eliminar(self,indice):

        self.NodoAux=NodoDoble()
        self.NodoAux2=NodoDoble()
        self.NodoAux=self.PrimerNodo
        self.NodoAux2=None
        contadorAux=0
        if indice >= 0 and indice < self.contador :
            while self.NodoAux is not None:
                
                if  indice==0 and contadorAux==0:#si el indice enviado es 0 entonces hay que devolver el valor de la primera posicion
                    self.PrimerNodo=self.PrimerNodo.Siguiente
                    self.PrimerNodo.anterior=None
                    self.contador+=1#sirve para verificar si ya he llegado al indice

                elif contadorAux==indice: #si no es el primero entonces es el segundo,tercero,etc....

                    self.NodoAux2.Siguiente=self.NodoAux.Siguiente
                    self.NodoAux.Siguiente.anterior=self.NodoAux.anterior
                    self.contador+=1#sirve para aumenta el tamano que posee la lista
                self.NodoAux2=self.NodoAux
                self.NodoAux=self.NodoAux.Siguiente    
                contadorAux+=1#si ingresa de indice 2 y contador empieza en 0 lo unico que hace esto es llegar al numero y hasta ese momento entrar al else if y asi insertar en esa posicion


        elif indice<0:
            print('No Pueda Haber Index negativo No Se Puede Mostrar Valor Que Establecio')        
        
        elif indice>self.contador:
            print('Error se ha excedido Index de la lista No Se Puede Mostrar El Valor Que Establecio')
    
    def Graficar(self):
        self.contadorGrafica+=1
        archivo=open("nuevo"+str(self.contadorGrafica)+".dot","w")#uso el contador para poder crear diversos archivos .dot al igual que imagenes de distinto nombre
        archivo.write("digraph G {\n")
        archivo.write("rankdir=LR;\n")
        archivo.write("node [shape=record];\n")
        self.NodoAux=NodoDoble()
        self.NodoAux2=NodoDoble()
        self.NodoAux=self.PrimerNodo
         
        while self.NodoAux is not None:
            
            archivo.write(str(self.NodoAux.dato)+"[shape=box];\n")

            self.NodoAux=self.NodoAux.Siguiente
        self.NodoAux=self.PrimerNodo
        while self.NodoAux is not None:
            if self.NodoAux.Siguiente is not None:
                self.NodoAux2=self.NodoAux.Siguiente
                archivo.write(str(self.NodoAux.dato)+"->"+str(self.NodoAux2.dato)+"\n")
                archivo.write(str(self.NodoAux2.dato)+"->"+str(self.NodoAux.dato)+"\n")
            

            self.NodoAux=self.NodoAux.Siguiente
        archivo.write("}")
        archivo.close()
        os.system("dot -Tjpg nuevo"+str(self.contadorGrafica)+".dot -o imagen"+str(self.contadorGrafica)+".jpg")
            

