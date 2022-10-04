#Exercicio 1
pessoa = {}
galera = []
soma = 0
media = 0
while resp:
    pessoa.clear()
    pessoa['nome'] = input("Digite seu nome: ")
    while True:
       pessoa['genero'] = input("Informe o sexo Masculino ou Feminino: ").upper()[0]
       if pessoa['genero'] in "MF":
           break
       else:
            print("Erro! Atenção a entrada valida: ")         
    pessoa['idade'] = int(input("Informe a idade: "))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    resp = input("Quer continuar ? Sim ou Não?").upper()[0]
    if resp == "N":
        break
print(f"Ao todo Temos {len(galera)} Cadastradas")    
media = soma/len(galera)  
print("A media de idade é: %.2f " % media)  
print("As mulheres cadastradas foram: ", end=" ")
for p in galera:
    if p['genero'] == "F":
        print(f"\n{p['nome']},", end=" ")
print()        
print("As pessoas acima da media são: ") 
for p in galera:
    if p['idade'] >= media:
         print(f"{p['nome']} {p['idade']}")   
         
#Exercicio 2
tupla = ()
num = []
for tupla in range(4):
    tupla = int(input("Digite um numero: "))
    num.append(tupla)
  

print(num[1])


#Exercicio 3
tupla = ({'Aluno': 'Lucas', 'Universidade': 'Unip', 'nota': 9.8, 'resultado': 'Aprovado'})

w = tupla['Aluno']
x = tupla['Universidade']
y = tupla['nota']
z = tupla['resultado']

print(f"Aluno {w}")
print(f"Universidade {x}")
print(f"Nota {y}")
print(f"Resultado {z}")
 
#Exercicio 4
setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = set(["mango"])

uniao = setx | sety | setz  
intersecsao = setx & sety & setz
repetidos = setx.issubset(setz)
repetidos2 = setx.issubset(sety)
diferente = setx.symmetric_difference(sety)   
         
print(uniao) 
print(intersecsao)
print(repetidos)
print(repetidos2)
print(diferente)




#Exercicio 5
cor = ([{'color1': 'Red'},{'color2': 'Green'},{'color3': 'Blue'}])
cor.insert(0,{'color4': 'Yellow'})

print(cor)
#Exercicio 6
def right_justify(s, total_length = 70):
    return ' ' * (total_length - len(s)) + s


a = right_justify('Folha')

# print(a)
#Exercicio 7
from __future__ import print_function, division
from email.charset import Charset
from numbers import Integral, Number
from re import L
import string
from unicodedata import numeric
from xml.dom.minidom import CharacterData


def chama_duas_vezes(func, numero):
    """Runs a function twice.
    func: function object
    arg: argument passed to the function
    """
#2 - chamou aqui, e daqui chama a função "print_duas_vezes" para impressões seguidas    
    func(numero + 1)
    func(numero + 2)


def print_duas_vezes(numero):
#2.5 - ela aguarda ser chamada consecutivamente    
    print(numero)
    print(numero)


def chama_quatro_vezes(func, numero):
#4 - daqui ela chama a funçao chama_duas_vezes para fazer tudo de novo, ou seja, 
# ocorrerá 2 impressões, e novamente irá chamar + 2 impressões totalizando 4
    chama_duas_vezes(func, numero + 3)
    chama_duas_vezes(func, numero + 4)

#1 - começa aqui, ira chamar a funçao chama duas apartir daqui.
chama_duas_vezes(print, 2)
print()
#3 - depois da primeira execução, vamos para cá.
chama_quatro_vezes(print, 2)  

# Exercicio 9 incompleto
lista = [3, "C", 9, "H", 4, "Q", 6]
lista.sorted()
print(lista)


