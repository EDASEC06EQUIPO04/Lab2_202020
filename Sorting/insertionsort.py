def insertionSort (lst, criterio:str, orden:str)->list: 
   
  #criterio='vote_count'
  criterio=criterio
      
  if criterio=='vote_count':
    
    size =  len(lst)-1 
    pos1 = 1
    
    for index in range(1,len(lst)):
      currentvalue = int(lst[index][criterio])
      position = index
      original=lst[index]
      #print (currentvalue, " " , index , "  ", position)
      #input ("clic para avanzaar")
      while position>0 and int(lst [position-1][criterio])>int(currentvalue):
          lst [position]=lst [position-1]
          position = position-1
          #print (currentvalue)
      lst[position]=original

   

    if (orden == "less"):
            for i  in range (0,len(lst),1):
                print (lst[i][criterio])
            print ("Se ordeno ascendentemente")
            input ("Se finalizo el proceso...")
    if (orden=="greater"):
            #input ("estoy aqui")
            for i  in range (1,len(lst),1):
              print (lst[len(lst)-i][criterio])
            print ("Se ordeno Descendentemente")
            input ("Se finalizo el proceso...")


  if criterio=='vote_average':
   
    size =  len(lst)-1 
    pos1 = 1
    
    for indexe in range(1,len(lst)):
          #print (lst[indexe][criterio])    
          currentvalue = (lst[indexe][criterio])
          position = indexe
          original=lst[indexe]
          while (position>0 and (lst [position-1][criterio])>(currentvalue)):
              lst [position]=lst [position-1]
              position = position-1
              #print (currentvalue)
          lst[position]=original



    if (orden == "less"):
            for i  in range (0,len(lst),1):
                print (lst[i][criterio])
            print ("Se ordeno ascendentemente")
            input ("Se finalizo el proceso...")
    if (orden=="greater"):
            #input ("estoy aqui")
            for i  in range (1,len(lst),1):
              print (lst[len(lst)-i][criterio])
            print ("Se ordeno Descendentemente")
            input ("Se finalizo el proceso...")

  return lst

def lessfunction (elemento1, elemento2):
    if elemento1<elemento2:
      return True
    return False


def insertionSort (lst, orden:str)->list: 
    print ("ahora si stoy aqui, voy a imprimir dos registros")
    print (lst[0])
    input ("clic para continuar")
    print (lst[1])
    input ("clic para continuar")
    size =  len(lst)-1 
    pos1 = 1
    
    # while pos1 <= size:
    #    pos2 = pos1
    #    while (pos2 >1) and (lessfunction (lst[pos2]['vote_count'], pos2),lst [pos2-1]['vote_count']):
    #        pivot=lst[pos2]
    #       lst[pos2]=lst [pos2-1]
    #        lst [pos2-1]=pivot
    #       pos2 -= 1
    #    pos1 += 1
    #   while (pos2 >1) and (lessfunction (lt.getElement(lst, pos2),lt.getElement(lst, pos2-1))):
    #            lt.exchange (lst, pos2, pos2-1)
    #           pos2 -= 1
    #       pos1 += 1
    
    for index in range(1,len(lst)):
     currentvalue = int(lst[index]['vote_count'])
     posM=int(currentvalue)
     position = index
     #print (currentvalue, " " , index , "  ", position)
     #input ("clic para avanzaar")
     while position>0 and int(lst [position-1]['vote_count'])>int(currentvalue):
         lst [position]=lst [position-1]
         position = position-1
         #print (currentvalue)
     #lst[position]['vote_count']=currentvalue
     print ("fuera de while",currentvalue)
     #input ("clic")
     #lst [position]=lst [position-1]
    input ("************************* dar clic para imprimir lista ordenada  en Insertion procedure  ********************")
    for i  in range (0,20,1):
      print (lst[i])
    
    return lst

