"""
Va a ser una pantalla extra (tkinter), la cual se abrirá al abrir el codigo
Las preguntas algunas seran radiobutton y otras checkbutton
Se enseña como habrá diferentes sumas en fuciones 
Y dependiendo la suma habran diferentes resultados
"""
import tkinter
quiz_anime = tkinter.Tk()
quiz_anime.configure(bg="white")
quiz_anime.geometry("700x700")
quiz_anime.title("Quiz Anime")
"""
Pregunta de si es preferible una pelicula o una serie o ambas
Teniendo solamente tres opciones (radiobutton)
"""
text2 = tkinter.Label(quiz_anime,
                      text="¿Que formato prefieres: pelicula, serie, o ambas?")
text2.pack(anchor="w")
eleccion1 = ["pelicula", "serie", "ambas"]
formato = tkinter.StringVar()
for index in range(len(eleccion1)):
    radiobutton1 = tkinter.Radiobutton(quiz_anime, text= eleccion1[index],
                                       variable = formato,indicatoron=0,
                                       value=index, width=10).pack(anchor="w")

"""
Pregunta de que cual es la cantidad de episodios preferida
si es escogida la opcion de serie
Teniendo cuatro opciones para elgir (radiobutton)
"""
text3 = tkinter.Label(quiz_anime,
                      text="¿Que cantidad de capitulos prefieres?")
text3.pack(anchor="w")
eleccion2 = ["1 a 18","19 a 29","más de 30","sin importar la cantidad", "elegí pelicula"]
cantidad = tkinter.StringVar()
for index in range(len(eleccion2)):
    radiobutton2 = tkinter.Radiobutton(quiz_anime, text= eleccion2[index],
                                       variable = cantidad,indicatoron=0,
                                       value=index, width=20).pack(anchor="w")
"""
Pregunta de que generos son los elegidos y preferidos por el usuario
Teniendo varias opciones para escoger, siendo un maximo de 2 las que
el usuario podrá elegir (checkbutton)
"""
text4 = tkinter.Label(quiz_anime,
                      text="¿Que genero prefieres? (escoge 2 como maximo)")
text4.place(x=300, y=0)

genero = tkinter.IntVar()
genero2 = tkinter.IntVar()
genero3 = tkinter.IntVar()
genero4 = tkinter.IntVar()
genero5 = tkinter.IntVar()
genero6 = tkinter.IntVar()
genero7 = tkinter.IntVar()
genero8 = tkinter.IntVar()

c31 = tkinter.Checkbutton(quiz_anime, text = "romance", indicatoron=0,
                          variable = genero, onvalue = 1,
                          offvalue = 0, width=20).place(x=400, y=20)
c32 = tkinter.Checkbutton(quiz_anime, text = "comedia", indicatoron=0,
                          variable = genero2, onvalue = 1,
                          offvalue = 0, width=20).place(x=400, y=40)
c33 = tkinter.Checkbutton(quiz_anime, text = "drama", indicatoron=0,
                          variable = genero3, onvalue = 1,
                          offvalue = 0, width=20).place(x=400, y=60)
c34 = tkinter.Checkbutton(quiz_anime, text = "accion", indicatoron=0,
                          variable = genero4, onvalue = 1,
                          offvalue = 0, width=20).place(x=400, y=80)
c35 = tkinter.Checkbutton(quiz_anime, text = "ciencia ficcion", indicatoron=0,
                          variable = genero5, onvalue = 1,
                          offvalue = 0, width=20).place(x=400, y=100)
c36 = tkinter.Checkbutton(quiz_anime, text = "aventura", indicatoron=0,
                          variable = genero6, onvalue = 1,
                          offvalue = 0, width=20).place(x=400, y=120)
c37 = tkinter.Checkbutton(quiz_anime, text = "misterio", indicatoron=0,
                          variable = genero7, onvalue = 1,
                          offvalue = 0, width=20).place(x=400, y=140)
c38 = tkinter.Checkbutton(quiz_anime, text = "terror", indicatoron=0,
                          variable = genero8, onvalue = 1,
                          offvalue = 0, width=20).place(x=400, y=160)")
"""
Pregunta de que generos especificos de anime son los elegidos y
preferidos por el usuario
Teniendo varias opciones para escoger, siendo un maxico de 3 las que
el usuario podrá elegir (checkbutton)
A futuro va a haber una mini explicacion de cada genero
"""
text5 = tkinter.Label(quiz_anime,
                      text="¿Que genero de anime prefieres (escoge 3 como maximo)")
text5.place(x=400, y=180)

genero_anime = tkinter.StringVar()
genero_anime2 = tkinter.StringVar()
genero_anime3 = tkinter.StringVar()
genero_anime4 = tkinter.StringVar()
genero_anime5 = tkinter.StringVar()
genero_anime6 = tkinter.StringVar()
genero_anime7 = tkinter.StringVar()
genero_anime8 = tkinter.StringVar()
genero_anime9 = tkinter.StringVar()
genero_anime10 = tkinter.StringVar()
genero_anime11 = tkinter.StringVar()
genero_anime12 = tkinter.StringVar()

c41 = tkinter.Checkbutton(quiz_anime, text = "shounen", indicatoron=0,
                          variable = genero_anime, onvalue = "shounen",
                          offvalue = 0, width=20).place(x=500, y=200)
c42 = tkinter.Checkbutton(quiz_anime, text = "isekai", indicatoron=0,
                          variable = genero_anime2, onvalue = "isekai",
                          offvalue = 0, width=20).place(x=500, y=220)
c43 = tkinter.Checkbutton(quiz_anime, text = "supepoderes", indicatoron=0,
                          variable = genero_anime3, onvalue = "supepoderes",
                          offvalue = 0, width=20).place(x=500, y=240)
c44 = tkinter.Checkbutton(quiz_anime, text = "mecha", indicatoron=0,
                          variable = genero_anime4, onvalue = "mecha",
                          offvalue = 0, width=20).place(x=500, y=260)
c45 = tkinter.Checkbutton(quiz_anime, text = "bl", indicatoron=0,
                          variable = genero_anime5, onvalue = "bl",
                          offvalue = 0, width=20).place(x=500, y=280)
c46 = tkinter.Checkbutton(quiz_anime, text = "gl", indicatoron=0,
                          variable = genero_anime6, onvalue = "gl",
                          offvalue = 0, width=20).place(x=500, y=300)
c47 = tkinter.Checkbutton(quiz_anime, text = "shoujo", indicatoron=0,
                          variable = genero_anime7, onvalue = "shoujo",
                          offvalue = 0, width=20).place(x=500, y=320)
c48 = tkinter.Checkbutton(quiz_anime, text = "escolar", indicatoron=0,
                          variable = genero_anime8, onvalue = "escolar",
                          offvalue = 0, width=20).place(x=500, y=340)
c49 = tkinter.Checkbutton(quiz_anime, text = "slice of life", indicatoron=0,
                          variable = genero_anime9, onvalue = "slice of life",
                          offvalue = 0, width=20).place(x=500, y=360)
c410 = tkinter.Checkbutton(quiz_anime, text = "josei", indicatoron=0,
                          variable = genero_anime10, onvalue = "josei",
                          offvalue = 0, width=20).place(x=500, y=380)
c411 = tkinter.Checkbutton(quiz_anime, text = "seinen", indicatoron=0,
                          variable = genero_anime11, onvalue = "seinen",
                          offvalue = 0, width=20).place(x=500, y=400)
c412 = tkinter.Checkbutton(quiz_anime, text = "gore", indicatoron=0,
                          variable = genero_anime12, onvalue = "gore",
                          offvalue = 0, width=20).place(x=500, y=420)
"""
Pregunta de si les gustan los deportes o no (radiobutton)
al elegir la opcion de si, se despeglaran las preguntas (solo si es serie)
Teniendo varias opciones para escoger, siendo un maxico de 2 las que
el usuario podrá elegir (checkbutton)
"""
text6 = tkinter.Label(quiz_anime,
                      text="¿Te gustan los deportes? Si sí,escoge cuales (maximo 2)")
text6.place(x=600, y=0)

deporte = tkinter.IntVar()
deporte2 = tkinter.IntVar()
deporte3 = tkinter.IntVar()
deporte4 = tkinter.IntVar()
deporte5 = tkinter.IntVar()
deporte6 = tkinter.IntVar()
deporte7 = tkinter.IntVar()
deporte8 = tkinter.IntVar()
deporte9 = tkinter.IntVar()
deporte10 = tkinter.IntVar()

c51 = tkinter.Checkbutton(quiz_anime, text = "football", indicatoron=0,
                          variable = deporte, onvalue = 1,
                          offvalue = 0, width=20).place(x=700, y=20)
c52 = tkinter.Checkbutton(quiz_anime, text = "baseball", indicatoron=0,
                          variable = deporte2, onvalue = 1,
                          offvalue = 0, width=20).place(x=700, y=40)
c53 = tkinter.Checkbutton(quiz_anime, text = "basquetball", indicatoron=0,
                          variable = deporte3, onvalue = 1,
                          offvalue = 0, width=20).place(x=700, y=60)
c54 = tkinter.Checkbutton(quiz_anime, text = "natacion", indicatoron=0,
                          variable = deporte4, onvalue = 1,
                          offvalue = 0, width=20).place(x=700, y=80)
c55 = tkinter.Checkbutton(quiz_anime, text = "golf", indicatoron=0,
                          variable = deporte5, onvalue = 1,
                          offvalue = 0, width=20).place(x=700, y=100)
c56 = tkinter.Checkbutton(quiz_anime, text = "tenis", indicatoron=0,
                          variable = deporte6, onvalue = 1,
                          offvalue = 0, width=20).place(x=700, y=120)
c57 = tkinter.Checkbutton(quiz_anime, text = "gymnasia", indicatoron=0,
                          variable = deporte7, onvalue = 1,
                          offvalue = 0, width=20).place(x=700, y=140)
c58 = tkinter.Checkbutton(quiz_anime, text = "patinaje", indicatoron=0,
                          variable = deporte8, onvalue = 1,
                          offvalue = 0, width=20).place(x=700, y=160)
c59 = tkinter.Checkbutton(quiz_anime, text = "skate", indicatoron=0,
                          variable = deporte9, onvalue = 1,
                          offvalue = 0, width=20).place(x=700, y=180)
c510 = tkinter.Checkbutton(quiz_anime, text = "ningun deporte", indicatoron=0,
                          variable = deporte10, onvalue = 1,
                          offvalue = 0, width=20).place(x=700, y=200)
"""
Una vez esten hechas las funciones se podran compilar las opciones
y teniendo animes que tengan un rango dependiendo de cada pregunta
asi sabien que programas son mas compatibles con las opciones
siendo que se van a dividir en peliculas y series
se creará un rango en las opciones para que sea mas amplia la gama 
Abajo se demuestra un ejemplo de como seria un resultado en concreto
"""
#----------------------------------------------------------------------------------
def resultado ():
#----------------------------------------------------------------------------------
"""
Aqui se encuentran algunas de las opciones que
pueden salir al completar el quiz
se van a añadir más de poco a poco
ya que son opciones excatas para que sean
compatibles con las elecciones
"""
#El Viaje de Chihiro
    if ((((formato.get() == 0))
        and (cantidad.get() == 4)
        and ((romance.get() == 1) and (aventura.get() == 1))
        and ((isekai.get() == 1) and (superpoderes.get() == 1))
        and (ningun.get() == 1))):
        chihiro = tkinter.Label(quiz_anime, text = "Deberias ver: << El Viaje de Chihiro >>")
        chihiro.pack(anchor="w")

#El Castillo Vagabundo
    if ((((formato.get() == 0))
        and (cantidad.get() == 4)
        and ((romance.get() == 1) and (aventura.get() == 1))
        and ((shoujo.get() == 1) and (superpoderes.get() == 1))
        and (ningun.get() == 1))):
        ecv = tkinter.Label(quiz_anime, text = "Deberias ver: << El Castillo Vagabundo >>")
        ecv.pack(anchor="w")

#I wanna eat your pancreas
    elif ((((formato.get() == 0))
        and (cantidad.get() == 4)
        and ((drama.get() == 1) and (romance.get() == 1))
        and ((slice_of_life.get() == 1) and (josei.get() == 1))
        and (ningun.get() == 1))):
        iweyp = tkinter.Label(quiz_anime, text = "Deberias ver: << I wanna eat your pancreas >>")
        iweyp.pack(anchor="w")

#Umibe no Etranger
    elif ((((formato.get() == 0))
        and (cantidad.get() == 4)
        and ((drama.get() == 1) and (romance.get() == 1))
        and ((slice_of_life.get() == 1) and (bl.get() == 1))
        and (ningun.get() == 1))):
        une = tkinter.Label(quiz_anime, text = "Deberias ver: << Umibe no Etranger >>")
        une.pack(anchor="w")

#----------------------------------------------------------------------------------

#Demon Slayer
    elif (((formato.get() == 1))
        and ((cantidad.get() == 2 or (cantidad.get() == 3))
        and ((accion.get() == 1) and (aventura.get() == 1))
        and ((shounen.get() == 1) and (superpoderes.get() == 1)
             and (gore.get() == 1))
        and (ningun.get() == 1))):
        demon = tkinter.Label(quiz_anime, text = "Deberias ver: << Demon Slayer >>")
        demon.pack(anchor="w")

#Chainsaw Man
    elif (((formato.get() == 1))
        and ((cantidad.get() == 0 or (cantidad.get() == 3))
        and ((accion.get() == 1) and (terror.get() == 1))
        and ((shounen.get() == 1) and (superpoderes.get() == 1)
             and (gore.get() == 1))
        and (ningun.get() == 1))):
        chainsaw = tkinter.Label(quiz_anime, text = "Deberias ver: << Chainsaw Man >>")
        chainsaw.pack(anchor="w")

#My Hero Academia
    elif (((formato.get() == 1))
        and ((cantidad.get() == 2 or (cantidad.get() == 3))
        and ((accion.get() == 1) and (aventura.get() == 1))
        and ((shounen.get() == 1) and (superpoderes.get() == 1)
             and (escolar.get() == 1))
        and (ningun.get() == 1))):
        mha = tkinter.Label(quiz_anime, text = "Deberias ver: << My Hero Academia >>")
        mha.pack(anchor="w")

#Spy X Family
    elif (((formato.get() == 1))
        and ((cantidad.get() == 1 or (cantidad.get() == 3))
        and ((accion.get() == 1) and (comedia.get() == 1))
        and ((shounen.get() == 1) and (superpoderes.get() == 1)
             and (slice_of_life.get() == 1))
        and (ningun.get() == 1))):
        sxf = tkinter.Label(quiz_anime, text = "Deberias ver: << Spy X Family >>")
        sxf.pack(anchor="w")

#Sasaki to Miyano
    elif (((formato.get() == 1))
        and ((cantidad.get() == 0 or (cantidad.get() == 3))
        and ((romance.get() == 1) and (comedia.get() == 1))
        and ((bl.get() == 1) and (escolar.get() == 1)
             and (slice_of_life.get() == 1))
        and (ningun.get() == 1))):
        stm = tkinter.Label(quiz_anime, text = "Deberias ver: << Sasaki to Miyano >>")
        stm.pack(anchor="w")

#Komi Can't Communicate
    elif (((formato.get() == 1))
        and ((cantidad.get() == 1 or (cantidad.get() == 3))
        and ((romance.get() == 1) and (comedia.get() == 1))
        and ((josei.get() == 1) and (escolar.get() == 1)
             and (slice_of_life.get() == 1))
        and (ningun.get() == 1))):
        stm = tkinter.Label(quiz_anime, text = "Deberias ver: << Komi Can't Communicate >>")
        stm.pack(anchor="w")

#Banana Fish
    elif (((formato.get() == 1))
        and ((cantidad.get() == 1 or (cantidad.get() == 3))
        and ((romance.get() == 1) and (drama.get() == 1))
        and ((bl.get() == 1) and (seinen.get() == 1)
             and (gore.get() == 1))
        and (ningun.get() == 1))):
        bf = tkinter.Label(quiz_anime, text = "Deberias ver: << Banana Fish >>")
        bf.pack(anchor="w")

#No.6
    elif (((formato.get() == 1))
        and ((cantidad.get() == 0 or (cantidad.get() == 3))
        and ((misterio.get() == 1) and (drama.get() == 1))
        and ((bl.get() == 1) and (seinen.get() == 1)
             and (seinen.get() == 1))
        and (ningun.get() == 1))):
        no6 = tkinter.Label(quiz_anime, text = "Deberias ver: << No.6 >>")
        no6.pack(anchor="w")

#Magical Girl Ore
    elif (((formato.get() == 1))
        and ((cantidad.get() == 0 or (cantidad.get() == 3))
        and ((accion.get() == 1) and (comedia.get() == 1))
        and ((shoujo.get() == 1) and (superpoderes.get() == 1)
             and (gl.get() == 1))
        and (ningun.get() == 1))):
        mgo = tkinter.Label(quiz_anime, text = "Deberias ver: << Magical Girl Ore >>")
        mgo.pack(anchor="w")

#How to keep a Mummy
    elif (((formato.get() == 1))
        and ((cantidad.get() == 0 or (cantidad.get() == 3))
        and ((ciencia_ficcion.get() == 1) and (comedia.get() == 1))
        and ((josei.get() == 1) and (superpoderes.get() == 1)
             and (slice_of_life.get() == 1))
        and (ningun.get() == 1))):
        htkam = tkinter.Label(quiz_anime, text = "Deberias ver: << How to keep a Mummy >>")
        htkam.pack(anchor="w")

#Zombieland Saga
    elif (((formato.get() == 1))
        and ((cantidad.get() == 1 or (cantidad.get() == 3))
        and ((terror.get() == 1) and (comedia.get() == 1))
        and ((josei.get() == 1) and (gore.get() == 1)
             and (slice_of_life.get() == 1))
        and (ningun.get() == 1))):
        zs = tkinter.Label(quiz_anime, text = "Deberias ver: << Zombieland Saga >>")
        zs.pack(anchor="w")

#Corpse Party
    elif (((formato.get() == 1))
        and ((cantidad.get() == 0 or (cantidad.get() == 3))
        and ((terror.get() == 1) and (misterio.get() == 1))
        and ((isekai.get() == 1) and (gore.get() == 1)
             and (escolar.get() == 1))
        and (ningun.get() == 1))):
        cp = tkinter.Label(quiz_anime, text = "Deberias ver: << Corpse Party >>")
        cp.pack(anchor="w")

#Kotaro vive solo
    elif (((formato.get() == 1))
        and ((cantidad.get() == 0 or (cantidad.get() == 3))
        and ((comedia.get() == 1) and (drama.get() == 1))
        and ((josei.get() == 1) and (escolar.get() == 1)
             and (slice_of_life.get() == 1))
        and (ningun.get() == 1))):
        kvs = tkinter.Label(quiz_anime, text = "Deberias ver: << Kotaro vive solo >>")
        kvs.pack(anchor="w")


#----------------------------------------------------------------------------------

#Free
    elif (((formato.get() == 1))
        and ((cantidad.get() == 1 or (cantidad.get() == 3))
        and ((accion.get() == 1) or (comedia.get() == 1))
        and ((shounen.get() == 1) or (escolar.get() == 1)
             or (slice_of_life.get() == 1))
        and (natacion.get() == 1))):
        free = tkinter.Label(quiz_anime, text = "Deberias ver: << Free >>")
        free.pack(anchor="w")

#Sk8 the Infinity
    elif (((formato.get() == 1))
        and ((cantidad.get() == 0 or (cantidad.get() == 3))
        and ((accion.get() == 1) or (comedia.get() == 1))
        and ((bl.get() == 1) or (shounen.get() == 1)
             or (slice_of_life.get() == 1))
        and (skate.get() == 1))):
        sk8 = tkinter.Label(quiz_anime, text = "Deberias ver: << Sk8 the Infinity >>")
        sk8.pack(anchor="w")

#----------------------------------------------------------------------------------
    else:
        malo = tkinter.Label(quiz_anime, text = "No hay recomendaciones aun")
        malo.pack(anchor="w")
#----------------------------------------------------------------------------------
espacio1 = tkinter.Label(quiz_anime, text=' ', bg='white').pack(anchor="w")
espacio2 = tkinter.Label(quiz_anime, text=' ', bg='white').pack(anchor="w")
espacio3 = tkinter.Label(quiz_anime, text=' ', bg='white').pack(anchor="w")
espacio4 = tkinter.Label(quiz_anime, text=' ', bg='white').pack(anchor="w")
espacio5 = tkinter.Label(quiz_anime, text=' ', bg='white').pack(anchor="w")
espacio6 = tkinter.Label(quiz_anime, text=' ', bg='white').pack(anchor="w")
espacio7 = tkinter.Label(quiz_anime, text=' ', bg='white').pack(anchor="w")
espacio8 = tkinter.Label(quiz_anime, text=' ', bg='white').pack(anchor="w")
espacio9 = tkinter.Label(quiz_anime, text=' ', bg='white').pack(anchor="w")
espacio10 = tkinter.Label(quiz_anime, text=' ', bg='white').pack(anchor="w")
espacio11 = tkinter.Label(quiz_anime, text=' ', bg='white').pack(anchor="w")
#----------------------------------------------------------------------------------
boton_final = tkinter.Button(quiz_anime, text = "resultados", command=resultado)
boton_final.pack()
espacio12 = tkinter.Label(quiz_anime, text=' ', bg='white').pack(anchor="w")

quiz_anime.mainloop()
