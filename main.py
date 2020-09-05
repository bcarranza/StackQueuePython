print("DEMOSTRACION DE PILAS Y COLAS")
while True:
    print("1. Pilas")
    print("2. Colas")
    print("3. Salir")
    print("Seleccione la opción deseada: ")
    op=input()
    if(op=="1"):
        #Declarando la pila
        stack = []
        while True:
            print("1. Apilar")
            print("2. Desapilar")
            print("3. Desapilar todo")
            print("4. Regresar al menu anterior")
            print("Seleccione la opción deseada: ")
            op2=input()

            if(op2=="1"):
                print("Ingrese el valor a apilar")
                value=input()
                stack.append(value)
                print("Valor ingresado con éxito presione una tecla para continuar ......")
            elif(op2=="2"): 
                if(len(stack)==0):
                    print("No es posible desapilar, ya que la pila se encuentra vacia")
                else:
                    print("Valor desapilado: " + stack.pop())
            elif(op2=="3"): 
                c=len(stack)
                print("Desapilando todos los valores")
                print("-----------------------------")
                for x in range(c):
                    print("Valor desapilado: " + stack.pop())
                print("Todos los valores fueron desapilados con exito.")
            elif(op2=="4"): 
                print("Retornando al menu anterior")
                break
            else:
                print("Opción invalida intente una nueva opción")        
            input("Press Enter to continue...")
    elif(op=="2"):
        queue = []
        while True:
            print("1. Encolar")
            print("2. Desencolar")
            print("3. Desencolar todo")
            print("4. Regresar al menu anterior")
            print("Seleccione la opción deseada: ")
            op2=input()
            if(op2=="1"):
                print("Ingrese el valor a encolar")
                value=input()
                queue.append(value)
                print("Valor ingresado con éxito presione una tecla para continuar ......")
            elif(op2=="2"): 
                if(len(queue)==0):
                    print("No es posible desencolar, ya que la cola se encuentra vacia")
                else:
                    print("Valor desencolado: " + queue.pop(0))
            elif(op2=="3"): 
                c=len(queue)
                print("Desencolando todos los valores")
                print("-----------------------------")
                for x in range(c):
                    print("Valor desencolado: " +  queue.pop(0))
                print("Todos los valores fueron desencolados con exito.")
            elif(op2=="4"): 
                print("Retornando al menu anterior")
                break
            else:
                print("Opción invalida intente una nueva opción")        
            input("Press Enter to continue...")
    if(op=="3"):
        print("Hasta luego!!")
        break
    input("Press Enter to continue...")