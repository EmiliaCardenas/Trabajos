"""
Va a ser una pantalla extra (tkinter), la cual se abrirá al abrir el codigo
Las preguntas algunas seran radiobutton y otras checkbutton
Se enseña como habrá diferentes sumas en fuciones 
Y dependiendo la suma habran diferentes resultados
"""
import tkinter
quiz_anime = tkinter.Tk()
quiz_anime.configure(bg="white")
quiz_anime.geometry("1800x750")
quiz_anime.title("Quiz Anime")
#----------------------------------------------------------------------------------
"""
Funciones para las primeras 2 preguntas,
las cuales ayudaran a desplegar las listas
"""
eleccion1 = ["Pelicula", "Serie"]
def formatos (eleccion1):
    for i in range(len(eleccion1)):
        radiobutton1 = tkinter.Radiobutton(quiz_anime, text= eleccion1[i],
                                           variable = formato,indicatoron=0,
                                           value=i, width=10,
                                           font=('Arial',9)).pack(anchor="w")

eleccion2 = ["1 a 18","19 a 29","Más de 30","Sin importar la cantidad", "Elegí pelicula"]
def cantidades (eleccion2):
    for i in range(len(eleccion2)):
        radiobutton2 = tkinter.Radiobutton(quiz_anime, text= eleccion2[i],
                                           variable = cantidad,indicatoron=0,
                                           value=i, width=20,
                                           font=('Arial',9)).pack(anchor="w")

print("Peliculas:")
recom = [["El Castillo Vagabundo"],["El Viaje de Chihiro"],["I wanna eat your pancreas"]]
i = 0
while i < len(recom):
    print(recom[i])
    i = i+1
print(" ")
print("Series:")  

i=0
while i < 5:
    print(" ")
    i = i+1
#----------------------------------------------------------------------------------
parte1 = tkinter.Label(quiz_anime,
                      text="Bienvenidxs a este <<Quiz de Anime>>",
                       bg="white", font=('Comic Sans MS',20)).pack(anchor="w")
parte15 = tkinter.Label(quiz_anime,
                      text="Este Quiz es para darte una recomendacion de que Anime deberias ver, basandose en las respuestas que elijas",
                        bg="white", font=('Comic Sans MS',12)).pack(anchor="w")
parte2 = tkinter.Label(quiz_anime,
                      text="Lee las instrucciones y contesta las preguntas. Si no aparece ningun resultado es por que aun no hay alguna recomendacion con esa descripcion",
                       bg="white", font=('Comic Sans MS',12)).pack(anchor="w")
espacio = tkinter.Label(quiz_anime, text=' ', bg='white').pack(anchor="w")

"""
Pregunta de si es preferible una pelicula o una serie o ambas
Teniendo solamente tres opciones (radiobutton)
"""
text2 = tkinter.Label(quiz_anime,
                      text="¿Que formato prefieres: pelicula, serie?",
                      bg="white", font=('Arial',12,'bold'))
text2.pack(anchor="w")

formato = tkinter.IntVar()
pregunta1 = formatos(eleccion1)
print(pregunta1)
#----------------------------------------------------------------------------------
"""
Pregunta de que cual es la cantidad de episodios preferida
si es escogida la opcion de serie
Teniendo cuatro opciones para elgir (radiobutton)
"""
text3 = tkinter.Label(quiz_anime,
                      text="¿Que cantidad de capitulos prefieres?",
                      bg="white", font=('Arial',12,'bold'))
text3.pack(anchor="w")
cantidad = tkinter.IntVar()
pregunta2 = cantidades (eleccion2)
print(pregunta2)
#----------------------------------------------------------------------------------
"""
Pregunta de que generos son los elegidos y preferidos por el usuario
Teniendo varias opciones para escoger, siendo un maximo de 2 las que
el usuario podrá elegir (checkbutton)
"""
text4 = tkinter.Label(quiz_anime,
                      text="¿Que genero prefieres? (escoge 2)",
                      bg="white", font=('Arial',12,'bold'))
text4.place(x=390, y=120)
romance = tkinter.IntVar()
comedia = tkinter.IntVar()
drama = tkinter.IntVar()
accion = tkinter.IntVar()
ciencia_ficcion = tkinter.IntVar()
aventura = tkinter.IntVar()
misterio = tkinter.IntVar()
terror = tkinter.IntVar()
deporte = tkinter.IntVar()
c31 = tkinter.Checkbutton(quiz_anime, text = "Romance", indicatoron=0,
                          variable = romance, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=400, y=145)
c32 = tkinter.Checkbutton(quiz_anime, text = "Comedia", indicatoron=0,
                          variable = comedia, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=400, y=170)
c33 = tkinter.Checkbutton(quiz_anime, text = "Drama", indicatoron=0,
                          variable = drama, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=400, y=195)
c34 = tkinter.Checkbutton(quiz_anime, text = "Accion", indicatoron=0,
                          variable = accion, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=400, y=220)
c35 = tkinter.Checkbutton(quiz_anime, text = "Ciencia ficcion", indicatoron=0,
                          variable = ciencia_ficcion, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=400, y=245)
c36 = tkinter.Checkbutton(quiz_anime, text = "Aventura", indicatoron=0,
                          variable = aventura, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=400, y=270)
c37 = tkinter.Checkbutton(quiz_anime, text = "Misterio", indicatoron=0,
                          variable = misterio, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=400, y=295)
c38 = tkinter.Checkbutton(quiz_anime, text = "Terror", indicatoron=0,
                          variable = terror, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=400, y=320)
c39 = tkinter.Checkbutton(quiz_anime, text = "Deporte", indicatoron=0,
                          variable = deporte, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=400, y=345) 
#----------------------------------------------------------------------------------
"""
Pregunta de que generos especificos de anime son los elegidos y
preferidos por el usuario
Teniendo varias opciones para escoger, siendo un maximo de 2 las que
el usuario podrá elegir (checkbutton)
A futuro va a haber una mini explicacion de cada genero
"""
text5 = tkinter.Label(quiz_anime,
                      text="¿Que genero de anime prefieres? (escoge 2)",
                      bg="white", font=('Arial',12,'bold'))
text5.place(x=790, y=120)
shounen = tkinter.IntVar()
isekai = tkinter.IntVar()
superpoderes = tkinter.IntVar()
mecha = tkinter.IntVar()
bl = tkinter.IntVar()
gl = tkinter.IntVar()
shoujo = tkinter.IntVar()
escolar = tkinter.IntVar()
slice_of_life = tkinter.IntVar()
josei = tkinter.IntVar()
seinen = tkinter.IntVar()
gore = tkinter.IntVar()
c41 = tkinter.Checkbutton(quiz_anime, text = "Shounen", indicatoron=0,
                          variable = shounen, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=800, y=145)
c42 = tkinter.Checkbutton(quiz_anime, text = "Isekai", indicatoron=0,
                          variable = isekai, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=800, y=170)
c43 = tkinter.Checkbutton(quiz_anime, text = "Superpoderes / Magia", indicatoron=0,
                          variable = superpoderes, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=800, y=195)
c44 = tkinter.Checkbutton(quiz_anime, text = "Mecha", indicatoron=0,
                          variable = mecha, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=800, y=220)
c45 = tkinter.Checkbutton(quiz_anime, text = "BL", indicatoron=0,
                          variable = bl, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=800, y=245)
c46 = tkinter.Checkbutton(quiz_anime, text = "GL", indicatoron=0,
                          variable = gl, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=800, y=270)
c47 = tkinter.Checkbutton(quiz_anime, text = "Shoujo", indicatoron=0,
                          variable = shoujo, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=800, y=295)
c48 = tkinter.Checkbutton(quiz_anime, text = "Escolar", indicatoron=0,
                          variable = escolar, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=800, y=320)
c49 = tkinter.Checkbutton(quiz_anime, text = "Slice of life", indicatoron=0,
                          variable = slice_of_life, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=800, y=345)
c410 = tkinter.Checkbutton(quiz_anime, text = "Josei", indicatoron=0,
                          variable = josei, onvalue = 1,
                          offvalue = 0, width=20,
                           font=('Arial',9)).place(x=800, y=370)
c411 = tkinter.Checkbutton(quiz_anime, text = "Seinen", indicatoron=0,
                          variable = seinen, onvalue = 1,
                          offvalue = 0, width=20,
                           font=('Arial',9)).place(x=800, y=395)
c412 = tkinter.Checkbutton(quiz_anime, text = "Gore", indicatoron=0,
                          variable = gore, onvalue = 1,
                          offvalue = 0, width=20,
                           font=('Arial',9)).place(x=800, y=420)
#----------------------------------------------------------------------------------
i=0
while i < 11 :
    espacio = tkinter.Label(quiz_anime, text=' ', bg='white').pack(anchor="w")
    i = i+1

"""
Una vez esten hechas las funciones se podran compilar las opciones
y teniendo animes que tengan un rango dependiendo de cada pregunta
asi sabien que programas son mas compatibles con las opciones
siendo que se van a dividir en peliculas y series
se creará un rango en las opciones para que sea mas amplia la gama 
Abajo se demuestra un ejemplo de como seria un resultado en concreto
Las opciones estan ordenadas alfabeticamente, separadas
primero las peliculas y despues las series
"""
def resultado ():
    if (formato.get() == 0) and (cantidad.get() == 4):
#El Castillo Vagabundo
        if (((romance.get() == 1) and (aventura.get() == 1))
            and ((shoujo.get() == 1) and (superpoderes.get() == 1))):
            ecv = tkinter.Label(quiz_anime, text = "Deberias ver: << El Castillo Vagabundo >>")
            ecv.pack(anchor="w")

#El Viaje de Chihiro
        elif (((romance.get() == 1) and (aventura.get() == 1))
            and ((isekai.get() == 1) and (superpoderes.get() == 1))):
            chihiro = tkinter.Label(quiz_anime, text = "Deberias ver: << El Viaje de Chihiro >>")
            chihiro.pack(anchor="w")

#I wanna eat your pancreas
        elif (((drama.get() == 1) and (romance.get() == 1))
            and ((slice_of_life.get() == 1) and (josei.get() == 1))):
            iweyp = tkinter.Label(quiz_anime, text = "Deberias ver: << I wanna eat your pancreas >>")
            iweyp.pack(anchor="w")

#Ponyo
        elif (((drama.get() == 1) and (ciencia_ficcion.get() == 1))
            and ((slice_of_life.get() == 1) and (superpoderes.get() == 1))):
            ponyo = tkinter.Label(quiz_anime, text = "Deberias ver: << Ponyo >>")
            ponyo.pack(anchor="w")

#Umibe no Etranger
        elif (((drama.get() == 1) and (romance.get() == 1))
            and ((slice_of_life.get() == 1) and (bl.get() == 1))):
            une = tkinter.Label(quiz_anime, text = "Deberias ver: << Umibe no Etranger >>")
            une.pack(anchor="w")

#----------------------------------------------------------------------------------

#Banana Fish
    elif (formato.get() == 1):
        if (((cantidad.get() == 1 or (cantidad.get() == 3))
            and ((romance.get() == 1) and (drama.get() == 1))
            and ((bl.get() == 1) and (seinen.get() == 1)))):
            bf = tkinter.Label(quiz_anime, text = "Deberias ver: << Banana Fish >>")
            bf.pack(anchor="w")

#Chainsaw Man
        elif (((cantidad.get() == 0 or (cantidad.get() == 3))
            and ((accion.get() == 1) and (terror.get() == 1))
            and ((shounen.get() == 1) and (gore.get() == 1)))):
            chainsaw = tkinter.Label(quiz_anime, text = "Deberias ver: << Chainsaw Man >>")
            chainsaw.pack(anchor="w")

#Corpse Party
        elif (((cantidad.get() == 0 or (cantidad.get() == 3))
            and ((terror.get() == 1) and (misterio.get() == 1))
            and ((gore.get() == 1) and (escolar.get() == 1)))):
            cp = tkinter.Label(quiz_anime, text = "Deberias ver: << Corpse Party >>")
            cp.pack(anchor="w")

#Demon Slayer
        elif (((cantidad.get() == 2 or (cantidad.get() == 3))
            and ((accion.get() == 1) and (aventura.get() == 1))
            and ((shounen.get() == 1) and (gore.get() == 1)))):
            demon = tkinter.Label(quiz_anime, text = "Deberias ver: << Demon Slayer >>")
            demon.pack(anchor="w")

#Free
        elif (((cantidad.get() == 2 or (cantidad.get() == 3))
            and ((deporte.get() == 1) and (comedia.get() == 1))
            and ((escolar.get() == 1) and (slice_of_life.get() == 1)))):
            free = tkinter.Label(quiz_anime, text = "Deberias ver: << Free >>")
            free.pack(anchor="w")

#How to keep a Mummy
        elif (((cantidad.get() == 0 or (cantidad.get() == 3))
            and ((ciencia_ficcion.get() == 1) and (comedia.get() == 1))
            and ((superpoderes.get() == 1) and (slice_of_life.get() == 1)))):
            htkam = tkinter.Label(quiz_anime, text = "Deberias ver: << How to keep a Mummy >>")
            htkam.pack(anchor="w")

#Hunter X Hunter
        elif (((cantidad.get() == 2 or (cantidad.get() == 3))
            and ((accion.get() == 1) and (drama.get() == 1))
            and ((shounen.get() == 1) and (superpoderes.get() == 1)))):
            hxh = tkinter.Label(quiz_anime, text = "Deberias ver: << Hunter X Hunter >>")
            hxh.pack(anchor="w")

#Jobless Reincarnation
        elif (((cantidad.get() == 2 or (cantidad.get() == 3))
            and ((accion.get() == 1) and (ciencia_ficcion.get() == 1))
            and ((isekai.get() == 1) and (seinen.get() == 1)))):
            jr = tkinter.Label(quiz_anime, text = "Deberias ver: << Jobless Reincarnation >>")
            jr.pack(anchor="w")

#Komi Can't Communicate
        elif (((cantidad.get() == 1 or (cantidad.get() == 3))
            and ((romance.get() == 1) and (comedia.get() == 1))
            and ((josei.get() == 1) and (escolar.get() == 1)))):
            stm = tkinter.Label(quiz_anime, text = "Deberias ver: << Komi Can't Communicate >>")
            stm.pack(anchor="w")

#Kotaro vive solo
        elif (((cantidad.get() == 0 or (cantidad.get() == 3))
            and ((comedia.get() == 1) and (drama.get() == 1))
            and ((josei.get() == 1) and (slice_of_life.get() == 1)))):
            kvs = tkinter.Label(quiz_anime, text = "Deberias ver: << Kotaro vive solo >>")
            kvs.pack(anchor="w")

#Magical Girl Ore
        elif (((cantidad.get() == 0 or (cantidad.get() == 3))
            and ((accion.get() == 1) and (comedia.get() == 1))
            and ((superpoderes.get() == 1) and (gl.get() == 1)))):
            mgo = tkinter.Label(quiz_anime, text = "Deberias ver: << Magical Girl Ore >>")
            mgo.pack(anchor="w")

#My Hero Academia
        elif (((cantidad.get() == 2 or (cantidad.get() == 3))
            and ((accion.get() == 1) and (aventura.get() == 1))
            and ((superpoderes.get() == 1) and (escolar.get() == 1)))):
            mha = tkinter.Label(quiz_anime, text = "Deberias ver: << My Hero Academia >>")
            mha.pack(anchor="w")

#No.6
        elif (((cantidad.get() == 0 or (cantidad.get() == 3))
            and ((misterio.get() == 1) and (drama.get() == 1))
            and ((bl.get() == 1) and (seinen.get() == 1)))):
            no6 = tkinter.Label(quiz_anime, text = "Deberias ver: << No.6 >>")
            no6.pack(anchor="w")

#Sasaki to Miyano
        elif (((cantidad.get() == 0 or (cantidad.get() == 3))
            and ((romance.get() == 1) and (comedia.get() == 1))
            and ((bl.get() == 1) and (escolar.get() == 1)))):
            stm = tkinter.Label(quiz_anime, text = "Deberias ver: << Sasaki to Miyano >>")
            stm.pack(anchor="w")

#Sk8 the Infinity
        elif (((cantidad.get() == 0 or (cantidad.get() == 3))
            and ((deporte.get() == 1) and (comedia.get() == 1))
            and ((bl.get() == 1) and(slice_of_life.get() == 1)))):
            sk8 = tkinter.Label(quiz_anime, text = "Deberias ver: << Sk8 the Infinity >>")
            sk8.pack(anchor="w")

#Spy X Family
        elif (((cantidad.get() == 1 or (cantidad.get() == 3))
            and ((accion.get() == 1) and (comedia.get() == 1))
            and ((shounen.get() == 1) and (slice_of_life.get() == 1)))):
            sxf = tkinter.Label(quiz_anime, text = "Deberias ver: << Spy X Family >>")
            sxf.pack(anchor="w")

#Your Lie in April
        elif (((cantidad.get() == 1 or (cantidad.get() == 3))
            and ((romance.get() == 1) and (drama.get() == 1))
            and ((shoujo.get() == 1) and (josei.get() == 1)))):
            ylia = tkinter.Label(quiz_anime, text = "Deberias ver: << Your Lie in April >>")
            ylia.pack(anchor="w")

#Zombieland Saga
        elif (((cantidad.get() == 1 or (cantidad.get() == 3))
            and ((terror.get() == 1) and (comedia.get() == 1))
            and ((josei.get() == 1) and (gore.get() == 1)))):
            zs = tkinter.Label(quiz_anime, text = "Deberias ver: << Zombieland Saga >>")
            zs.pack(anchor="w")
#----------------------------------------------------------------------------------
boton_final = tkinter.Button(quiz_anime, text = "Resultados",
                             bg="#EFB8FF", command=resultado,
                             font=('Arial',20)).place(x=700, y=500)
espacio13 = tkinter.Label(quiz_anime, text=' ', bg='white').pack(anchor="w")
quiz_anime.mainloop()
