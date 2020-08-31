import config as cf
import sys
import csv

from ADT import list as lt
from DataStructures import listiterator as it
#from DataStructures import liststructure as lt

#from Sorting.insertionsort import lessfunction
from Sorting import insertionsort  as InsSort
from Sorting import shellsort as shell
from Sorting import selectionsort as seSort
from time import process_time 
from Sorting import insertionsort  as InsSort




def printMenu():

    print("\n**************************************************************************************")
    print("\n Bienvenidos a la consola del RETO 1           ***** EXPLORANDO LAMAGIA DEL CINE *****")
    print("\n**************************************************************************************")
    print ("CARGA DE DATOS")
    print("     (1)  Cargar Datos de Archivos Large ")
    print("     (2)  Cargar Datos de Archivos Small ")
    print("     (3)  Cargar cualquier archivo por nombre")
    print ("")
    print ("REQUERIMIENTO 1 - Crear Ranking de peliculas")
    print("     (4)  Consultar numero de peliculas buenas (vote_average>=6)")
    print("     (5)  Cacular el promedio de la votacion")
    print("     (6)  Consultar buenas peliculas por director")
    print ("")
    print ("REQUERIMIENTO 2 - Crear Ranking de peliculas")
    print("     (7)  Ordenar por Vote Count Ascendente")
    print("     (8)  Ordenar por Vote Count Descendente")
    print("     (9)  Ordenar por Vote Average Ascendente")
    print("     (10) Ordenar por Vote Average Descendente")
    print("     (11) The Best Movies")
    print("     (12) The Worst Movies")
    # print("     (13) Shell sort")
    #print("     (14) Selection Sort")

    print ("")
    print ("REQUERIMIENTO 3 - Conocer un director")
    print("     (15) Listar las peliculas de un director")
    print("     (16) Numero de peliculas del director")
    print("     (17) Promedio de la calificacion de las peliculas del director")
    print ("")

    print ("REQUERIMIENTO 4 - Información de un actor")
    print("     (18) Listar las peliculas de un actor")
    print("     (19) numero de peliculas en las que ha participado")
    print("     (20) Nombre del director con el que mas colaboraciones ha tenido")
    print("     (21) Cantidad de películas en las que ha participado")    
    print ("") 
    print ("REQUERIMIENTO 5 - Entender un género cinematográfico")
    print("     (22) lista de todas las películas asociadas al género")
    print("     (23) La cantidad de películas encontradas")
    print("     (24) El promedio de votos (vote_count) del género")  
    print ("") 
    print ("REQUERIMIENTO 6 - Crear ranking del género")
    print("     (25) Lista de las películas que hacen parte del ranking ")
    print("     (26) El promedio de votos y calificación (vote_count) películas que hacen parte del ranking.")
    print("     (27) El promedio de votos y calificación (vote_average) dpelículas que hacen parte del ranking.")  
    print ("") 
    print("     0- Salir")

"""   De aqui en adelante  procedimientos para el Lab 0"""



def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1


def loadCSVFile (file, cmpfunction):
    lst=lt.newList("ARRAY_LIST", cmpfunction)
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(  cf.data_dir + file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst


def loadMovies ():
    lst = loadCSVFile("theMoviesdb/movies-small.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def peliculasBuenas(lst1: list)-> int:
    #print(lst1)
    print("Aqui estoy en peliculas buenas ")
    nRegistros= len(lst1)
    pelBuenas=0
    for i in range (0, nRegistros, 1):
        if (float(lst1[i]['vote_average']) >= 6):
            pelBuenas+=1
            
        #print(lst1[i]['vote_average'])
        #pelBuenas=pelBuenas+ float(lst1[i]['vote_average'])
    #print(pelBuenas)    
    #input("Click para continuar")
   
    return pelBuenas

def PromedioPeliculasBuenas(lst1: list)-> float:
    #print(lst1)
    print("Aqui estoy ")
    nRegistros= len(lst1)
    pelBuenas=0
    proBuenas=0.0
    for i in range (0, nRegistros, 1):
        if (float(lst1[i]['vote_average']) >= 6):
            pelBuenas+=1
            proBuenas= proBuenas + float(lst1[i]['vote_average'])
        #print(lst1[i]['vote_average'])
        #pelBuenas=pelBuenas+ float(lst1[i]['vote_average'])
    #print(pelBuenas)    
    #input("Click para continuar")
    proBuenas=proBuenas/pelBuenas
    return proBuenas
    
def loadCSVFile1 (file, lst, sep=";")->list:

def loadCSVFile (file, lst, sep=";")->list:
    """
    Carga un archivo csv a una lista
    Args:
        file 
            Archivo de texto del cual se cargaran los datos requeridos.
        lst :: []
            Lista a la cual quedaran cargados los elementos despues de la lectura del archivo.
        sep :: str
            Separador escodigo para diferenciar a los distintos elementos dentro del archivo.
    Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None   
    """
    del lst[:]
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep

    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lst.append(row)
    except:
        del lst[:]
        print("Se presento un error en la carga del archivo")
    
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
     

    #for i in range (0,len(lst)-1,1):
    #    print (lst[i])
    input ("Ya se cargo el archivo, Clic para continuar")
    return lst

def peliculasBuenasDirector(lst1: list, lst2:list,  director:str)-> None:


    nRegistros= len(lst1)
    print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")   
    #print (lst2[0]['director_name'], "   ++++   ", director )
    print ("La cantidad de registos a consultar son:", nRegistros)
    #print("Aqui estoy ... ")
    #input ("Clic en peliculas director")
    pelBuenasDirector=0
    proBuenas=0.0
    NuPeliculas=0
    

    for i in range (0, nRegistros, 1):
        if (lst2[i]['director_name'] == director):
            NuPeliculas= NuPeliculas+1
        if (float(lst1[i]['vote_average']) >= 6) and (lst2[i]['director_name'] == director):
            pelBuenasDirector+=1
            proBuenas= proBuenas + float(lst1[i]['vote_average'])

def printMenu():
    """
    Imprime el menu de opciones
    """
 
    print("\n**************************************************************************************")
    print("\n Bienvenidos a la consola del RETO 1           ***** EXPLORANDO LAMAGIA DEL CINE *****")
    print("\n**************************************************************************************")
    print ("CARGA DE DATOS")
    print("     (1) Lab 0 - Cargar Datos de Archivos Large ")
    print("     (2) Lab 0 - Cargar Datos de Archivos Small ")
    print("     (3) Lab 0 - Cargar cualquier archivo por nombre")
    print ("")
    print ("REQUERIMIENTO 2 - Crear Ranking de peliculas")
    print("     (4) Lab 1 - Ordenar por Vote Count Ascendente")
    print("     (5) Lab 1 - Ordenar por Vote Count Descendente")
    print("     (6) Lab 1 - Ordenar por Vote Average Ascendente")
    print("     (7) Lab 1 - Ordenar por Vote Average Descendente")
    print("     (8) Lab 1 - The Best Movies")
    print("     (9) Lab 1 - The Best Worst")
    print ("")
    print ("REQUERIMIENTO 3 - Conocer un director")
    print("     (10) Lab 1 - Listar las peliculas de un director")
    print("     (11) Lab 1 - numero de peliculas del director")
    print("     (12) Lab 1 - promediode la calificacion de las peliculas del director")
    print ("")
    
    print("     0- Salir")

"""   De aqui en adelante  procedimientos para el Lab 0"""
    
def peliculasBuenas(lst1: list)-> int:
    #print(lst1)
    print("Aqui estoy ")
    nRegistros= len(lst1)
    pelBuenas=0
    for i in range (0, nRegistros, 1):
        if (float(lst1[i]['vote_average']) >= 6):
            pelBuenas+=1

            
        #print(lst1[i]['vote_average'])
        #pelBuenas=pelBuenas+ float(lst1[i]['vote_average'])
    #print(pelBuenas)    
    #input("Click para continuar")

    if pelBuenasDirector != 0:
        proBuenas= proBuenas/pelBuenasDirector
        respuesta=(pelBuenasDirector, proBuenas)
    print ("")
    print("El numero de peliculas del director " , director , " son: ", NuPeliculas ,"de las cuales ", pelBuenasDirector, "son buenas. Con un promedio de: ", round(proBuenas,2)) 
    print("")
    print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")      
    input ("Clic para cotinuar")
  #  return respuesta

def ListarPeliculasDirector(lst1: list, lst2:list,  director:str)-> None:
    
    nRegistros= len(lst1)
    print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")   
    #print (lst2[0]['director_name'], "   ++++   ", director )
    print ("La cantidad de registos a consultar son:", nRegistros)
    #print("Aqui estoy ... ")
    #input ("Clic en peliculas director")
    pelBuenasDirector=0
    proBuenas=0.0
    NuPeliculas=0
    
    print ("++++++++++++++++++++++++++++++++ Las peliculas del director ",  director , " ++++++++++++++++++++++++++++++++++++++++++++++++++")
    print ("")
    
    for i in range (0, nRegistros, 1):

        if (lst2[i]['director_name'] == director):
            NuPeliculas= NuPeliculas+1
            print (lst1[i]['original_title']) 

    print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")      
    input ("Clic para cotinuar")
  #  return respuesta

def ContarPeliculasDirector(lst1: list, lst2:list,  director:str)-> None:
    
    nRegistros= len(lst1)
    print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")   
    #print (lst2[0]['director_name'], "   ++++   ", director )
    print ("La cantidad de registos a consultar son:", nRegistros)
    #print("Aqui estoy ... ")
    #input ("Clic en peliculas director")
    pelBuenasDirector=0
    proBuenas=0.0
    NuPeliculas=0
    
    print ("++++++++++++++++++++++++++++++++ Las peliculas del director ",  director , " ++++++++++++++++++++++++++++++++++++++++++++++++++")
    print ("")
    
    for i in range (0, nRegistros, 1):

        if (lst2[i]['director_name'] == director):
            NuPeliculas= NuPeliculas+1
            

    print ("El numero de peliculas de [", director, " ] es: ", NuPeliculas  )
    print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")      
    input ("Clic para cotinuar")
  #  return respuesta

def PromedioPeliculasDirector(lst1: list, lst2:list,  director:str)-> None:
    
    nRegistros= len(lst1)
    print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")   
    #print (lst2[0]['director_name'], "   ++++   ", director )
    print ("La cantidad de registos a consultar son:", nRegistros)
    #print("Aqui estoy ... ")
    #input ("Clic en peliculas director")
    pelBuenasDirector=0
    proBuenas=0.0
    NuPeliculas=0
    
    print ("++++++++++++++++++++++++++++++++ Las peliculas del director ",  director , " ++++++++++++++++++++++++++++++++++++++++++++++++++")
    print ("")
    
    for i in range (0, nRegistros, 1):

        if (lst2[i]['director_name'] == director):
            NuPeliculas= NuPeliculas+1
            proBuenas= proBuenas + float(lst1[i]['vote_average'])
    proBuenas=proBuenas/NuPeliculas        

    print ("El numero de peliculas de [", director, " ] es: ", NuPeliculas, " y tiene un vote_average de: ", round(proBuenas,2)   )
    print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")      
    input ("Clic para cotinuar")
  #  return respuesta


def buscarMovies (lista2:list,cantidad:int)->None:
        
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++  The Best Movies +++++++++++++++++++++++++++++++++")
    
    for i in range (len(lista2)-1,len(lista2)-1-cantidad,-1):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(lista2[i],"\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    input ("Dar clic para continuar...")

def buscarMoviesWorst (lista2:list,cantidad:int)->None:
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++  The Worst Movies +++++++++++++++++++++++++++++++++")
    for i in range (0,cantidad,1):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(lista2[i],"\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    input ("Dar clic para continuar...")

   
    return pelBuenas

def PromedioPeliculasBuenas(lst1: list)-> float:
    #print(lst1)
    print("Aqui estoy ")
    nRegistros= len(lst1)
    pelBuenas=0
    proBuenas=0.0
    for i in range (0, nRegistros, 1):
        if (float(lst1[i]['vote_average']) >= 6):
            pelBuenas+=1
            proBuenas= proBuenas + float(lst1[i]['vote_average'])
        #print(lst1[i]['vote_average'])
        #pelBuenas=pelBuenas+ float(lst1[i]['vote_average'])
    #print(pelBuenas)    
    #input("Click para continuar")
    proBuenas=proBuenas/pelBuenas
    return proBuenas

def peliculasBuenasDirector(lst1: list, lst2:list,  director:str)-> None:
    #print(lst1)
    print("Aqui estoy ")
    nRegistros= len(lst1)
    pelBuenasDirector=0
    proBuenas=0.0
    NuPeliculas=0
    for i in range (0, nRegistros, 1):
        if ( lst2[i]['director_name'] == director):
            NuPeliculas= NuPeliculas+1
        if (float(lst1[i]['vote_average']) >= 6) and (lst2[i]['director_name'] == director):
            pelBuenasDirector+=1
            proBuenas= proBuenas + float(lst1[i]['vote_average'])
            
        #print(lst1[i]['vote_average'])
        #pelBuenas=pelBuenas+ float(lst1[i]['vote_average'])
    #print(pelBuenas)    
    #input("Click para continuar")
    if pelBuenasDirector != 0:
        proBuenas= proBuenas/pelBuenasDirector
        respuesta=(pelBuenasDirector, proBuenas)
    print("El numero de peliculas del director " , director , " son: ", NuPeliculas ,"de las cuales ", pelBuenasDirector, "son buenas. Con un promedio de: ", round(proBuenas,2)) 
    input ("Clic para cotinuar")
  #  return respuesta

    """   De aqui en adelante debemos desarrollar los procedimientos para el Lab 1"""
  

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    return 0



def iSort (lst:list, orden:str)->list: 
    
    input ("Vamos a proceder a ordenar ascendentemente usando el metodo Insertion Sort, esto puede tomar algunos segundos o minutos. Clic para continuar")
    listaOrdenada = []
    listaOrdenada=InsSort.insertionSort (lst, orden)
  
   
    return listaOrdenada

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """

    lista1 = []  # se require usar lista definida peliculas
    lista2 = []  # se require usar lista definida directores casting
    lista3 = []   # se require usar lista definida books

    lista1 = []  # se require usar lista definida
    lista2 = []  # se require usar lista definida
    lista3 = []   # se require usar lista definida
    """

    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar ?  ') #leer opción ingresada
        print ("Usted selecciono: ", inputs)
        if len(inputs)>0:

            if int(inputs)==1: #opcion 1
                lista1=loadCSVFile1("Data/theMoviesdb/MoviesDetailsCleaned-large.csv", lista1) 
                print("Datos cargados de Movies Large, ",len(lista1)," elementos cargados")
                lista2=loadCSVFile1("Data/theMoviesdb/MoviesCastingRaw-large.csv", lista2 ) 
                print("Datos cargados de Casting Large, ",len(lista2)," elementos cargados")
                input ("Clic para cotinuar...")

            elif int(inputs)==2: #opcion 2
                lista1=loadCSVFile1("Data/theMoviesdb/MoviesDetailsCleaned-small.csv", lista1) 
                print("Datos cargados de Movies Small, ",len(lista1)," elementos cargados")
                lista2=loadCSVFile1("Data/theMoviesdb/MoviesCastingRaw-small.csv", lista2) 
                print("Datos cargados de Casting Small, ",len(lista2)," elementos cargados")
                input ("Clic para cotinuar")
            
            elif int(inputs)==3: #opcion 3
                
                input ("Clic para continuar")
                fileToLoad = input ("Digite el nombre del archivo [ ejemplo: Data/GoodReads/books.csv ] : ")
                lista1=loadCSVFile1(fileToLoad,lista1) 
                print("Datos cargados del archivo [",fileToLoad, " ]: ", len(lista1))
                
                input ("Clic para cotinuar")

            elif int(inputs[0])==4: #opcion 4
                lista1=loadCSVFile1("Data/theMoviesdb/MoviesDetailsCleaned-small.csv", lista1) 
                print("Datos cargados de Movies Small, ",len(lista1)," elementos cargados")
                peliculas_buenas= peliculasBuenas(lista1)
                print("El numero de peliculas revisadas fueron: " , len(lista1) , " de las cuales " , peliculas_buenas , "obtuvieron calificacion >= a 6") 
                input ("Clic para cotinuar")

            elif int(inputs[0])==5: #opcion 5
                lista1=loadCSVFile1("Data/theMoviesdb/MoviesDetailsCleaned-small.csv", lista1)
                proPeliculas_buenas= PromedioPeliculasBuenas(lista1)
                print("El  promedio de las peliculas buenas fue de:  " , round(proPeliculas_buenas,2) ) 
                input ("Clic para cotinuar")

            elif int(inputs[0])==6: #opcion 6
                
                lista1=loadCSVFile1("Data/theMoviesdb/MoviesDetailsCleaned-large.csv", lista1)
                lista2=loadCSVFile1("Data/theMoviesdb/MoviesCastingRaw-large.csv", lista2 ) 
                print("Datos cargados Movies Large: [ ",len(lista1),"], casting with directors: [ ", len (lista2), " ]")
                print("")
                director=input("Digite el nombre del director a consultar? ")
                print("El numero de peliculas buenas del director " , director) 
                #input ("Clic para cotinuar este es el Diretor de enviar...")
                peliculasDirector= peliculasBuenasDirector(lista1, lista2, director)
                #print("El numero de peliculas buenas del director " , director , " son: " , peliculasDirector) 
                input ("Clic para cotinuar")

            elif int(inputs)==7: #opcion 7
                orden="less"
                criterio='vote_count'
                lista1=loadCSVFile1("Data/theMoviesdb/MoviesDetailsCleaned-small.csv", lista1) 
                lista2=loadCSVFile1("Data/theMoviesdb/MoviesCastingRaw-small.csv", lista2) 
                print("Datos cargados de Movies Small, ",len(lista1)," elementos cargados", len(lista2))
                t1_start = process_time() #tiempo inicial
                input ("Vamos a proceder a ordenar usando el metodo Insertion Sort, esto puede tomar algunos segundos o minutos. Clic para continuar")
                lista3=InsSort.insertionSort (lista1,criterio,orden)
                t1_stop = process_time() #tiempo final
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("Tiempo de ejecución de metodo InsertionSort ",t1_stop-t1_start," segundos")
                input ("Dar clic para continuar...")

            elif int(inputs)==8: #opcion 8
                orden="greater"
                criterio='vote_count'
                lista1=loadCSVFile1("Data/theMoviesdb/MoviesDetailsCleaned-small.csv", lista1) 
                lista2=loadCSVFile1("Data/theMoviesdb/MoviesCastingRaw-small.csv", lista2) 
                print("Datos cargados de Movies Small, ",len(lista1)," elementos cargados", len(lista2))
                t1_start = process_time() #tiempo inicial
                input ("Vamos a proceder a ordenar usando el metodo Insertion Sort, esto puede tomar algunos segundos o minutos. Clic para continuar")
                lista3=InsSort.insertionSort (lista1,criterio,orden)
                t1_stop = process_time() #tiempo final
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("Tiempo de ejecución de metodo InsertionSort ",t1_stop-t1_start," segundos")
                input ("Dar clic para continuar...")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

            elif int(inputs)==9: #opcion 9
                orden="less"
                criterio='vote_average'
                lista1=loadCSVFile1("Data/theMoviesdb/MoviesDetailsCleaned-small.csv", lista1) 
                lista2=loadCSVFile1("Data/theMoviesdb/MoviesCastingRaw-small.csv", lista2) 
                print("Datos cargados de Movies Small, ",len(lista1)," elementos cargados", len(lista2))
                t1_start = process_time() #tiempo inicial
                input ("Vamos a proceder a ordenar usando el metodo Insertion Sort, esto puede tomar algunos segundos o minutos. Clic para continuar")
                lista3=InsSort.insertionSort (lista1,criterio,orden)
                t1_stop = process_time() #tiempo final
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("Tiempo de ejecución de metodo InsertionSort ",t1_stop-t1_start," segundos")
                input ("Dar clic para continuar...")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

            elif int(inputs)==10: #opcion 10 
                t1_start = process_time() #tiempo inicia
                orden="greater"
                criterio='vote_average'
                lista1=loadCSVFile1("Data/theMoviesdb/MoviesDetailsCleaned-small.csv", lista1) 
                lista2=loadCSVFile1("Data/theMoviesdb/MoviesCastingRaw-small.csv", lista2) 
                print("Datos cargados de Movies Small, ",len(lista1)," elementos cargados", len(lista2))
                input ("Vamos a proceder a ordenar usando el metodo Insertion Sort, esto puede tomar algunos segundos o minutos. Clic para continuar")
                lista3=InsSort.insertionSort (lista1,criterio,orden)
                t1_stop = process_time() #tiempo final
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("Tiempo de ejecución de metodo InsertionSort ",t1_stop-t1_start," segundos")
                input ("Dar clic para continuar...")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

            elif int(inputs)==11: #opcion 11
                t1_start = process_time() #tiempo inicia
                orden="less"
                criterio='vote_count'
                #lista1=loadCSVFile1("Data/theMoviesdb/MoviesDetailsCleaned-large.csv", lista1) 
                lista1=loadCSVFile1("Data/theMoviesdb/MoviesDetailsCleaned-small.csv", lista1) 
                #print("Datos cargados : ", len(lista2))
                lista3=InsSort.insertionSort (lista1,criterio,orden)
                print ("")
                print ("Datos cargados y ordenados...")
                print ("")
                cantidad=int(input ("Digite el numero de pelicuales que dea listar?  "))
                print ("")
                buscarMovies (lista1,cantidad)
                t1_stop = process_time() #tiempo final
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("Tiempo de ejecución de metodo de la busqueda ",t1_stop-t1_start," segundos")
                input ("Clic para cotinuar")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

            elif int(inputs)==12: #opcion 12
                t1_start = process_time() #tiempo inicia

                orden="less"
                criterio='vote_count'
                #lista1=loadCSVFile1("Data/theMoviesdb/MoviesDetailsCleaned-large.csv", lista1) 
                lista1=loadCSVFile1("Data/theMoviesdb/MoviesDetailsCleaned-small.csv", lista1) 
                lista3=InsSort.insertionSort (lista1,criterio,orden)
                print ("Datos cargados y ordenados...")
                print ("")
                cantidad=int(input ("Digite el numero de pelicuales que dea listar?  "))
                print ("")
                buscarMoviesWorst (lista1,cantidad)
                t1_stop = process_time() #tiempo final
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("Tiempo de ejecución de metodo de la busqueda ",t1_stop-t1_start," segundos")
                input ("Clic para cotinuar")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

                
            elif int(inputs)==13: #opcion 13
                lista1=lt.newList (datastructure='ARRAY_LIST')   
                #lista1=lt.newList (datastructure='SINGLE_LINKED') 
                #lista1 = lt.newList() 
                lista1=loadCSVFileNew("Data/theMoviesdb/MoviesDetailsCleaned-small.csv") 
                shell.shellSort(lista1,lessfunction)
                input ("Se ordenaron ascendentemente las peliculas por el campo  ** Vote Count ** ....Clic para cotinuar")
           
            elif int(inputs)==14: #opcion 14
                
                lista1=lt.newList ()
                #lista1=lt.newList (datastructure='ARRAY_LIST')   
                #lista1=lt.newList (datastructure='SINGLE_LINKED') 
                #lista1 = lt.newList() 
                lista1=loadCSVFileNew("Data/theMoviesdb/MoviesDetailsCleaned-small.csv") 
                seSort.selectionSort(lista1,lessfunction)         

            elif int(inputs)==15: #opcion 15
                lista1=loadCSVFile1("Data/theMoviesdb/MoviesDetailsCleaned-large.csv", lista1)
                lista2=loadCSVFile1("Data/theMoviesdb/MoviesCastingRaw-large.csv", lista2 ) 
                print("Datos cargados Movies Large: [ ",len(lista1),"], casting with directors: [ ", len (lista2), " ]")
                print("")
                director=input("Digite el nombre del director a consultar? ")
                print("El numero de peliculas buenas del director " , director) 
                #input ("Clic para cotinuar este es el Diretor de enviar...")
                peliculasDirector= ListarPeliculasDirector(lista1, lista2, director)
                #print("El numero de peliculas buenas del director " , director , " son: " , peliculasDirector) 
                input ("Clic para cotinuar")                
          
            elif int(inputs)==16: #opcion 16
                lista1=loadCSVFile1("Data/theMoviesdb/MoviesDetailsCleaned-large.csv", lista1)
                lista2=loadCSVFile1("Data/theMoviesdb/MoviesCastingRaw-large.csv", lista2 ) 
                print("Datos cargados Movies Large: [ ",len(lista1),"], casting with directors: [ ", len (lista2), " ]")
                print("")
                director=input("Digite el nombre del director a consultar? ")
                print("El numero de peliculas buenas del director " , director) 
                #input ("Clic para cotinuar este es el Diretor de enviar...")
                peliculasDirector= ContarPeliculasDirector(lista1, lista2, director)
                #print("El numero de peliculas buenas del director " , director , " son: " , peliculasDirector) 
                input ("Clic para cotinuar")   

            elif int(inputs)==17: #opcion 17
                lista1=loadCSVFile1("Data/theMoviesdb/MoviesDetailsCleaned-large.csv", lista1)
                lista2=loadCSVFile1("Data/theMoviesdb/MoviesCastingRaw-large.csv", lista2 ) 
                print("Datos cargados Movies Large: [ ",len(lista1),"], casting with directors: [ ", len (lista2), " ]")
                print("")
                director=input("Digite el nombre del director a consultar? ")
                print("El numero de peliculas buenas del director " , director) 
                #input ("Clic para cotinuar este es el Diretor de enviar...")
                peliculasDirector= PromedioPeliculasDirector(lista1, lista2, director)
                #print("El numero de peliculas buenas del director " , director , " son: " , peliculasDirector) 
                input ("Clic para cotinuar")        

            elif int(inputs)==17: #opcion 18

               input (" Estamos en constuccion.....Clic para cotinuar")   

            elif int(inputs)==17: #opcion 19

               input (" Estamos en constuccion.....Clic para cotinuar")         
            
            elif int(inputs)==0: #opcion 0, salir
                sys.exit(0)  


            if int(inputs[0])==1: #opcion 1
                lista = loadCSVFile("Data/test.csv") #llamar funcion cargar datos
                print("Datos cargados, ",lista['size']," elementos cargados")

            elif int(inputs[0])==2: #opcion 2
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    

                else: print("La lista tiene ",lista['size']," elementos")

            elif int(inputs[0])==3: #opcion 3
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsFilteredByColumn(criteria, "nombre", lista) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )

            elif int(inputs[0])==4: #opcion 4
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsByCriteria(criteria,0,lista)
                    print("Coinciden ",counter," elementos con el crtierio: '", criteria ,"' (en construcción ...)")
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
        """    
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar:  ') #leer opción ingresada
        print ("Usted selecciono: ", inputs)
        if len(inputs)>0:
            if int(inputs)==1: #opcion 1
                lista1=loadCSVFile("Data/theMoviesdb/MoviesDetailsCleaned-large.csv", lista1) 
                print("Datos cargados de Movies Large, ",lista1['size']," elementos cargados")
                
                lista2=loadCSVFile("Data/theMoviesdb/MoviesCastingRaw-large.csv", lista2 ) 
                print("Datos cargados de Casting Large, ",lista2['size']," elementos cargados")
                input ("Clic para cotinuar...")

            elif int(inputs)==2: #opcion 2
                lista1=loadCSVFile("Data/theMoviesdb/MoviesDetailsCleaned-small.csv", lista1) 
                print("Datos cargados de Movies Small, ",len(lista1)," elementos cargados")
                lista2=loadCSVFile("Data/theMoviesdb/MoviesCastingRaw-small.csv", lista2) 
                print("Datos cargados de Casting Small, ",len(lista2)," elementos cargados")
                input ("Clic para cotinuar")
            
            elif int(inputs)==3: #opcion 3
                
                input ("Clic para continuar")
                fileToLoad = input ("Digite el nombre del archivo [ ejemplo: Data/GoodReads/books.csv ] : ")
                lista1=loadCSVFile(fileToLoad) 
                print("Datos cargados del archivo [",fileToLoad, " ]: ", lista1['size'])
                
                input ("Clic para cotinuar")

            elif int(inputs)==4: #opcion 4
                 a="a"
                 #print (lista1)
                 #input ("Clic para avanzar")
                 lista3=iSort (lista1, a)
                 print  ("Se ha ordenado la lista")

            elif int(inputs)==5: #opcion 5
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsFilteredByColumn(criteria, "nombre", lista) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs)==6: #opcion 6
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsByCriteria(criteria,0,lista)
                    print("Coinciden ",counter," elementos con el crtierio: '", criteria ,"' (en construcción ...)")
            elif int(inputs)==7: #opcion 7 
                input ("En construccion....Clic para cotinuar")
            elif int(inputs)==8: #opcion 8
                input ("En construccion....Clic para cotinuar")
            elif int(inputs)==9: #opcion 9
                input ("En construccion....Clic para cotinuar")

            elif int(inputs)==0: #opcion 0, salir
                sys.exit(0)  

            

if __name__ == "__main__":
    main()