import os
    
odontologia = 0
ginecologia = 0
consulta_general = 0
maternidad = 0
infancia = 0
repetir = True 

def fnt_limpiarPantalla():
        os.system('cls')
        
def fnt_opcion(op):
    global odontologia,consulta_general,maternidad,infancia
    if (op == 1):
         odontologia += 1
        
    if (op == 2):
        ginecologia += 1
            
    if (op == 3):
        consulta_general += 1
            
    if (op == 4):
        maternidad += 1
            
    if  (op == 5):
        infancia += 1
        

    def fnt_reporte():
        global odontologia,ginecologia,consulta_general,maternidad,infancia
        print("Odontología: ",odontologia)
        print("Ginecología: ",ginecologia)
        print("Consulta general: ",consulta_general)
        print("Maternidad: ",maternidad)
        print("Infancia: ",infancia)

    while repetir == True:
        fnt_limpiarPantalla()
        opcion = int(input('---MENÚ DE OPCIONES---\n1. Odontologia\n2. Ginecologia\n3. Consulta general\n4. Maternidad\n5. Infancia\n6. Salir\n -> '))
        fnt_opcion(opcion)
        enter = input('\n <ENTER>')