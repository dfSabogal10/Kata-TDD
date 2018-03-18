class Estadisticas:
    def estadisticas(self, cadena):
        if cadena=="":
            return [0]
        elif "," in cadena:
            numeros=cadena.split(",")
            return [len(numeros)]
        else:
            return [1]

    def estadisticas_it2(self,cadena):
        if cadena=="":
            return [0,None]
        elif "," in cadena:
            numeros=cadena.split(",")
            if numeros[0]<numeros[1]:
                return [2,int(numeros[0])]
            else:
                return [2,int(numeros[1])]
        else:
            return [1,int(cadena)]
