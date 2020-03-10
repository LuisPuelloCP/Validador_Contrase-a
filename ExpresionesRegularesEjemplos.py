import re

cadena = "Estoy empavado"

#print(re.search("empavadoo",cadena)) #Ayuda a buscar un texto en una cadena devuelve un objeto como resultado

textoBuscar = "empavado"

#textoEncontrado = re.search(textoBuscar,cadena) #Otra forma de buscar un texto en una cadena

#print(textoEncontrado.start())# Muestra desde que posicion comenzo a encontrar la palabra en la cadena
#print(textoEncontrado.end())# Muestra desde que posicion terminó la palabra en la cadena
#print(textoEncontrado.span())#Muestra lo anterior de manera conjunta (empieza,termina) y lo muestra en forma de tupla


print(len(re.findall(textoBuscar,cadena))) # nos muestra cuantas veces se repite una palabra en una cadena

""" Metacaracteres

^: Funciona para buscar todo lo que empiece tal palabra en una cadena se coloca al comienzo de la palabra
$: Funciona para buscar todo lo que termine en tal palabre en una cadena se coloca al final de la palabra
[]: Forma un conjunto o clase 
-: Ayuda a definir un rango
{}: Permite colocar la cantidad de caracteres permitidos en forma de rango
():ayuda a separar una expresion de otra

ejemplos:
    [a-z] creamos un conjunto o clase de todas las letras del abecedario(minusculas)
    [A-Z] creamos un conjunto o clase de todas las letras del abecedario(MAYUSCULAS)
    [a-z]{2,5} conjunto de todas las letras minusculas donde solo pueden haber entre 2 y 5 letras minusculas
    ([A-Z]{2,5})([a-z]{2,5}) Esto verifica que la expresion contenga entre 2 y 5 minusculas y mayusculas

    esto que te muestro lo va buscando en orden primero las mayusculas y luego las minusculas, no lo hace en desorden
    para que lo haga en desorden coloca (?=.*[A-Z]{2,5})(?=.*[a-z]{2,5})
    aun no se bien que significan estos simbolos
    ?= si no estoy mal esto sirve para buscar en toda la cadena
    .* = si no estoy mal esto sirva para buscar en cualquier orden
"""