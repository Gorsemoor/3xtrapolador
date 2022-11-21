# -*- coding: utf-8 -*-

def menu():
    srt_titulo =" Opciones de Extrapolacion "
    print("\n")
    print("\033[1;32m " + srt_titulo.center(40,"*"))
    print("\033[0m")

    print("\n \033[1;33m  1.Extrapolacion basica \n  \033[1;34m 2.Metodo dos \n  \033[1;35m 3.Metodo Sofia  \n  \033[1;31m 4.Metodo DinVerter \n  \033[1;36m 5.Salir \n")
    print("\033[0m")
    
    Op =raw_input("Selecciona una opcion del menu: ")

    if Op.isdigit()==True:
        resultado = "numero"
    else:
         resultado = "texto"
    
    if resultado == "numero":
        if int(Op)==1:
            mBasico()
        elif int(Op)==2:
            mSimilitud()
        elif int(Op)==3:
            mSofia()
        elif int(Op)==4:
            mDinverter()
        elif int(Op)==5:
            print("exit")
    else:
        print("Solo se admiten las opciones del menu \n")
        menu()
   


# METODO BASICO DE EXTRAPOLACION
def mBasico():
    def mBasico_colocarCC():
        
        global str_Cc

        print("\033[H\033[J") 
        srt_titulo =" METODO BASICO DE EXTRAPOLACION "
        print("\n")
        print("\033[1;32m " + srt_titulo.center(40,"*"))
        print("\033[0m")
        print("\n")
       
        str_Cc = raw_input("\033[1;33m Coloca tu CC completa: \033[0m")
      
        lista1=[]

        lista1 = str_Cc.split("|")

        global cont1
        cont1 =0

        for valor1 in lista1:
            cont1 +=1
   
    def mBasico_calculo():
        int_Posicion = str_Cc.find("|")

        str_Bin = str_Cc[:int_Posicion-6]

        print(str_Bin + "xxxxx1")
        print("\n")
        consulta_gral(mBasico_colocarCC, mBasico_validar)


    def mBasico_validar():
        if cont1==4:
            mBasico_calculo()
        else:
           mensajeGral(mBasico_colocarCC)
           mBasico_validar()    


    mBasico_colocarCC()
    mBasico_validar()

# METODO 2
def mSimilitud():
    def m2_colocarCC():
      
      global POSICION_INICIAL
      global str_Cc1
      global str_Cc2
      
      print("\033[H\033[J") 
      srt_titulo =" METODO 2 "
      print("\n")
      print("\033[1;32m " + srt_titulo.center(40,"*"))
      print("\033[0m")
        
      POSICION_INICIAL = 6
      print("\n")
      str_Cc1 = raw_input("\033[1;33m  Coloca tu CC1: \033[0m")
      print("\n")
      str_Cc2 = raw_input("\033[1;33m  Coloca tu CC2: \033[0m")
      print("\033[0m")
      

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
        
      if list3[9] == "x":
          list3.pop(9)
          list3.append("1")
          
      bin_generado = "".join(list3)

      valor = str_Cc1[0:POSICION_INICIAL]
      print("\n")
      print(" Resultado: %s%s" %(valor, bin_generado))
      print("\n")
      consulta_gral(m2_colocarCC,m2_validar)

        
       
    def m2_validar():
        if cont1==4 and cont2==4:
            m2_calculo()
        else:
            mensajeGral(m2_colocarCC)
            m2_validar()    

    m2_colocarCC()
    m2_validar()
    
# METODO SOFIA
def mSofia():
    def mSofia_colocarCC():
        global int_CC1
        global int_CC2

        print("\033[H\033[J") 
        srt_titulo =" METODO SOFIA "
        print("\n")
        print("\033[1;32m " + srt_titulo.center(40,"*"))
        print("\033[0m")
        print("\n")
        
        int_CC1 = raw_input("\033[1;33m  Colocar la primer CC generada: \033[0m")
        print("\n")
        int_CC2 = raw_input("\033[1;33m  Colocar la segunda CC generada: \033[0m")
        print("\033[0m")
        
        lista1=[]
        lista2=[]

        lista1 = int_CC1.split("|")
        lista2 = int_CC2.split("|")
        
        global cont1
        global cont2
        cont1 =0
        cont2= 0

        for valor1 in lista1:
            cont1 +=1

        for valor2 in lista2:
            cont2 +=1
        
                            
    def mSofia_calculo():
        CC1 =int(int_CC1[9:10]) +  int(int_CC1[10:11])
        CC2 =int(int_CC2[9:10]) +  int(int_CC2[10:11])

        CC1 = float(float(CC1) /2) *5
        CC2 = float(float(CC2)/2)*5


        resultado = int(CC1) + int(CC2)
        Bin_Generado1 = int_CC1[0:8] + str(resultado) + "xxxxx1"
        Bin_Generado2 = int_CC2[0:8] + str(resultado) + "xxxxx1"

        print("\nBin Generado 1: %s " %(Bin_Generado1))
        print("\n")
        print("Bin Generado 2: %s \n" %(Bin_Generado2))

        consulta_gral(mSofia_colocarCC,mSofia_validar)
        
 
    def mSofia_validar():
        if cont1==4 and cont2==4:
            mSofia_calculo()
        else:
            mensajeGral(mSofia_colocarCC)
            mSofia_validar()

    mSofia_colocarCC()
    mSofia_validar()



# METODO DINVERTER
def mDinverter():
    def mDin_colocarCC():
        global str_CC1
        global str_CC2
        global  list1_Grupo1
        global  list1_Grupo2
        global  list2_Grupo2
        global str_Cc1
        global str_Cc2

        print("\033[H\033[J") 
        srt_titulo =" METODO DINVERTER "
        print("\n")
        print("\033[1;32m " + srt_titulo.center(40,"*"))
        print("\033[0m")
        print("\n")
        
        str_CC1 = raw_input("\033[1;33m Ingresa la primer cc: \033[0m")
        str_CC2 = raw_input("\033[1;33m Ingresa la segunda cc: \033[0m")

        DIVISOR = 16

        str_Cc1 = str_CC1[0:16]
        str_Cc2 = str_CC2[0:16]

        list1_Grupo1 = [] 
        list1_Grupo2=[] 

        list2_Grupo2 = [] 

        lista1=[]
        lista2=[]

        lista1 = str_CC1.split("|")
        lista2 = str_CC2.split("|")
        
        global cont1
        global cont2
        cont1 =0
        cont2= 0

        for valor1 in lista1:
            cont1 +=1

        for valor2 in lista2:
            cont2 +=1

            
    def mDin_calculo():
        
        valor1 =0
        while valor1 <8:
            list1_Grupo1.append(str_Cc1[valor1])
            valor1 +=1

        valor2=8
        while valor2 <16:
            list1_Grupo2.append(str_Cc1[valor2])
            
            list2_Grupo2.append(str_Cc2[valor2])
            valor2 +=1
            
        list_final =[]

        valor1 = 0

        while valor1 <8:
            list_final.append(int(list1_Grupo1[valor1]) * int(list2_Grupo2[valor1]))
            valor1 +=1

        str_listaFinal = map(str,list_final)
        a="".join(str_listaFinal)

        b="".join(map(str,list1_Grupo2))

        list_Bin=[]

        x = 0

        while x <8:
            if a[x] != b[x]:
                list_Bin.append("x")
            else:
                list_Bin.append(a[x])
            x +=1

        if list_Bin[7] == "x":
            list_Bin.pop(7)
            list_Bin.append("1")
            
        print("----------------  BIN FINAL ----------------")
        binInicial ="".join(map(str,list1_Grupo1))
        r= "".join(map(str,list_Bin))

        print(binInicial +  r)
        consulta_gral(mDin_colocarCC,mDin_validar)
        
        
    def mDin_validar():
        if cont1==4 and cont2==4:
           mDin_calculo()
        else:
            mensajeGral(mDin_colocarCC)
            mDin_validar()

    mDin_colocarCC()
    mDin_validar()

def mensajeGral(mFuncion):
     import time
     print("El formato de CC1 o CC2, debe respetar la siguiente estructura: xxxxxxxxxxxxx|xx|xx|xxx")
     time.sleep(4)
     mFuncion()
     
def consulta_gral(nombreFuncion1, nombreFuncion2):

    while True:
        R=raw_input(" ¿Deseas volver a extrapolar? Y/N: ")
        if R=="Y" or R=="y":
            print("\033[H\033[J") 
            nombreFuncion1()
            nombreFuncion2 ()
            break
        elif R=="N" or R=="n":
            print("\033[H\033[J") 
            menu()
            break
        else:
            print("Solo se admite la respuesta Y (y) o N (n) \n")

    
menu()
