from unittest import TestCase

from Estadisticas import Estadisticas

class TestEstadisticas(TestCase):
    def test_estadisticas_it1(self):
        self.assertEqual(Estadisticas().estadisticas(""),[0],"cadena vacia")

    def test_estadisticas_it1_unnumero(self):
        self.assertEqual(Estadisticas().estadisticas("1"),[1],"Un numero")

    def test_estadisticas_it1_dosnumeros(self):
        self.assertEqual(Estadisticas().estadisticas("1,2"), [2], "Dos numeros")

    def test_estadisticas_it1_multiplesnumeros(self):
        self.assertEqual(Estadisticas().estadisticas("1,2,3,4"), [4], "Multiples numeros")

    def test_estadisticas_it2_cadenavacia(self):
        self.assertEqual(Estadisticas().estadisticas_it2(""), [0,None], "iteracion 2: cadena vacia")

    def test_estadisticas_it2_unnumero(self):
        self.assertEqual(Estadisticas().estadisticas_it2("1"), [1,1], "iteracion 2: unnumero")
    
    def test_estadisticas_it2_dosnumeros(self):
        self.assertEqual(Estadisticas().estadisticas_it2("1,2"), [2,1], "iteracion 2: dosnumeros")
