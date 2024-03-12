from Polinomio1 import Polinomio1, Nodo

class Polinomio2(Polinomio1):
    def sumar(self, otro):
        resultado = Polinomio2()
        actual = self.cabeza
        
        # Copiar este polinomio al resultado.
        while actual:
            resultado.agregar_termino(actual.coeficiente, actual.exponente)
            actual = actual.siguiente
        
        # Sumar términos del otro polinomio.
        actual = otro.cabeza
        while actual:
            resultado.agregar_termino(actual.coeficiente, actual.exponente)
            actual = actual.siguiente

        return resultado

    def restar(self, otro):
        resultado = Polinomio2()
        actual = self.cabeza

        # Copiar este polinomio al resultado.
        while actual:
            resultado.agregar_termino(actual.coeficiente, actual.exponente)
            actual = actual.siguiente
        
        # Restar términos del otro polinomio, cambiando el signo del coeficiente.
        actual = otro.cabeza
        while actual:
            resultado.agregar_termino(-actual.coeficiente, actual.exponente)
            actual = actual.siguiente

        return resultado

    def multiplicar(self, otro):
        resultado = Polinomio2()

        actual_self = self.cabeza
        while actual_self:
            actual_otro = otro.cabeza
            while actual_otro:
                nuevo_coef = actual_self.coeficiente * actual_otro.coeficiente
                nuevo_exp = actual_self.exponente + actual_otro.exponente
                resultado.agregar_termino(nuevo_coef, nuevo_exp)
                actual_otro = actual_otro.siguiente
            actual_self = actual_self.siguiente

        return resultado
