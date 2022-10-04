import moduloexe8
import math

l =[]

for x in range(2):
     l.append(moduloexe8.mult("Digite um numero: ", 0, 100))
     if len(l) == 2:
         print("Mensagem de multiplicação efetuada Resultado aparecerá abaixo.")

resultado = math.prod(l)     
print("Multiplicação: %.1f" % resultado) 