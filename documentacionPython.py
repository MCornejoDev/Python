#Esto es un curso de Python
#Líneas y espacios
#Un programa de Python está formado por líneas de texto.
radio = 5
area = 3.14159242 * radio ** 2
print(area)

#Se recomienda que cada línea contenga una única instrucción, 
#aunque puede haber varias instrucciones en una línea, separadas por un punto y coma (;).
radio = 5; area = 3.14159242 * radio ** 2
print(area)

#Por motivos de legibilidad, se recomienda que las líneas no superen los 79 caracteres. 
#Si una instrucción supera esa longitud, se puede dividir en varias líneas usando el caracter contrabarra (\):

radio = 5
area = 3.14159265358979323846 \
       * radio ** 2
print(area)

#Los elementos del lenguaje de Python se separan por espacios en blanco (normalmente, uno),
#aunque en algunos casos no se escriben espacios:

#1- Entre los nombres de las funciones y el paréntesis
#2- Antes de una coma (,)
#3- Entre los delimitadores y su contenido (paréntesis, llaves, corchetes o comillas)
#PD: Los espacios no son significativos, es decir, da lo mismo un espacio que varios, excepto al principio de una línea.

#Consejo : Los espacios al principio de una línea (el sangrado) indican un nivel de agrupamiento. 
# El sangrado inicial es una de las características de Python que lo distinguen de otros lenguajes como JS ,PHP , etc..

#     x = 42
#SyntaxError: unexpected indent

#Palabras reservadas (keyWords)
# False      await      else      import     pass
# None       break      except    in         raise
# True       class      finally   is         return
# and        continue   for       lambda     try
# as         def        from      nonlocal   while
# assert     del        global    not        with
# async      elif       if        or         yield

#Literales

#Los literales son los datos simples que Python es capaz de manejar:

#números: valores lógicos, enteros, decimales y complejos, en notación decimal, octal o hexadecimal Y cadenas de texto

#Operadores
# +       -       *       **      /       //      %      @
# <<      >>      &       |       ^       ~
# <       >       <=      >=      ==      !=

#Identificadores : Son las variables que usan los usuarios para jugar con ellos, deben empezar por una letra y pueden contener
#numeros, mayusculas,minusculas y el guión bajo

#Funciones integradas (built-in functions)
#Una función es un bloque de instrucciones agrupadas, que permiten reutilizar partes de un programa.

#Python incluye las siguientes funciones de forma predeterminada (es decir, estas funciones siempre están disponibles):

#abs()         dict()      help()       min()      setattr()
#all()         dir()       hex()        next()     slice()
#any()         divmod()    id()         object()   sorted()
#ascii()       enumerate() input()      oct()      staticmethod()
#bin()         eval()      int()        open()     str()
#bool()        exec()      isinstance() ord()      sum()
#bytearray()   filter()    issubclass() pow()      super()
#bytes()       float()     iter()       print()    tuple()
#callable()    format()    len()        property() type()
#chr()         frozenset() list()       range()    vars()
#classmethod() getattr()   locals()     repr()     zip()
#compile()     globals()   map()        reversed() __import__()
#complex()     hasattr()   max()        round()
#delattr()     hash()      memoryview() set()

#Funciones adicionales
#Un programa puede definir nuevas funciones o redefinir las funciones integradas. 

#Los nombres de las funciones no pueden coincidir con las palabras reservadas.

#Un programa puede también importar nuevas funciones que se encuentran definidas en otros ficheros llamados módulos.

#Python incluye una biblioteca de módulos (llamada Biblioteca estándar) especializados en todo tipo de tareas.

#Además de la biblioteca estándar, existen miles de módulos escritos por diferentes programadores y accesibles en Internet. 
#El principal repositorio de módulos es el Python Package Index (Índice de paquetes de Python), más conocido por PyPI.