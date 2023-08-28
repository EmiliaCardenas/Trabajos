"""
Se inicia pidiendo el nombre de usuario por cortesia
"""
print("Escribre tu nombre, por favor: ")
nombre = str(input())
print("Bienvenidx a este quiz de anime", nombre)

"""
Va a ser una pantalla extra, la cual se abrirá al abrir el codigo
Las preguntas algunas seran radiobutton y otras checkbutton
Se enseña como habrá diferentes sumas en fuciones 
Y dependiendo la suma habran diferentes resultados
"""

"""
Pregunta de si es preferible un pelicula o una serie o ambas
Teniendo solamente tres opciones (radiobutton)
"""
print("¿Que prefieres: pelicula, serie, o ambas?")

if radiobutton1 == pelicula:
    res = 1
elif radiobutton1 == serie:
    res = 2
elif radiobutton1 == ambas:
    res = 3
else:
    res = 0

"""
Pregunta de que cual es la cantidad de episodios preferida
si es escogida la opcion de serie
Teniendo cuatro opciones para elgir (radiobutton)
"""
print("¿Que cantidad de capitulos prefieres?")
poco "1-18"
medio "19-29"
mucho "30<"
nada "sin importar la cantidad"
if radiobutton2 == poco:
    res = 1
elif radiobutton2 == medio:
    res = 2
elif radiobutton2 == mucho:
    res = 3
elif radiobutton2 == nada:
    res = 4
else:
    res = 0

"""
Pregunta de que generos son los elegidos y preferidos por el usuario
Teniendo varias opciones para escoger, siendo un maximo de 2 las que
el usuario podrá elegir (checkbutton)
"""
print("¿Que genero prefieres (escoge 2 como maximo)")

if checkbutton3 == romance:
    res = 1
elif checkbutton3 == comedia:
    res = 2
elif checkbutton3 == drama:
    res = 3
elif checkbutton3 == accion:
    res = 4
elif checkbutton3 == ciencia_ficcion:
    res = 5
elif checkbutton3 == aventura:
    res = 6
elif checkbutton3 == misterio:
    res = 7
elif checkbutton3 == terrror:
    res = 8
else:
    res = 0

"""
Pregunta de que generos especificos de anime son los elegidos y
preferidos por el usuario
Teniendo varias opciones para escoger, siendo un maxico de 3 las que
el usuario podrá elegir (checkbutton)
A futuro va a haber una mini explicacion de cada genero
"""
print("¿Que genero de anime prefieres (escoge 3 como maximo)")
if checkbutton4 == shounen:
    res = 1
elif checkbutton4 == isekai:
    res = 2
elif checkbutton4 == supepoderes:
    res = 3
elif checkbutton4 == mecha:
    res = 4
elif checkbutton4 == bl:
    res = 5
elif checkbutton4 == gl:
    res = 6
elif checkbutton4 == shoujo:
    res = 7
elif checkbutton4 == escolar:
    res = 8
elif checkbutton4 == sol:
    res = 9
elif checkbutton4 == josei:
    res = 10
elif checkbutton4 == seinen:
    res = 11
elif checkbutton4 == gore:
    res = 12
else:
    res = 0

"""
Pregunta de si les gustan los deportes o no (radiobutton)
al elegir la opcion de si, se despeglaran las preguntas (solo si es serie)
Teniendo varias opciones para escoger, siendo un maxico de 2 las que
el usuario podrá elegir (checkbutton)
"""
print("¿Te gustan los deportes? Si sí, escoge cuales (maximo 2)")

if radiobutton5 == si:
    if checkbutton5 == football:
        res = 1
    elif checkbutton5 == baseball:
        res = 2
    elif checkbutton5 == basquetball:
        res = 3
    elif checkbutton5 == natacion:
        res = 4
    elif checkbutton5 == golf:
        res = 5
    elif checkbutton5 == tenis:
        res = 6
    elif checkbutton5 == gymnasia:
        res = 7
    elif checkbutton5 == patinaje:
        res = 8
    elif checkbutton5 == skate:
        res = 9
elif radiobutton5 == no:
    res = 1
else:
    res = 0

"""
Una vez esten hechas las funciones se podran compilar las opciones
y teniendo animes que tengan un rango dependiendo de cada pregunta
asi sabien que programas son mas compatibles con las opciones
siendo que se van a dividir en peliculas y series
se creará un rango en las opciones para que sea mas amplia la gama 
Un ejemplo se demuestra abajo

2 peliculas
"""
Viaje_de_chihiro = (pelicula) + ("Genero" aventura + drama) + \
                   ("genero anime" isekai) + (deporte = no)
"""
Viaje_de_chihiro daria pelicula = 1 genero = 9, genero anime = 2,
deporte 0. Cada una de las sumas en un caso a parte que al final ayuda a ver
si es elegida o no por el usuario
"""
I_wanna_eat_you_pancreas = (pelicula) + ("Genero" comedia + drama) + \
                           ("genero anime" shoujo + sol + josei) + (deporte = no)
