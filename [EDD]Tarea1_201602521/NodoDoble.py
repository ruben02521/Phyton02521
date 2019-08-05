class NodoDoble:
#constructor es con _init_

    def _init_(self, dato):
        #aqui pongo self que es como this, de una les declaro al siguiente y anterior como null(none)
        self.dato=dato  #el elemento que envien al constructor sera el que se le impondra al elemento dentro del nodo
        self.Siguiente=None
        self.anterior=None
    