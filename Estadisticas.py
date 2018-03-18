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
            minimo = numeros[0]
            for num in numeros:
                if num < minimo:
                    minimo = num
            return [len(numeros), int(minimo)]
        else:
            return [1,int(cadena)]

    def estadisticas_it3(self,cadena):
        if cadena=="":
            return [0,None,None]
        elif "," in cadena:
            numeros = cadena.split(",")
            minimo = numeros[0]
            maximo = numeros[0]
            for num in numeros:
                if num < minimo:
                    minimo = num
                if num > maximo:
                    maximo = num
            return [len(numeros), int(minimo), int(maximo)]
        else:
            return [1,1,1]
