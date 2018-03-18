from unittest import TestCase

from Estadisticas import Estadisticas

class TestEstadisticas(TestCase):
    def test_estadisticas(self):
        self.assertEqual(Estadisticas().estadisticas(""),[0],"cadena vacia")

    def test_estadisticas_unnumero(self):
        self.assertEqual(Estadisticas().estadisticas("1"),[1],"Un numero")
