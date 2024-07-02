import numpy as np

DiaTrabajado=10000;
MontoAdicional=0.25;

def registrogiftcards(ListaNombres, ListaGiftcards, ListaDirecciones, ListaTotalAbon, ListaNumeroCF, ListaAdiCargas, ListaDiasTrabajados):
    for i in range(len(ListaGiftcards)):
        NombreTrabajador=input("INGRESE NOMBRE DEL TRABAJADOR: ")
        ListaNombres.append(NombreTrabajador)
        Direccion=input("INGRESE LA DIRECCION DEL TRABAJADOR: ")
        ListaDirecciones.append(Direccion)
        NumCargasFam=int(input("INGRESE NUMERO DE CARGAS FAMILIARES: "))
        ListaNumeroCF.append(NumCargasFam)
        DiasTrabajados=int(input("INGRESE NUMERO DE DIAS TRABAJADOS EN EL ULTIMO MES: "))
        ListaDiasTrabajados.append(DiasTrabajados)
        MontoTotalAbon=DiasTrabajados*DiaTrabajado
        ListaTotalAbon.append(MontoTotalAbon)
        if NumCargasFam<=3:
                MontoTotalAbon=MontoTotalAbon+MontoAdicional
        TotalFinalAbon=MontoTotalAbon+MontoAdicional
        ListaAdiCargas.append(NumCargasFam)
        ListaGiftcards.append(TotalFinalAbon)

def cobrosregistrados(ListaNombres, ListaGiftcards, ListaDirecciones, ListaTotalAbon, ListaNumeroCF, ListaAdiCargas, ListaDiasTrabajados):
    print(f"TRABAJADORES:                   \t{ListaNombres}")
    print(f"DIRECCION:                      \t{ListaDirecciones}")
    print(f"MONTO ABONADO:                  \t{ListaTotalAbon}")
    print(f"NUMERO DE CARGAS FAMILIARES:    \t{ListaNumeroCF}")
    print(f"ADICIONAL POR CARGAS:           \t{ListaAdiCargas}")
    print(f"TOTAL:                          \t{ListaGiftcards}")




def despachos(Sector, ListaDirecciones):
    if Sector=="C":
         



