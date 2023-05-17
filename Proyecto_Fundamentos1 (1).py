import numpy as np

#Areas predeterminadas
areas=[("CONSUMO"),("VESTIMENTA")]

#Categorias
consumo=[("CARNES"),("BEBIDAS")]
Vestimenta=[("CAMISAS"),("PANTALONES")]
catmas1=[]
catmas2=[]
catmas3=[]

#Inicio de la funcion de agregar categorias al area de CONSUMO  
def categoria_consumo():
                        
    print()
    print(f" ♝  Categorias del Aréa de {areas[0]} ♝")
    print()
                        
    for i in consumo:
        
        print(f"→ {i}")
                         
    print()       
                        
        
    preguntar=input("Ingresa el apelativo de la nueva CATEGORIA: ").upper()
    print()

    verificar_cat = preguntar
                    
    found = False

    for element in consumo:
                        
     if element == verificar_cat:
        found = True
        break
                            
    if found:
                    
        print("[-] Error, CATEGORIA EXISTENTE ")
                            
        categoria_consumo()
                        
    else:
                        
        consumo.append(preguntar)
        view=consumo.index(preguntar)
                                            
        if view<=4:
            print("¿Deseas agregar mas CATEGORIAS?")
            pedi_cat=input("Ingresa '1' SI\nIngresa '2' NO Y MENU DE APARTADO\n➤ ")
                                                  
            while pedi_cat!="1" and pedi_cat!="2":

                print("[-] Error, Ingresa uno de los numeros solicitados")
                print()
                pedi_cat=input("Ingresa '1' SI\nIngresa '2' NO Y MENU DE APARTADO\n➤ ")
                                                    
            if pedi_cat=="1":
                categoria_consumo()
                                    
            else:
                admin()
        else:
                        
            print(f" 🅧 YA NO PUEDES CREAR MAS CATEGORIAS EN {areas[0]} 🅧 ")
            consumo.remove(preguntar)
            print()
            admin()    
#FIN de la funcion de agregar categorias al area de CONSUMO                             

#INICIO de la funcion de agregar categorias al area de VESTIMENTAS
def categoria_vestimenta():
                        
    print()
    print(f" ♝  Categorias del Aréa de {areas[1]} ♝")
    print()
                        
    for i in Vestimenta:
        
         print(f"→ {i}")
                         
    print()       
                    
    preguntar=input("Ingresa el apelativo de la nueva CATEGORIA: ").upper()
    print()

    verificar_cat = preguntar
                    
    found = False

    for element in Vestimenta:
                        
        if element == verificar_cat:
          found = True
          break
                            
    if found:
                    
        print("[-] Error, CATEGORIA EXISTENTE ")
                            
        categoria_vestimenta()
                        
    else:
                                
        Vestimenta.append(preguntar)
        view=Vestimenta.index(preguntar)
                                            
        if view<=4:
            print("¿Deseas agregar mas CATEGORIAS?")
            pedi_cat=input("Ingresa '1' SI\nIngresa '2' NO Y MENU DE APARTADO\n➤ ")
                                
                                
            while pedi_cat!="1" and pedi_cat!="2":

                print("[-] Error, Ingresa uno de los numeros solicitados")
                print()
                pedi_cat=input("Ingresa '1' SI\nIngresa '2' NO Y MENU DE APARTADO\n➤ ")
                                                
            if pedi_cat=="1":
                categoria_vestimenta()
                                
            else:
                admin()
        else:
                    
            print(f" 🅧 YA NO PUEDES CREAR MAS CATEGORIAS EN {areas[1]} 🅧 ")
            Vestimenta.remove(preguntar)
            print()
            admin() 
#FIN de la funcion de agregar categorias al area de vestimentas               

#Funcion para agregar nueva categoria Num. caracter areas[2]
def cat_new1():

        print()
        print(f" ♝  Categorias del Aréa de {areas[2]} ♝")
        print()
                        
        for i in catmas1:
        
         print(f"→ {i}")
                 

        print()    
        preguntar=input("Ingresa el apelativo de la nueva CATEGORIA: ").upper()
        print()
        verificar_cat = preguntar
        
        found = False

        for element in catmas1:
            
                if element == verificar_cat:
                    found = True
                    break
                
        if found:
           
                print("[-] Error, CATEGORIA EXISTENTE ")
                
                cat_new1()
        else:
                catmas1.append(preguntar)
                view=catmas1.index(preguntar)
                                
                if view<=4:
                    print("¿Deseas agregar mas CATEGORIAS?")
                    pedi_cat=input("Ingresa '1' SI\nIngresa '2' NO Y MENU DE APARTADO\n➤ ")
                    
                    while pedi_cat!="1" and pedi_cat!="2":

                        print("[-] Error, Ingresa uno de los numeros solicitados")
                        print()
                        pedi_cat=input("Ingresa '1' SI\nIngresa '2' NO Y MENU DE APARTADO\n➤ ")
                                    
                    if pedi_cat=="1":
                        cat_new1()
                    
                    else:
                        admin()
                else:
        
                    print(F" 🅧 YA NO PUEDES CREAR MAS CATEGORIAS EN {areas[2]} 🅧 ")
                    catmas1.remove(preguntar)
                    print()
                    admin()       
#Funcion para agregar nueva categoria Num. caracter areas[2] FIN

#Funcion para agregar nueva categoria Num. caracter areas[3] INICIO
def cat_new2():

        print()
        print(f" ♝  Categorias del Aréa de {areas[3]} ♝")
        print()
                        
        for i in catmas2:
        
          print(f"→ {i}")
                 
        print()    
        preguntar=input("Ingresa el apelativo de la nueva CATEGORIA: ").upper()
        print()
        verificar_cat = preguntar
        
        found = False

        for element in catmas2:
            
                if element == verificar_cat:
                    found = True
                    break
                
        if found:
           
            print("[-] Error, CATEGORIA EXISTENTE ")
                
            cat_new2()
            
        else:
            
                catmas2.append(preguntar)
                view=catmas2.index(preguntar)
                                
                if view<=4:
                    print("¿Deseas agregar mas CATEGORIAS?")
                    pedi_cat=input("Ingresa '1' SI\nIngresa '2' NO Y MENU DE APARTADO\n➤ ")
                    
                    while pedi_cat!="1" and pedi_cat!="2":

                        print("[-] Error, Ingresa uno de los numeros solicitados")
                        print()
                        pedi_cat=input("Ingresa '1' SI\nIngresa '2' NO Y MENU DE APARTADO\n➤ ")
                                    
                    if pedi_cat=="1":
                        cat_new2()
                    
                    else:
                        admin()
                else:
        
                    print(f" 🅧 YA NO PUEDES CREAR MAS CATEGORIAS EN {areas[3]} 🅧 ")
                    catmas2.remove(preguntar)
                    print()
                    admin()      
#Funcion para agregar nueva categoria Num. caracter areas[3] FIN

#Funcion para agregar nueva categoria Num. caracter areas[4] INICIO
def cat_new3():

        print()
        print(f" ♝  Categorias del Aréa de {areas[4]} ♝")
        print()
                        
        for i in catmas3:
        
         print(f"→ {i}")
                
        print()    
        preguntar=input("Ingresa el apelativo de la nueva CATEGORIA: ").upper()
        print()
        verificar_cat = preguntar
        
        found = False

        for element in catmas3:
            
                if element == verificar_cat:
                    found = True
                    break
                
        if found:
           
                print("[-] Error, CATEGORIA EXISTENTE ")
                cat_new3()
        else:
            
                catmas3.append(preguntar)
                view=catmas3.index(preguntar)
                                
                if view<=4:

                    print("¿Deseas agregar mas CATEGORIAS?")
                    pedi_cat=input("Ingresa '1' SI\nIngresa '2' NO Y MENU DE APARTADO\n➤ ")
                    
                    while pedi_cat!="1" and pedi_cat!="2":

                        print("[-] Error, Ingresa uno de los numeros solicitados")
                        print()
                        pedi_cat=input("Ingresa '1' SI\nIngresa '2' NO Y MENU DE APARTADO\n➤ ")
                                    
                    if pedi_cat=="1":
                        cat_new3()
                    
                    else:
                        admin()
                else:
        
                    print(f" 🅧 YA NO PUEDES CREAR MAS CATEGORIAS EN {areas[4]} 🅧 ")
                    catmas3.remove(preguntar)
                    print()
                    admin()      
#Funcion para agregar nueva categoria Num. caracter areas[4] FIN

#Metodo para agregar mas areas Inicio
def agregar_areas():
    
            print()    
            preguntar=input("Ingresa el apelativo de la nueva Aréa: ").upper()
            print()
            
            verificar_area= preguntar
        
            found = False

            for element in areas:
            
                if element == verificar_area:
                    found = True
                    break
                
            if found:
           
                print("[-] Error, ARÉA EXISTENTE ")
                
                agregar_areas()
            
            else:
            
                areas.append(preguntar)
                view=areas.index(preguntar)
                                
                if view<=4:
                    print("¿Deseas agregar mas ARÉAS?")
                    pedi_area=input("Ingresa '1' SI\nIngresa '2' NO Y MENU DE APARTADO\n➤ ")
                    
                    while pedi_area!="1" and pedi_area!="2":

                        print("[-] Error, Ingresa uno de los numeros solicitados")
                        print()
                        pedi_area=input("Ingresa '1' SI\nIngresa '2' NO Y MENU DE APARTADO\n➤ ")
                                    
                    if pedi_area=="1":
                        agregar_areas()
                    
                    else:
                        admin()
                else:
        
                    print(" 🅧 YA NO PUEDES CREAR MAS AREAS 🅧 ")
                    areas.remove(preguntar)
                    print()
                    admin() 
#Metodo para agregar mas areas Fin
                  
#INICIO del apartado de productos                                  
def productos():
    
    print()
    print("♖  PRODUCTOS  ♖")
    print()
    ver=input("Digita '1' AGREGAR PRODUCTOS\n"
              "Digita '2' BORRAR PRODUCTOS\n"
              "Digita '3' REGRESAR\n")
    
    while ver!="1" and ver!="2" and ver!="3":
        print("[-] Error, Ingresa uno de los numeros solicitados")
        print()
        print(" ♖   PRODUCTOS  ♖")
        print()
        ver=input("Digita '1' AGREGAR PRODUCTOS\n"
              "Digita '2' BORRAR PRODUCTOS\n"
              "Digita '3' REGRESAR\n➤ ")

    if ver=="1":
        def agregar_pro():
            
            data = np.loadtxt('Productos.txt', dtype=object, delimiter=',')

            print()
            print("✩  Agregar NUEVOS PRODUCTOS ✩")
            print()
                
            print(f"Productos Actuales:\n{data}")
            print()
                
            Nombre = input("Nombre del Producto ➤ ")
            print()
            Proveedor = input("Proveedor de Producto ➤ ")
            print()
            Fecha=input("Fecha de Incorporacion del Producto ➤ ")
            print()
            Detalles=input("Descripcion del Producto ➤ ")
            print()
            PRECIO=float(input("Precio del Producto ➤ "))
            print()
            Cantidad=int(input("Cantidad de Productos ➤ "))
            print()
            
            NuevoProducto = np.array([[Nombre, Proveedor,Fecha,Detalles,PRECIO, Cantidad]], dtype=object)
            data = np.vstack((data, NuevoProducto))
            np.savetxt('Productos.txt', data, delimiter=',', fmt='%s')
            print(f"✩ Productos Actuales ✩\n {data}")
            print()
            averi=input("¿Deseas agregar otro PRODUCTO (si/no)?\n ➤ ").lower()
             
            while averi!="si" and averi!="no":
                print("[-] ERROR, ingresa una respuesta concreta") 
                print()
                averi=input("¿Deseas agregar otro PRODUCTO (si/no)?\n ➤ ").lower()
                
            if averi=="si":
                agregar_pro()
            else:
                productos()
                
        agregar_pro()        

    elif ver=="2":
         
        def borrar_pro():
            data = np.loadtxt('Productos.txt', dtype=object, delimiter=',')
            contador=0
            print()
            print("  ♝  Productos Actuales ♝")
            print()

            for i in data:
                contador+=1
                nuevo=contador-1
                
                print(f"{nuevo} {i}")
                
            print()     
        
            delete=input("Ingresa el numero del CARACTER que quieres BORRAR ✂\n ➤ ")
            
            while delete.isdigit()!=True or delete=="0":
                print("[-] Error, Digita un numero entre los solicitados")
                print()
                delete=input("Ingresa el numero del CARACTER que quieres BORRAR ✂\n ➤ ")
                print()
            
            cara2=int(delete)+1
            
            if cara2>len(data) or cara2<=0:
                print("✖  Producto no Existente  ✖")
                borrar_pro()
                
            else:
                data=np.delete(data,[int(delete)][:],axis=0)
                np.savetxt('Productos.txt', data, delimiter=',', fmt='%s')
                print(" ✓ Producto Eliminado ✓")
                print()
                print(f"✩ Productos Actuales ✩\n {data}")
                print()           
                averi=input("¿Deseas eliminar otro PRODUCTO (si/no)?\n ➤ ").lower()
             
                while averi!="si" and averi!="no":
                    print("[-] ERROR, ingresa una respuesta concreta") 
                    print()
                    averi=input("¿Deseas eliminar otro PRODUCTO (si/no)?\n ➤ ").lower()
                    
                if averi=="si":
                    borrar_pro()
                else:
                    productos()
                
        borrar_pro()  
        
    else:
        admin()    
#Fin del  apartado de productos  
               #Solo entrar admin Fin
               
#Menu del gerente Inicio
def gerente():
    print()
    print("   ♟  Menú de Apartados  ♟")
    print()
    menuG="Digita '1' ➾  Ver Aréas\nDigita '2' ➾  Ver Categorías\nDigita '3' ➾  Ver Productos\nDigita '4' ➾  Ver Ventas\nDigita '5' ➾  Regresar MENÚ\n"
    print(menuG)
        
    pide_area=input("Ingresa el numero del Apartado que quieres consultar ➤ ")

    while pide_area!="1" and pide_area!="2" and pide_area!="3" and pide_area!="4" and pide_area!="5":

     print("[-] Error, Ingresa uno de los numeros solicitados")
     print()
     pide_area=input("Ingresa el numero del apartado que quieres consultar ➤ ")

    if pide_area=="1":
              
        print()
        print("  ✤  ARÉAS ACTUALES ✤ \n")
        
        for i in areas:
    
          print(f"✓ {i}")

        print("\n¿Regresar MENU DE APARTADOS?")
        dato=input("Ingresa '1' SI.\nIngresa '2' NO y salir.\n➤ ")
                    
                    
        while dato!="1" and dato!="2":

            print("[-] Error, Ingresa uno de los numeros solicitados")
            print()
            dato=input("Ingresa '1' SI\nIngresa '2' NO y salir\n➤ ")
                                    
        if dato=="1":
            gerente()
                    
        else:
            print()
            print("Fin del programa.")

    elif pide_area=="2":
              
        print()
        print("  ✤  CATEGORIAS ACTUALES ✤ \n")
        
        for i in consumo, Vestimenta, catmas1, catmas2, catmas3:
    
          print(f"✓ {i}")
          
        print("\n¿Regresar MENU DE APARTADOS?")
        dato=input("Ingresa '1' SI.\nIngresa '2' NO y salir\n➤ ")
                                
        while dato!="1" and dato!="2":
            print("[-] Error, Ingresa uno de los numeros solicitados")
            print()
            dato=input("Ingresa '1' SI\nIngresa '2' NO y salir\n➤ ")
                                    
        if dato=="1":
            gerente()
                    
        else:
            print()
            print("Fin del programa.")
            
    elif pide_area=="3":
        
        data = np.loadtxt('Productos.txt', dtype=object, delimiter=',')
        print()
        print(f"✩ Productos Actuales ✩\n\n {data}")
        print()
        print("¿Regresar MENU DE APARTADOS?")
        dato=input("Ingresa '1' SI.\nIngresa '2' NO y salir\n➤ ")
                               
        while dato!="1" and dato!="2":
            print("[-] Error, Ingresa uno de los numeros solicitados")
            print()
            dato=input("Ingresa '1' SI\nIngresa '2' NO y salir\n➤ ")
        
        if dato=="1":
            gerente()

        else:
            print()
            print("Fin del Programa")
            
    elif pide_area=="4":
        
        ventas = np.loadtxt('Ventas.txt', dtype=object, delimiter=',')
        
        print("\n ✉  Productos Vendidos ✉")
        print(f"\n {ventas}")
        
        print("\n¿Regresar MENU DE APARTADOS?")
        dato=input("Ingresa '1' SI.\nIngresa '2' NO y salir\n➤ ")
                                
        while dato!="1" and dato!="2":
            print("[-] Error, Ingresa uno de los numeros solicitados")
            print()
            dato=input("Ingresa '1' SI\nIngresa '2' NO y salir\n➤ ")
                                    
        if dato=="1":
            gerente()
                    
        else:
            print()
            print("Fin del programa.")
        
    elif pide_area=="5":
        consulta()
        print()
#Menu del gerente Inicio

#Varible para tomar los valores del final total pagar
totalPagar=[] 

#Variable para hacer el listado de compras
recibo=[]

#Inicio de la funcion venta
def vendedor():
    
    print("  ☸  Venta de Productos ☸")
        
    data = np.loadtxt('Productos.txt', dtype=object, delimiter=',')
    print()
    contador=0
    for i in data:
        contador+=1
        nuevo=contador-1       
        print(f"{nuevo} {i}")

    data = np.loadtxt('Productos.txt', dtype=object, delimiter=',')    
    print()    
    caracter=input("Ingresa el numero del caracter donde se encuentra el producto ➤ ")

    while caracter.isdigit()!=True or caracter=="0" :
        print("[-] Error, Ingresa un numero de caracter valido o mayor a 1.")
        print()
        caracter=input("Ingresa el numero del caracter donde se encuentra el producto ➤ ")

    cara2=int(caracter)+1
          
    if cara2>len(data) or cara2<=0:
        print()
        print("✖  Producto no Existente  ✖")
        print()
        vendedor()
        
    else:    
        PRODUCTO=data[int(caracter)][0]
        PRECIO=data[int(caracter)][4]
        
        print()
        print(f"☸  Unidades disponibles: {data[int(caracter)][5]}")
        print(f"☸  Producto: {PRODUCTO}\n☸  PRECIO: ${PRECIO}")
        print()
        UNIDADES=input("Ingresa la cantidad de unidades que deseas ➤ ")
        
        disponible=data[int(caracter)][5]
        
        while UNIDADES.isdigit()!=True or UNIDADES<="0" or int(UNIDADES)>int(disponible):
            print("[-] Error, Ingresa numeros mayores a CERO o menores a la Cantidad Disponible\n")
            UNIDADES=input("Ingresa la cantidad de unidades que deseas ➤ ")
            
        datonuevo=int(data[int(caracter)][5]) - int(UNIDADES)
        data[int(caracter)][5]=datonuevo
        np.savetxt('Productos.txt', data, delimiter=',', fmt='%s')
        print()
                 
        if data[int(caracter)][5]<=0:
            PAGAR=(float(PRECIO)*int(UNIDADES))
            totalPagar.append(PAGAR)
            print(f"☸  Total del producto ${PAGAR}\n")
            data=np.delete(data,[int(caracter)][:],axis=0)
            np.savetxt('Productos.txt', data, delimiter=',', fmt='%s')
            
        elif data[int(caracter)][5]>0:
            PAGAR=(float(PRECIO)*int(UNIDADES))
            totalPagar.append(PAGAR)
            print(f"☸  Total del producto ${PAGAR}")
            print()
        
        ventas = np.loadtxt('Ventas.txt', dtype=object, delimiter=',')

        NuevaVenta = np.array([[PRODUCTO,UNIDADES,PAGAR]], dtype=object)
        ventas = np.vstack((ventas, NuevaVenta))
        np.savetxt('Ventas.txt', ventas, delimiter=',', fmt='%s')
    
        regre_compra=input("¿Deseas comprar mas productos?\nDigita '1' ➾  SI\nDigita '2' ➾  Cancelar Productos\n➤ ")
                
        recibo.append([PRODUCTO,UNIDADES,PAGAR])
        
        while regre_compra!="1" and  regre_compra!="2" :
                print("[-] Error, Ingresa un numero de caracter valido.")
                print()
                regre_compra=input("¿Deseas comprar mas productos?\nDigita '1' ➾  SI\nDigita '2' ➾  Cancelar Compras\n➤ ")
        
        if regre_compra=="1":
            print()
            vendedor()
        else:
            pago=0
            
            pago=sum(totalPagar)
        
            print("\n☑  Carrito de Compras  ☑\n")
            for i in recibo:
                print(f"{i}")
                
            print(f"\nTotal a pagar es de ${pago}")
            
            def cancelar():
                
                efectivo=input("\nIngresa la cantidad de dinero a cancelar la cuenta:\n➤  $")    
                
                while efectivo.isdigit()!=True:
                    print("[-] Error, Dato no valido\n")
                    efectivo=input("Ingresa la cantidad de dinero a cancelar la cuenta:\n➤  $")    
                
                if float(efectivo)<pago:
                    
                    print("\n [-] Error, Pago Insuficiente...")
                    cancelar()
                    
                    
                elif float(efectivo)==pago:
                    
                    print("\n Gracias Por tu compra, Vuelve Pronto...")
                    print(f"\n ❋  Tus compras son  ❋\n")
                    
                    for i in recibo:
                        print(f"{i}")
                    
                elif float(efectivo)>pago:
                    
                    vuelto=float(efectivo)-float(pago)
                    print(f"\n Tu cambio es de: ${vuelto}")
                    print("\n Gracias Por tu compra, Vuelve Pronto...")
                    print(f"\n ❋  Tus compras son  ❋\n")
                    
                    for i in recibo:
                        print(f"{i}")
                                           
                volver=input("\n¿Deseas regresar al MENU?\nDigita '1' SI\n"
                      "Digita '2' NO y FINALIZAR\n➤ ")  
                                
                while volver!="1" and volver!="2":
                    print("\n[-] Error, Ingresa un numero solicitado")
                    volver=input("\n¿Deseas regresar al MENU?")  
                                
                if volver=="1":
                    print()
                    recibo.remove([PRODUCTO,UNIDADES,PAGAR])
                    totalPagar.remove(PAGAR)
                    consulta()
                                                        
                else:
                    print("\nFin del Programa")        
                                           
            cancelar()         
#FIn de la funcion venta  

#Menu del admin Inicio                  
def admin():
    print("  ♟  Menú de Apartados ♟")
    print()
    menu2="Digita '1' ➾  Creacion de Aréas\nDigita '2' ➾  Creacion de Categorías\nDigita '3' ➾  Productos Agregar/Eliminar\nDigita '4' ➾  MENU PRINCIPAL\n"
    print(menu2)
        
    pedi_area=input("Ingresa el numero del Apartado que quieres consultar ➤ ")

    while pedi_area!="1" and pedi_area!="2" and pedi_area!="3" and pedi_area!="4":

     print("[-] Error, Ingresa uno de los numeros solicitados")
     print()
     pedi_area=input("Ingresa el numero del apartado que quieres consultar ➤ ")
    

    if pedi_area=="1":
              
        print()
        print("  ✤  ARÉAS ACTUALES ✤ \n")
        
        for i in areas:
    
          print(f"✓ {i}")
     
        agregar_areas()
           
    elif pedi_area=="2":
        
        print()
        print("  ✤  ARÉAS PARA CATEGORIAS  ✤ \n")
        
        for i in areas:
    
          print(f"✓ {i}")
          
        print()  
        
        pedir=input("Ingresa el apelitivo del Aréa que deseas agregar Categorias ➤ ").upper()
        
        detener=True
            
        while detener:
            
         try:
                pedir in areas
                view=areas.index(pedir)
                detener=False
                               
                if view==0:
                    categoria_consumo()
                                
                elif view==1:                                
                    categoria_vestimenta()
                                                     
                elif view==2:
                    cat_new1()

                elif view==3: 
                    cat_new2()

                elif view==4: 
                    cat_new3()
         except:
                print("[-] ERROR, ingresa una aréa compatible") 
                print()
                pedir=input("Ingresa el apelitivo del Aréa que deseas agregar Categorias ➤ ").upper()
                
    elif pedi_area=="3":
        productos()
    
    elif pedi_area=="4":
          consulta()
          print()
    
 #Solo entrar admin Fin
#Menu del admin Fin

#Menu principal Inicio
def consulta():
    
    global contraseña   
    
    print("\n    Menú de Navegación ✈")
    print()             
    
    Menu=" Digita '1' ➾  INGRESAR O CREAR DATOS\n Digita '2' ➾  OBTENER DATOS\n Digita '3' ➾  REALIZAR VENTAS\n Digita '4' ➾  CAMBIAR DE USUARIO\n Digita '5' ➾  SALIR DEL PROGRAMA"

    print(Menu)
    print()

    dato=input("Ingresa el numero del departamento que quieres consultar ➤ ")

    while dato!="1" and dato!="2"  and dato!="3" and dato!="4" and dato!="5":

     print("[-] Error, Ingresa uno de los numeros solicitados")
     print()
     dato=input("Ingresa el numero del departamento que quieres consultar ➤ ")
    
    #ad:123
    #ger:132
    #ven:321
    
    if dato=="1" and contraseña=="123": 
        print()
        admin()
    
    elif dato=="1" and contraseña=="132" or dato=="1" and contraseña=="321":  
        print()
        print(" ✖  NO TIENES PERMISOS  ✖") 
        consulta()     
        
    elif dato=="2" and contraseña=="123" or dato=="2" and contraseña=="132":
        gerente()
         
    elif dato=="2" and contraseña=="321":
        print()
        print(" ✖  NO TIENES PERMISOS  ✖")
        consulta()  
        
    elif dato=="3" and contraseña=="123" or dato=="3" and contraseña=="321":
        print()
        vendedor()
        
    elif dato=="3" and contraseña=="132":
        print()
        print(" ✖  NO TIENES PERMISOS  ✖")
        consulta()
        
    elif dato=="4":
        usuario()
    else:
        print()
        print("Fin del Programa.")
#Menu principal FIn

#Login INicio
def usuario():
    
    print("\n************************************")
    print("         ~~~~ LOGIN ~~~~")
    print("************************************\n")
    menu=input("Nombre de Usuario:\n▶ ").lower()

    while menu!="admin" and menu!="gerente" and menu!="vendedor":
        print("[-] Error, Ingresa un cargo compatible\n")
        menu=input("Nombre de Usuario:\n▶ ").lower()
        
    global contraseña

    contraseña=input("\nPor favor, Ingresa tu contraseña:\n▶ ")
    
    if menu=="admin" and contraseña=="123":
        consulta()
       
    elif menu=="gerente" and contraseña=="132":
         consulta()
       
    elif menu=="vendedor" and contraseña=="321":
         consulta() 
    else:
        print()
        print("[-] Error, Contraseña Incorrecta.. ")
        print()
        usuario()  
#Login Fin     
usuario()

#Funcion global para poder utilizarla en las demas funciones
global contraseña
