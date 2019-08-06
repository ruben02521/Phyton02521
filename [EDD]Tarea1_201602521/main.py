from ListaDoble import ListaDoble #como lista doble ya tiene importada la clase nodo doble ya puedo usar todo lo de las clases aqui
class principal:
    ListaEnlazadaDoble=ListaDoble()
   
    ListaEnlazadaDoble.Insertar_Inicio(10)
    ListaEnlazadaDoble.Insertar_Inicio(20)
    ListaEnlazadaDoble.Insertar_Inicio(30)
    ListaEnlazadaDoble.Insertar_Inicio(40)
    ListaEnlazadaDoble.Insertar_Inicio(50)
    ListaEnlazadaDoble.Insertar_Final(100)
    ListaEnlazadaDoble.Insertar_Final(200)
    ListaEnlazadaDoble.Insertar_Final(300)
    ListaEnlazadaDoble.Insertar_Final(400)
    ListaEnlazadaDoble.Insertar_Final(500)
    ListaEnlazadaDoble.Graficar()
    print(end='\n')
    print('Lista Con Inserciones De Inicio y Fin:')
    ListaEnlazadaDoble.Imprimir_Lista()
    print(end='\n')
    ListaEnlazadaDoble.Insertar_Pos(3,777)
    ListaEnlazadaDoble.Insertar_Pos(8,999)
    ListaEnlazadaDoble.Graficar()#inserto antes en los indices especificados y luego grafico con este metodo
    print(end='\n')
    print('Lista Con Inserciones De Index Especificado:')
    ListaEnlazadaDoble.Imprimir_Lista()
    print(end='\n')
    print(end='\n')
    ListaEnlazadaDoble.Obtener_Pos(3)# muestra el 777 en consola
    ListaEnlazadaDoble.Eliminar(0)# borra el 50
    ListaEnlazadaDoble.Eliminar(4)# borra el 10
    ListaEnlazadaDoble.Graficar()#Elimino antes en los indices especificados y luego grafico con este metodo
    print('Lista Con Eliminacion De Index Especificado:')
    ListaEnlazadaDoble.Imprimir_Lista()
    print(end='\n')
    input('Pulse Cualquier Tecla Para Terminar')
    