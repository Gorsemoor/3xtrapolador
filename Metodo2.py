def m2_colocarCC():
  
  global POSICION_INICIAL
  global str_Cc1
  global str_Cc2
  
  POSICION_INICIAL = 6
  str_Cc1 = raw_input("Coloca tu CC1: ")
  str_Cc2 = raw_input("Coloca tu CC2: ")

  

  lista1=[]
  lista2=[]

  lista1 = str_Cc1.split("|")
  lista2 =str_Cc2.split("|")
  
  global cont1
  global cont2
  cont1 =0
  cont2= 0

  for valor1 in lista1:
      cont1 +=1

  for valor2 in lista2:
      cont2 +=1
        
def m2_calculo():
  int_Posicion1 = str_Cc1.find("|")
  int_Posicion2 = str_Cc2.find("|")

  str_Bin1 = str_Cc1[POSICION_INICIAL:int_Posicion1]
  str_Bin2 = str_Cc2[POSICION_INICIAL:int_Posicion2]


  list1=[]
  for x in str_Bin1:
    list1.append(x)
    

  list2=[]
  for x in str_Bin2:
    list2.append(x)
    

  list3=[]
  for x in range(10):
    if list1[x] == list2[x]:
      list3.append(list1[x])
    else:
      list3.append("x")

  bin_generado = "".join(list3)

  valor = str_Cc1[0:POSICION_INICIAL]

  print("%s%s" %(valor, bin_generado))

def m2_mensaje():
    print("El formato de CC1 y CC2 debe respetar la siguiente estructura: xxxxxxxxxxxxx|xx|xx|xxx")
    m2_colocarCC()

    
def m2_validar():
    if cont1==4 and cont2==4:
        m2_calculo()
    else:
        m2_mensaje()
        m2_validar()    

m2_colocarCC()
m2_validar()
