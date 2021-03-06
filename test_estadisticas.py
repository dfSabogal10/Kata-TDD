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
        self.assertEqual(Estadisticas().estadisticas("4,3,2,1"), [4], "Multiples numeros")

    def test_estadisticas_it2_cadenavacia(self):
        self.assertEqual(Estadisticas().estadisticas_it2(""), [0,None], "iteracion 2: cadena vacia")

    def test_estadisticas_it2_unnumero(self):
        self.assertEqual(Estadisticas().estadisticas_it2("1"), [1,1], "iteracion 2: un numero")

    def test_estadisticas_it2_dosnumeros(self):
        self.assertEqual(Estadisticas().estadisticas_it2("1,2"), [2,1], "iteracion 2: dos numeros")

    def test_estadisticas_it2_multiplesnumeros(self):
        self.assertEqual(Estadisticas().estadisticas_it2("4,3,2,1"), [4,1], "iteracion 2: multiples numeros")

    def test_estadisticas_it3_cadenavacia(self):
        self.assertEqual(Estadisticas().estadisticas_it3(""), [0,None,None], "iteracion 3: cadena vacia")

    def test_estadisticas_it3_unnumero(self):
        self.assertEqual(Estadisticas().estadisticas_it3("1"), [1, 1, 1], "iteracion 3: un numero")

    def test_estadisticas_it3_dosnumeros(self):
        self.assertEqual(Estadisticas().estadisticas_it3("1,2"), [2, 1, 2], "iteracion 3: dos numeros")

    def test_estadisticas_it3_multiplesnumeros(self):
        self.assertEqual(Estadisticas().estadisticas_it3("4,3,2,1"), [4, 1, 4], "iteracion 3: multiples numeros")

    def test_estadisticas_it4_cadenavacia(self):
        self.assertEqual(Estadisticas().estadisticas_it4(""), [0, None, None,None], "iteracion 4: cadena vacia")

    def test_estadisticas_it4_unnumero(self):
        self.assertEqual(Estadisticas().estadisticas_it4("1"), [1, 1, 1,1], "iteracion 4: un numero")

    def test_estadisticas_it4_dosnumeros(self):
        self.assertEqual(Estadisticas().estadisticas_it4("1,2"), [2, 1, 2,1.5], "iteracion 4: dos numeros")

    def test_estadisticas_it4_multiplesnumeros(self):
        self.assertEqual(Estadisticas().estadisticas_it4("4,3,2,1"), [4, 1, 4,2.5], "iteracion 4: multiples numeros")

