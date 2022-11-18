def mSofia_colocarCC():
    global int_CC1
    global int_CC2
    int_CC1 = raw_input("Colocar la primer CC generada: ")
    int_CC2 = raw_input("Colocar la segunda CC generada: ")

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
    Bin_Generado1 = int_CC1[0:8] + str(resultado) + "xxxxxx"
    Bin_Generado2 = int_CC2[0:8] + str(resultado) + "xxxxxx"

    print(Bin_Generado1)
    print("\n")
    print(Bin_Generado2)

def mSofia_mensaje():
    print("El formato de CC1 y CC2 debe respetar la siguiente estructura: xxxxxxxxxxxxx|xx|xx|xxx")
    mSofia_colocarCC()


def mSofia_validar():
    if cont1==4 and cont2==4:
        mSofia_calculo()
    else:
        mSofia_mensaje()
        mSofia_validar()

mSofia_colocarCC()
mSofia_validar()

