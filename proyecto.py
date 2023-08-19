"""
Se enseña como habrá diferentes sumas en fuciones (que se haran luego)
Y dependiendo la suma habran diferentes resultado
"""

"""
Pregunta de si es preferible un pelicula o una serie o ambas
Teniendo solamente tres opciones
"""
pelicula = 1
serie = 2
ambas = pelicula + serie

"""
Pregunta de que cual es la cantidad de episodios preferida
si es escogida la opcion de serie
Teniendo cuatro opciones para elgir
"""
poco ("1-18") = 1
medio ("19-29") = 2
mucho ("30<") = 3
nada ("sin importar la cantidad") = 4

"""
Pregunta de que generos son los elegidos y preferidos por el usuario
Teniendo varias opciones para escoger, siendo un maxico de 2 las que
el usuario podrá elegir
"""

romance = 1
comedia = 2
drama = 3
accion = 4
ciencia_ficcion = 5
aventura = 6
misterio = 7
terror = 8

"""
Pregunta de que generos especificos de anime son los elegidos y
preferidos por el usuario
Teniendo varias opciones para escoger, siendo un maxico de 3 las que
el usuario podrá elegir
A futuro va a haber una mini explicacion de cada genero
"""

shounen = 1
isekai = 2
superpoderes = 3
mecha = 4
bl = 5
gl = 6
shoujo = 7
escolar = 8
sol ("Slice of life") = 9
josei = 10
seinen = 11
gore = 12

"""
Pregunta de si les gustan los deportes o no
al elegir la opcion de si, se despeglaran las preguntas (solo si es serie)
Teniendo varias opciones para escoger, siendo un maxico de 2 las que
el usuario podrá elegir
"""
deporte
si = 1
no = 0

fut = 1
base = 2
basq = 3
nat = 4
golf = 5
tenis = 6
gymna = 7
patin = 8
skate = 9

"""
Una vez esten hechas las funciones se podran compilar las opciones
y teniendo animes que tengan un rango dependiendo de cada pregunta
asi sabien que programas son mas compatibles con las opciones
siendo que se van a dividir en peliculas y series
se creará un rango en las opciones para que sea mas amplia la gama 
Un ejemplo se demuestra abajo
"""

"""
2 peliculas
"""
Viaje_de_chihiro = (pelicula) + ("Genero" aventura + drama) + \
                   ("genero anime" isekai) + (deporte = no)
I_wanna_eat_you_pancreas = (pelicula) + ("Genero" comedia + drama) + \
                           ("genero anime" shoujo + sol + josei) + (deporte = no)
