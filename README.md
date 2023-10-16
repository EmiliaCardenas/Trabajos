# Quiz de ANIME

Un test para saber que anime(s) serían los más recomendados para ver conforme a tus gustos y actividades.

### Contexto

La importancia de este proyecto es poder brindar ideas de qué ver. ¿Por qué esto es importante? Hay varias razones; empezando por la liberación de dopamina, ya que relacionamos la idea de descansar con una recompensa para nuestro cerebro. Es una manera de separarse de la rutina, creando un momento de liberación y relajación que a veces no se obtiene a diario. Sirve para la socialización, al tener un tema en común el cual se puede compartir con más personas, generando nuevos lazos. Se pueden liberar sentimientos, generando empatía, odio, amor, tristeza, etc. por algún personaje. Generando nuevas sensaciones y de cierta manera, pudiendo ser parte de ese universo. Las creaciones audiovisuales en su mayoría tiene lecciones, algunas buenas y otras son lo contrario, pero en si intenta enseñarle algo al espectador. Siendo que si se ve un impacto positivo por esas lecciones, el espectador puede implementarlas en su vida diaria. Los espectadores se pueden sentir seguros al verlas, haciendo que sentimientos como estrés o ansiedad se disipen por un rato, teniendo así un mejor estado de ánimo. Esas serían las principales razones por las cuales es bueno despejarse y tener tiempo para ver un contenido audio visual.
Morales A. (2021). Los beneficios emocionales que tiene ver una serie, según los psicólogos. Vogue Spain. https://www.vogue.es/belleza/articulos/ver-una-serie-beneficios-emocionales-psicologos-netflix-amazon#:~:text=Nos%20protege%20frente%20al%20estado,la%20ansiedad%20y%20el%20estr%C3%A9s.

¿Por qué específicamente anime? Al ser un producto animado tiene más libertades a la hora de hacer un mundo fantástico o con algún elemento fuera de lo habitual, aunque también los animes de la vida ordinaria tienen su encanto. Al ser una animación diferente a la occidental obtiene un encanto particular, aparte que en la cultura japonesa está más normalizado que la animación no tiene edad mínima ni máxima. Aunque hay animación en este lado del mundo, es más común que sea para una audiencia infantil; mientras que en Japón y el área Oriental, la animación puede haber para varios tipos de público.

### Explicación

Inicia con una pestaña de tkinter, la cual es una biblioteca que abre una ventana extra, en la cual el usuario puede interactuar.
Teniendo como base varias preguntas,  dependiendo de las elecciones del usuario y si coinciden con sus intereses. Sería recolectar una suma o resta de datos, dependiendo de las opciones elegidas. Cada pregunta tendrá sus números por separado (no mezclando las sumas o restas de otras preguntas), al final de tener todas las respuestas se comprarán con los datos de cada anime dependiendo las preguntas, intentando al final encontrar las mejores recomendaciones, acorde a lo seleccionado. Las preguntas pueden ser por ejempo:

- Los géneros de gusto del usuario (Misterio, Thriller, Acción, Romance, etc).
- Los géneros relacionados al anime del gusto del usuario (Shounen, Shoujo, Josei, Mecha, etc.)
- La cantidad aceptada de episodios (12, 24, 30<, etc.)
- Si prefiere pelicula o serie

Eso sería un ejemplo de lo que puede tener el quiz, el cual tendrá una amplia gama de opciones de animes.

### Correcciones

        """
        Sub-Competencia: Separa el código en funciones pequeñas reusables,
        haciendo uso correcto de paso por parametros y return
        
        Error original: No se evidenciaba en donde se usaban las funciones
                def formato (radiobutton1):
                    if radiobutton1 == pelicula:
                        res = 1
                    elif radiobutton1 == serie:
                        res = 2
                    elif radiobutton1 == ambas:
                        res = 3
                    else:
                        res = 0
                        
        Cambio realizado: Las funciones tienen un proposito mas claro
        y se usan en otra parte del codigo (no hay return ya que
        tkinter no me lo compilaba)
                def formatos (eleccion1):
                    for i in range(len(eleccion1)):
                    ...
                pregunta1 = formatos(eleccion1)
                    
        
        Líneas de código donde se ve la corrección: 50 a 64, 84 a 99,
        130 a 494, 659, 676, 900 a 903
        """
        
        """
        Sub-Competencia: usa la forma más a apropiada al problema para
        guardar los datos (listas, variable, tipo de dato, etc...)
        
        Error original: Las listas no se compilaban en el codigo
                lista = ["a", "b", "c"]
                tkinter.Label(quiz_anime,
                              text=lista).pack(anchor="w")
                
        Cambio realizado: la lista se escribe en cada radiobutton sin tener
        que hacerlos manualmente (cosa que no se pudo hacer con los checkbutons)
                radiobutton2 = tkinter.Radiobutton(quiz_anime, text= eleccion2[i],
                                                   variable = cantidad
                                                   ).pack(anchor="w")
                                                   
        Líneas de código donde se ve la corrección: 50 a 64, 84 a 99,
        """
        
        """
        Sub-Competencia: Aplica estructuras condicionales para resolver un problema
        
        Error original: El codigo no compila al los condicinales
        no servir y estar puestos de manera correcta
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
                    
        Cambio realizado: las condiciones estan basadas en variables
        existentes y estan organiazadas con valores mas exactos
                if (formato.get() == 0) and (cantidad.get() == 4):
                    if (((romance.get() == 1) and (aventura.get() == 1))
                        and ((shoujo.get() == 1) or (superpoderes.get() == 1))):
        
        Líneas de código donde se ve la corrección: 130 a 494
        """
        
        """
        Sub-Competencia: Usa operadores aritméticos de manera eficaz
        
        Error original: tenia ifs sumandose para crear condiciones
        las cuales al fina no compilaban ya que era una
        syntaxis incorrecta 
                if (((cantidad.get() == 2 or (cantidad.get() == 3))
                    + ((accion.get() == 1) and (aventura.get() == 1))
                    + ((shounen.get() == 1) or (superpoderes.get() == 1)))):
        
        Cambio realizado: añadi en los ciclos una suma sencilla y una condicion
        de menor que en cada uno
                while i < len(recom):
                    print("-",recom[i])
                    i = i + 1
        
        Líneas de código donde se ve la corrección: 531 a 541, 604 a 614
        """
        
        """
        Sub-Competencia: usa la forma más a apropiada al problema para
        guardar los datos (listas, variable, tipo de dato, etc...)
        
        Error original: usar las listas anidadas para cada respuesta
        pero no compilaba ya que tkinter no lo permite (y no encontre
        la sintaxis para poder hacerlo)
                if (((cantidad.get() == 2 or (cantidad.get() == 3))
                    and ((accion.get() == 1) and (aventura.get() == 1))
                    and ((shounen.get() == 1) or (superpoderes.get() == 1)))):
                    nt = tkinter.Label(quiz_anime,
                    text = "Deberias ver:", recoms[1][0])
        
        Cambio realizado: Se usaron las listas anidadas para dar una lista de
        que animes van a estar incluidos en el quiz
                recom = [["El Castillo Vagabundo"],["El Viaje de Chihiro"]]
                recom.sort()
                i = 0
                while i < len(recom):
                    print("-",recom[i])
                    i = i + 1
        
        Líneas de código donde se ve la corrección: 503 a 541, 569 a 614
        """
        
        """
        Sub-Competencia: Aplica estructuras cíclicas para resolver
        un problema de manera eficiente
        
        Error original: No compila el codigo, los ciclos no tenian un uso adecuado
        y solo estaban puestos para cumplir con la entrega
                while else == True:
                    print("aun no hay recomendaciones")
        
        Cambio realizado: Se usan para poder imprimir las listas anidadas y así
        no tener que poner una por una
                i = 0
                while i < len(recoms):
                    print("-",recoms[i])
                    i = i + 1
        
        Líneas de código donde se ve la corrección: 529 a 541, 602 a 614
        """

### Comentarios
    """
    (uso ciclos, uso listas anidadas)
    toma la lista y va por cada valor y poniendoles un '-'
    para que parezca una lista escrita de los animes
    devuelve: la lista en orden alfabetico en forma de
    prints en la consola de python
    """
    
    """
    (uso funciones)
    toma la funcion y hace que actue una vez sea
    precionado el boton
    devuelve: el texto del anime que quede con las
    elecciones de los otros botones
    """


