import funcionesGifcards as fg

ListaNombres=[]
ListaGiftcards=[]
ListaDirecciones=[]
ListaTotalAbon=[]
ListaNumeroCF=[]
ListaAdiCargas=[]
ListaDiasTrabajados=[]



while(True):
    print("MENU GIFTCARDS")
    print("1.- REGISTRO DE TRABAJADORES")
    print("2.- LISTA DE TRABAJADORES REGISTRADOS")
    print("3.- OPCION DE DESPACHO")
    print("4.- SALIR")

    opc=int(input("ESCOJA UNA DE LAS OPCIONES 1/2/3/4: "));

    if opc==1:
        print("REGISTRO DE TRABAJADORES")
        fg.registrogiftcards(ListaNombres, ListaGiftcards, ListaDirecciones, ListaTotalAbon, ListaNumeroCF, ListaAdiCargas)
    
    if opc==2:
        print("LISTA DE TRABAJADORES REGISTRADOS")
        fg.cobrosregistrados()

    if opc==3:
        print("OPCION DE DESPACHO");
        Sector=input("¿A QUE SECTOR PERTENECE? CENTRO=C/NORTE=N/SUR=S")
        fg.despachos(Sector, ListaDirecciones)

    if opc==4:
        print("EL PROGRAMA HA FINALIZADO")
        break






