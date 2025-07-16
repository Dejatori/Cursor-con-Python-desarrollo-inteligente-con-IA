"""
Tests para la función contar_palabras
-------------------------------------
Pruebas unitarias para verificar el correcto funcionamiento del contador de palabras.
"""

import unittest
from contador import contar_palabras

class TestContarPalabras(unittest.TestCase):
    """
    Pruebas unitarias para la función contar_palabras.
    Cada método prueba un caso de uso diferente.
    """

    def test_texto_simple(self):
        """Debe contar correctamente palabras simples y únicas."""
        texto = "hola mundo python"
        total, contador = contar_palabras(texto)
        self.assertEqual(total, 3)
        self.assertEqual(contador['hola'], 1)
        self.assertEqual(contador['mundo'], 1)
        self.assertEqual(contador['python'], 1)

    def test_texto_con_palabras_repetidas(self):
        """Debe contar correctamente palabras repetidas."""
        texto = "hola mundo hola python mundo"
        total, contador = contar_palabras(texto)
        self.assertEqual(total, 5)
        self.assertEqual(contador['hola'], 2)
        self.assertEqual(contador['mundo'], 2)
        self.assertEqual(contador['python'], 1)

    def test_texto_vacio(self):
        """Debe devolver cero para texto vacío."""
        texto = ""
        total, contador = contar_palabras(texto)
        self.assertEqual(total, 0)
        self.assertEqual(len(contador), 0)

    def test_texto_solo_espacios(self):
        """Debe devolver cero para texto con solo espacios o saltos de línea."""
        texto = "   \n\t   "
        total, contador = contar_palabras(texto)
        self.assertEqual(total, 0)
        self.assertEqual(len(contador), 0)

    def test_texto_con_puntuacion(self):
        """Debe ignorar signos de puntuación y contar solo palabras."""
        texto = "¡Hola, mundo! ¿Cómo estás? Python es genial."
        total, contador = contar_palabras(texto)
        self.assertEqual(total, 7)
        self.assertEqual(contador['hola'], 1)
        self.assertEqual(contador['mundo'], 1)
        self.assertEqual(contador['cómo'], 1)
        self.assertEqual(contador['estás'], 1)
        self.assertEqual(contador['python'], 1)
        self.assertEqual(contador['es'], 1)
        self.assertEqual(contador['genial'], 1)

    def test_texto_con_numeros(self):
        """Debe contar números como palabras independientes."""
        texto = "Python 3.9 es la versión 3 del lenguaje"
        total, contador = contar_palabras(texto)
        self.assertEqual(total, 9)
        self.assertEqual(contador['python'], 1)
        self.assertEqual(contador['3'], 2)  # Aparece dos veces
        self.assertEqual(contador['9'], 1)
        self.assertEqual(contador['es'], 1)
        self.assertEqual(contador['la'], 1)
        self.assertEqual(contador['versión'], 1)
        self.assertEqual(contador['del'], 1)
        self.assertEqual(contador['lenguaje'], 1)

    def test_texto_con_mayusculas_minusculas(self):
        """Debe ignorar diferencias entre mayúsculas y minúsculas."""
        texto = "HOLA Mundo Python hola MUNDO"
        total, contador = contar_palabras(texto)
        self.assertEqual(total, 5)
        self.assertEqual(contador['hola'], 2)
        self.assertEqual(contador['mundo'], 2)
        self.assertEqual(contador['python'], 1)

    def test_texto_con_caracteres_especiales(self):
        """Debe ignorar caracteres especiales y contar solo palabras y números."""
        texto = "Python@programming #coding $100%"
        total, contador = contar_palabras(texto)
        self.assertEqual(total, 4)
        self.assertEqual(contador['python'], 1)
        self.assertEqual(contador['programming'], 1)
        self.assertEqual(contador['coding'], 1)
        self.assertEqual(contador['100'], 1)

    def test_texto_largo(self):
        """Debe contar correctamente en textos largos y con saltos de línea."""
        texto = (
            "\n"
            "Python es un lenguaje de programación interpretado de alto nivel.\n"
            "Fue creado por Guido van Rossum y lanzado por primera vez en 1991.\n"
            "Python tiene una sintaxis simple y clara que favorece la legibilidad del código.\n"
        )
        total, contador = contar_palabras(texto)
        self.assertEqual(total, 36)
        self.assertEqual(contador['python'], 2)
        self.assertEqual(contador['es'], 1)
        self.assertEqual(contador['un'], 1)
        self.assertEqual(contador['lenguaje'], 1)
        self.assertEqual(contador['de'], 2)
        self.assertEqual(contador['programación'], 1)
        self.assertEqual(contador['interpretado'], 1)
        self.assertEqual(contador['alto'], 1)
        self.assertEqual(contador['nivel'], 1)
        self.assertEqual(contador['1991'], 1)

    def test_orden_contador(self):
        """Debe devolver las palabras más comunes en orden descendente de frecuencia."""
        texto = "a b c a b a"
        total, contador = contar_palabras(texto)
        mas_comunes = contador.most_common()
        self.assertEqual(mas_comunes[0], ('a', 3))
        self.assertEqual(mas_comunes[1], ('b', 2))
        self.assertEqual(mas_comunes[2], ('c', 1))

if __name__ == '__main__':
    unittest.main()
