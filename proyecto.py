"""
Proyecto Quiz de Anime
Test en el cual puedes encontrar un nuevo anime para ver
Va a ser una pantalla extra (tkinter)
Las preguntas dos seran radiobutton y otras dos checkbutton
Cada respuesta a elegir sera una variable diferente
Y dependiendo las eleccion se desplegara el mejor resultado
"""

#bibliotecas
import tkinter
quiz_anime = tkinter.Tk()
quiz_anime.configure(bg="white")
quiz_anime.geometry("1800x750")
quiz_anime.title("Quiz Anime")

"""
================== funciones de preguntas 1 y 2  =====================================
"""

def formatos (eleccion1):
    """
    (uso listas, uso funciones)
    recibe: eleccion1 (lista)
    toma la lista y la vuelve radiobuttons
    devuelve: radiobuttons con los valores de la lista
    """
    for i in range(len(eleccion1)):
        radiobutton1 = tkinter.Radiobutton(
            quiz_anime, text= eleccion1[i],
            variable = formato,indicatoron=0,
            value=i, width=10,
            font=('Arial',9)
            ).pack(anchor="w")

def cantidades (eleccion2):
    """
    (uso listas, uso funciones)
    recibe: eleccion2 (lista)
    toma la lista y la vuelve radiobuttons
    devuelve: radiobuttons con los valores de la lista
    """
    for i in range(len(eleccion2)):
        radiobutton2 = tkinter.Radiobutton(
            quiz_anime, text= eleccion2[i],
            variable = cantidad,indicatoron=0,
            value=i, width=20,
            font=('Arial',9)
            ).pack(anchor="w")

def orden (lista):
    """
    (uso ciclos, uso funciones)
    recibe: recoms y recom (listas anidadas)
    toma la lista y la imprime junto con un
    guion al inicio
    """
    i = 0
    while i < len(lista):
        print("-",lista[i])
        i = i + 1
"""
================== funcion de resultados  =====================================
"""


def resultado ():
    """
    (uso condicionales, uso funciones)
    recibe: ningun valor ya que va ligado a un boton
    toma todos los condicionales para usarlos junto con el boton
    los valores en los condicionales son de cada boton del quiz
    devuelve: el texto de la eleccion que se relaciona mas
    a lo elegido en los checkbuttons y radiobuttons
    """

#--------------- Area Peliculas -------------------------------

    if (formato.get() == 0) and (cantidad.get() == 4):
#El Castillo Vagabundo
        if (
            ((romance.get() == 1) and (aventura.get() == 1))
            and ((shoujo.get() == 1) or (superpoderes.get() == 1))):
            ecv = tkinter.Label(quiz_anime,
                                text = "Deberias ver:"
                                " << El Castillo Vagabundo >>")
            ecv.pack(anchor="w")

#El Viaje de Chihiro
        elif (
            ((romance.get() == 1) and (aventura.get() == 1))
            and ((isekai.get() == 1) or (superpoderes.get() == 1))):
            chihiro = tkinter.Label(quiz_anime,
                                    text = "Deberias ver:"
                                    " << El Viaje de Chihiro >>")
            chihiro.pack(anchor="w")

#I wanna eat your pancreas
        elif (
            ((drama.get() == 1) and (romance.get() == 1))
            and ((slice_of_life.get() == 1) or (josei.get() == 1))):
            iweyp = tkinter.Label(quiz_anime,
                                  text = "Deberias ver:"
                                  " << I wanna eat your pancreas >>")
            iweyp.pack(anchor="w")

#Ponyo
        elif (
            ((drama.get() == 1) and (ciencia_ficcion.get() == 1))
            and ((slice_of_life.get() == 1) or (superpoderes.get() == 1))):
            ponyo = tkinter.Label(quiz_anime,
                                  text = "Deberias ver:"
                                  " << Ponyo >>")
            ponyo.pack(anchor="w")

#Umibe no Etranger
        elif (
            ((drama.get() == 1) and (romance.get() == 1))
            and ((slice_of_life.get() == 1) or (bl.get() == 1))):
            une = tkinter.Label(quiz_anime, text = "Deberias ver:"
                                " << Umibe no Etranger >>")
            une.pack(anchor="w")

#Princesa Mononoke
        elif (
            ((drama.get() == 1) and (aventura.get() == 1))
            and ((superpoderes.get() == 1) or (shoujo.get() == 1))):
            pm = tkinter.Label(quiz_anime, text = "Deberias ver:"
                                " << Princesa Mononoke >>")
            pm.pack(anchor="w")

#Mi vecino Totoro
        elif (
            ((ciencia_ficcion.get() == 1) and (aventura.get() == 1))
            and ((superpoderes.get() == 1) or (slice_of_life.get() == 1))):
            mvt = tkinter.Label(quiz_anime, text = "Deberias ver:"
                                " << Mi vecino Totoro >>")
            mvt.pack(anchor="w")

#Your Name
        elif (
            ((ciencia_ficcion.get() == 1) and (romance.get() == 1))
            and ((shoujo.get() == 1) or (josei.get() == 1))):
            yn = tkinter.Label(quiz_anime, text = "Deberias ver:"
                                " << Your Name >>")
            yn.pack(anchor="w")

        else:
            els2 = tkinter.Label(quiz_anime, text = "Aun no se añade"
                                " algun anime con esa descripcion."
                                " Vuelve a intentar")
            els2.pack(anchor="w")
            
#--------------- Area Series -------------------------------

#Banana Fish
    elif (formato.get() == 1):
        if (
            ((cantidad.get() == 1 or (cantidad.get() == 3))
            and ((romance.get() == 1) and (drama.get() == 1))
            and ((bl.get() == 1) or (seinen.get() == 1)))):
            bf = tkinter.Label(quiz_anime, text = "Deberias ver:"
                               " << Banana Fish >>")
            bf.pack(anchor="w")

#Chainsaw Man
        elif (
            ((cantidad.get() == 0 or (cantidad.get() == 3))
            and ((accion.get() == 1) and (terror.get() == 1))
            and ((shounen.get() == 1) or (gore.get() == 1)))):
            chainsaw = tkinter.Label(quiz_anime, text = "Deberias ver:"
                                     " << Chainsaw Man >>")
            chainsaw.pack(anchor="w")

#Corpse Party
        elif (
            ((cantidad.get() == 0 or (cantidad.get() == 3))
            and ((terror.get() == 1) and (misterio.get() == 1))
            and ((gore.get() == 1) or (escolar.get() == 1)))):
            cp = tkinter.Label(quiz_anime, text = "Deberias ver:"
                               " << Corpse Party >>")
            cp.pack(anchor="w")

#Demon Slayer
        elif (
            ((cantidad.get() == 2 or (cantidad.get() == 3))
            and ((accion.get() == 1) and (aventura.get() == 1))
            and ((shounen.get() == 1) or (gore.get() == 1)))):
            demon = tkinter.Label(quiz_anime, text = "Deberias ver:"
                                  " << Demon Slayer >>")
            demon.pack(anchor="w")

#Free
        elif (
            ((cantidad.get() == 2 or (cantidad.get() == 3))
            and ((deporte.get() == 1) and (comedia.get() == 1))
            and ((escolar.get() == 1) or (slice_of_life.get() == 1)))):
            free = tkinter.Label(quiz_anime, text = "Deberias ver:"
                                 " << Free >>")
            free.pack(anchor="w")

#How to keep a Mummy
        elif (
            ((cantidad.get() == 0 or (cantidad.get() == 3))
            and ((ciencia_ficcion.get() == 1) and (comedia.get() == 1))
            and ((superpoderes.get() == 1) or (slice_of_life.get() == 1)))):
            htkam = tkinter.Label(quiz_anime, text = "Deberias ver:"
                                  " << How to keep a Mummy >>")
            htkam.pack(anchor="w")

#Hunter X Hunter
        elif (
            ((cantidad.get() == 2 or (cantidad.get() == 3))
            and ((accion.get() == 1) and (drama.get() == 1))
            and ((shounen.get() == 1) or (superpoderes.get() == 1)))):
            hxh = tkinter.Label(quiz_anime, text = "Deberias ver:"
                                " << Hunter X Hunter >>")
            hxh.pack(anchor="w")

#Jobless Reincarnation
        elif (
            ((cantidad.get() == 2 or (cantidad.get() == 3))
            and ((accion.get() == 1) and (ciencia_ficcion.get() == 1))
            and ((isekai.get() == 1) or (seinen.get() == 1)))):
            jr = tkinter.Label(quiz_anime, text = "Deberias ver:"
                               " << Jobless Reincarnation >>")
            jr.pack(anchor="w")

#Komi Can't Communicate
        elif (
            ((cantidad.get() == 1 or (cantidad.get() == 3))
            and ((romance.get() == 1) and (comedia.get() == 1))
            and ((josei.get() == 1) or (escolar.get() == 1)))):
            stm = tkinter.Label(quiz_anime, text = "Deberias ver:"
                                " << Komi Can't Communicate >>")
            stm.pack(anchor="w")

#Kotaro vive solo
        elif (
            ((cantidad.get() == 0 or (cantidad.get() == 3))
            and ((comedia.get() == 1) and (drama.get() == 1))
            and ((josei.get() == 1) or (slice_of_life.get() == 1)))):
            kvs = tkinter.Label(quiz_anime, text = "Deberias ver:"
                                " << Kotaro vive solo >>")
            kvs.pack(anchor="w")

#Magical Girl Ore
        elif (
            ((cantidad.get() == 0 or (cantidad.get() == 3))
            and ((accion.get() == 1) and (comedia.get() == 1))
            and ((superpoderes.get() == 1) or (gl.get() == 1)))):
            mgo = tkinter.Label(quiz_anime, text = "Deberias ver:"
                                " << Magical Girl Ore >>")
            mgo.pack(anchor="w")

#My Hero Academia
        elif (
            ((cantidad.get() == 2 or (cantidad.get() == 3))
            and ((accion.get() == 1) and (aventura.get() == 1))
            and ((superpoderes.get() == 1) or (escolar.get() == 1)))):
            mha = tkinter.Label(quiz_anime, text = "Deberias ver:"
                                " << My Hero Academia >>")
            mha.pack(anchor="w")

#No.6
        elif (
            ((cantidad.get() == 0 or (cantidad.get() == 3))
            and ((misterio.get() == 1) and (drama.get() == 1))
            and ((bl.get() == 1) or (seinen.get() == 1)))):
            no6 = tkinter.Label(quiz_anime, text = "Deberias ver:"
                                " << No.6 >>")
            no6.pack(anchor="w")

#Sasaki to Miyano
        elif (
            ((cantidad.get() == 0 or (cantidad.get() == 3))
            and ((romance.get() == 1) and (comedia.get() == 1))
            and ((bl.get() == 1) or (escolar.get() == 1)))):
            stm = tkinter.Label(quiz_anime, text = "Deberias ver:"
                                " << Sasaki to Miyano >>")
            stm.pack(anchor="w")

#Sk8 the Infinity
        elif (
            ((cantidad.get() == 0 or (cantidad.get() == 3))
            and ((deporte.get() == 1) and (comedia.get() == 1))
            and ((bl.get() == 1) or (slice_of_life.get() == 1)))):
            sk8 = tkinter.Label(quiz_anime, text = "Deberias ver:"
                                " << Sk8 the Infinity >>")
            sk8.pack(anchor="w")

#Spy X Family
        elif (
            ((cantidad.get() == 1 or (cantidad.get() == 3))
            and ((accion.get() == 1) and (comedia.get() == 1))
            and ((shounen.get() == 1) or (slice_of_life.get() == 1)))):
            sxf = tkinter.Label(quiz_anime, text = "Deberias ver:"
                                " << Spy X Family >>")
            sxf.pack(anchor="w")

#Your Lie in April
        elif (
            ((cantidad.get() == 1 or (cantidad.get() == 3))
            and ((romance.get() == 1) and (drama.get() == 1))
            and ((shoujo.get() == 1) or (josei.get() == 1)))):
            ylia = tkinter.Label(quiz_anime, text = "Deberias ver:"
                                 " << Your Lie in April >>")
            ylia.pack(anchor="w")

#Zombieland Saga
        elif (
            ((cantidad.get() == 1 or (cantidad.get() == 3))
            and ((terror.get() == 1) and (comedia.get() == 1))
            and ((josei.get() == 1) or (gore.get() == 1)))):
            zs = tkinter.Label(quiz_anime, text = "Deberias ver:"
                               " << Zombieland Saga >>")
            zs.pack(anchor="w")

#Re Zero
        elif (
            ((cantidad.get() == 2 or (cantidad.get() == 3))
            and ((accion.get() == 1) and (ciencia_ficcion.get() == 1))
            and ((isekai.get() == 1) or (gore.get() == 1)))):
            rz = tkinter.Label(quiz_anime, text = "Deberias ver:"
                               " << Re Zero >>")
            rz.pack(anchor="w")

#One Piece
        elif (
            ((cantidad.get() == 2 or (cantidad.get() == 3))
            and ((accion.get() == 1) and (aventura.get() == 1))
            and ((shounen.get() == 1) or (superpoderes.get() == 1)))):
            op = tkinter.Label(quiz_anime, text = "Deberias ver:"
                               " << One Piece >>")
            op.pack(anchor="w")

#Beastars
        elif (
            ((cantidad.get() == 1 or (cantidad.get() == 3))
            and ((romance.get() == 1) and (drama.get() == 1))
            and ((escolar.get() == 1) or (slice_of_life.get() == 1)))):
            bst = tkinter.Label(quiz_anime, text = "Deberias ver:"
                               " << Beastars >>")
            bst.pack(anchor="w")

#Haikyuu!
        elif (
            ((cantidad.get() == 2 or (cantidad.get() == 3))
            and ((deporte.get() == 1) and (comedia.get() == 1))
            and ((escolar.get() == 1) or (shounen.get() == 1)))):
            hk = tkinter.Label(quiz_anime, text = "Deberias ver:"
                               " << Haikyuu! >>")
            hk.pack(anchor="w")

#Attack on Titan
        elif (
            ((cantidad.get() == 2 or (cantidad.get() == 3))
            and ((drama.get() == 1) and (accion.get() == 1))
            and ((gore.get() == 1) or (shounen.get() == 1)))):
            aot = tkinter.Label(quiz_anime, text = "Deberias ver:"
                               " << Attack on Titan >>")
            aot.pack(anchor="w")

#Way of the House husband
        elif (
            ((cantidad.get() == 0 or (cantidad.get() == 3))
            and ((comedia.get() == 1) and (romance.get() == 1))
            and ((slice_of_life.get() == 1) or (josei.get() == 1)))):
            wothh = tkinter.Label(quiz_anime, text = "Deberias ver:"
                               " << Way of the House husband>>")
            wothh.pack(anchor="w")

#Danganronpa
        elif (
            ((cantidad.get() == 2 or (cantidad.get() == 3))
            and ((terror.get() == 1) and (misterio.get() == 1))
            and ((escolar.get() == 1) or (gore.get() == 1)))):
            dgrp = tkinter.Label(quiz_anime, text = "Deberias ver:"
                               " << Danganronpa >>")
            dgrp.pack(anchor="w")

#Mob Psycho 100
        elif (
            ((cantidad.get() == 1 or (cantidad.get() == 3))
            and ((comedia.get() == 1) and (accion.get() == 1))
            and ((slice_of_life.get() == 1) or (superpoderes.get() == 1)))):
            mp = tkinter.Label(quiz_anime, text = "Deberias ver:"
                               " << Mob Psycho 100 >>")
            mp.pack(anchor="w")

#Saiki K
        elif (
            ((cantidad.get() == 2 or (cantidad.get() == 3))
            and ((comedia.get() == 1) and (ciencia_ficcion.get() == 1))
            and ((slice_of_life.get() == 1) or (superpoderes.get() == 1)))):
            sk = tkinter.Label(quiz_anime, text = "Deberias ver:"
                               " << Saiki K >>")
            sk.pack(anchor="w")

#The Promise Nerverland
        elif (
            ((cantidad.get() == 1 or (cantidad.get() == 3))
            and ((aventura.get() == 1) and (terror.get() == 1))
            and ((gore.get() == 1) or (shounen.get() == 1)))):
            tpn = tkinter.Label(quiz_anime, text = "Deberias ver:"
                               " << The Promise Nerverland >>")
            tpn.pack(anchor="w")

#Jujutsu Kaisen
        elif (
            ((cantidad.get() == 0 or (cantidad.get() == 3))
            and ((accion.get() == 1) and (terror.get() == 1))
            and ((gore.get() == 1) or (shounen.get() == 1)))):
            jk = tkinter.Label(quiz_anime, text = "Deberias ver:"
                               " << Jujutsu Kaisen >>")
            jk.pack(anchor="w")

#Naruto
        elif (
            ((cantidad.get() == 2 or (cantidad.get() == 3))
            and ((accion.get() == 1) and (aventura.get() == 1))
            and ((shounen.get() == 1) or (superpoderes.get() == 1)))):
            nt = tkinter.Label(quiz_anime, text = "Deberias ver:"
                               " << Naruto >>")
            nt.pack(anchor="w")

        else:
            els = tkinter.Label(quiz_anime, text = "Aun no se añade"
                                " algun anime con esa descripcion."
                                " Vuelve a intentar")
            els.pack(anchor="w")

"""
========  parte principal del programa ========================================
"""

# Area de la consola

print("\nPeliculas:")
recom = [
    ["El Castillo Vagabundo"],["El Viaje de Chihiro"],
    ["I wanna eat your pancreas"],["Ponyo"],["Umibe no Etranger"],
    ["Princesa Mononoke"],["Mi vecino Totori"],
    ["Your Name"]
    ]

# Ciclo de listas anidadas
recom.sort()

orden(recom)

print("\nSeries:")  
recoms = [
    ["Banana Fish"],["Chainsaw Man"],["Corpse Party"],
    ["Demon Slayer"],["Free"],["How to keep a Mummy"],
    ["Hunter X Hunter"],["Jobless Reincarnation"],
    ["Komi Cant Communicate"],["Kotaro vive solo"],["Magical Girl Ore"],
    ["My Hero Academia"],["No.6"],["Sasaki to Miyano"],
    ["Sk8 the Infinity"],["Spy X Family "],["Your Lie in April"],
    ["Zombieland Saga"],["Re Zero"],["One Piece"],
    ["Beastars"],["Haikyuu!"],["Attack on titan"],
    ["Way of the House husband"],["Danganronpa"],
    ["Mob Psycho 100"],["Saiki K"],["The Promise Neverland"],
    ["Jujutsu Kaisen"],["Naruto"]
    ]

recoms.sort()

orden(recoms)

#Area de tkinter
    
eleccion1 = ["Pelicula", "Serie"]
eleccion2 = ["1 a 18","19 a 29","Más de 30",
             "Sin importar la cantidad", "Elegí pelicula"]

#Texto inical
parte1 = tkinter.Label(
    quiz_anime,
    text="Bienvenidxs a este <<Quiz de Anime>>",
    bg="white", font=('Comic Sans MS',20)).pack()

parte15 = tkinter.Label(
    quiz_anime,
    text="Este Quiz es para darte una recomendacion de"
    " que Anime deberias ver, basandose en"
    " las respuestas que elijas."
    " Hay una lista de animes en el tablero de Python",
    bg="white", font=('Comic Sans MS',12)).pack(anchor="w")

parte2 = tkinter.Label(
    quiz_anime,
    text="Lee las instrucciones y contesta las preguntas."
    " Si no aparece ningun resultado es por que aun"
    " no hay alguna recomendacion con esa descripcion",
    bg="white", font=('Comic Sans MS',12)).pack(anchor="w")

espacio = tkinter.Label(quiz_anime, text=' ', bg='white').pack(anchor="w")

#Preguntas

#Pregunta 1
text2 = tkinter.Label(
    quiz_anime,
    text="¿Que formato prefieres: pelicula, serie?",
    bg="white", font=('Arial',12,'bold')).pack(anchor="w")

formato = tkinter.IntVar()

pregunta1 = formatos(eleccion1)

#Pregunta 2
text3 = tkinter.Label(
    quiz_anime,
    text="¿Que cantidad de capitulos prefieres?",
    bg="white", font=('Arial',12,'bold')).pack(anchor="w")

cantidad = tkinter.IntVar()

pregunta2 = cantidades (eleccion2)

#Pregunta 3
text4 = tkinter.Label(
    quiz_anime,
    text="¿Que genero prefieres? (escoge 2)",
    bg="white", font=('Arial',12,'bold')).place(x=390, y=120)

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

#Pregunta 4
text5 = tkinter.Label(
    quiz_anime,
    text="¿Que genero de anime prefieres? (escoge 2)",
    bg="white", font=('Arial',12,'bold')).place(x=790, y=120)

shounen = tkinter.IntVar()
isekai = tkinter.IntVar()
superpoderes = tkinter.IntVar()
bl = tkinter.IntVar()
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

c43 = tkinter.Checkbutton(quiz_anime, text = "Superpoderes / Magia",
                          indicatoron=0,
                          variable = superpoderes, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=800, y=195)

c44 = tkinter.Checkbutton(quiz_anime, text = "BL", indicatoron=0,
                          variable = bl, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=800, y=220)

c45 = tkinter.Checkbutton(quiz_anime, text = "Shoujo", indicatoron=0,
                          variable = shoujo, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=800, y=245)

c46 = tkinter.Checkbutton(quiz_anime, text = "Escolar", indicatoron=0,
                          variable = escolar, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=800, y=270)

c47 = tkinter.Checkbutton(quiz_anime, text = "Slice of life", indicatoron=0,
                          variable = slice_of_life, onvalue = 1,
                          offvalue = 0, width=20,
                          font=('Arial',9)).place(x=800, y=295)

c48 = tkinter.Checkbutton(quiz_anime, text = "Josei", indicatoron=0,
                          variable = josei, onvalue = 1,
                          offvalue = 0, width=20,
                           font=('Arial',9)).place(x=800, y=320)

c49 = tkinter.Checkbutton(quiz_anime, text = "Seinen", indicatoron=0,
                          variable = seinen, onvalue = 1,
                          offvalue = 0, width=20,
                           font=('Arial',9)).place(x=800, y=345)

c410 = tkinter.Checkbutton(quiz_anime, text = "Gore", indicatoron=0,
                          variable = gore, onvalue = 1,
                          offvalue = 0, width=20,
                           font=('Arial',9)).place(x=800, y=370)

#Texto de explicacion de cada genero
ex1 = tkinter.Label(
    quiz_anime,
    text="- Shounen: creacion dirigida a un publico masculino juvenil",
    bg="white", font=('Arial',9)).place(x=975, y=145)

ex2 = tkinter.Label(
    quiz_anime,
    text="- Isekai: viaje a un mundo desconocido",
    bg="white", font=('Arial',9)).place(x=975, y=170)

ex3 = tkinter.Label(
    quiz_anime,
    text="- Superpoderes / Magia: que los personajes"
    " tengan al gun tipo de poder o magia",
    bg="white", font=('Arial',9)).place(x=975, y=195)

ex4 = tkinter.Label(
    quiz_anime,
    text="- BL: un romance entre dos hombres",
    bg="white", font=('Arial',9)).place(x=975, y=220)

ex5 = tkinter.Label(
    quiz_anime,
    text="- Shoujo: creacion dirigida a un publico femenino juvenil",
    bg="white", font=('Arial',9)).place(x=975, y=245)

ex6 = tkinter.Label(
    quiz_anime,
    text="- Escolar: historia que se desarolla"
    " principalmente en una escuela",
    bg="white", font=('Arial',9)).place(x=975, y=270)

ex7 = tkinter.Label(
    quiz_anime,
    text="- Slice of life: recuentos de la vida"
    " diaria de los personajes principales",
    bg="white", font=('Arial',9)).place(x=975, y=295)

ex8 = tkinter.Label(
    quiz_anime,
    text="- Josei: creacion dirigida a"
    " un publico femenino adulto",
    bg="white", font=('Arial',9)).place(x=975, y=320)

ex9 = tkinter.Label(
    quiz_anime,
    text="- Seinen: creacion dirigida a"
    " un publico masculino adulto",
    bg="white", font=('Arial',9)).place(x=975, y=345)

ex10 = tkinter.Label(
    quiz_anime,
    text="- Gore: obras en las cuales se presentan"
    " escenarios explicitos (sangre/organos)",
    bg="white", font=('Arial',9)).place(x=975, y=370)

i=0
while i < 5 :
    espacio = tkinter.Label(
        quiz_anime, text=' ', bg='white').pack(anchor="w")
    i = i+1

#Boton final
boton_final = tkinter.Button(
    quiz_anime, text = "Resultados",
    bg="#EFB8FF", command=resultado,
    font=('Arial',16)).place(x=700, y=410)

espacio13 = tkinter.Label(quiz_anime, text=' ', bg='white').pack(anchor="w")

quiz_anime.mainloop()
