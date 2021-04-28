#  =================================================================================================================
#           
#           Universidad del Valle de Guatemala, Algoritmos y Programación Básica
#           Semestre 1 2021
#                           ____
#                          / . .\
#                          \  ---<
#                           \  /
#                ___________/ /
#               /____________/. ... ..     ...      ..... ...   . . .  ... . 
#
#           Ejercicio 4: Persistencia
#           Juan Pablo Muralles ©
#
#  ==================================================================================================================
from datetime import datetime
import time
import csv

#time = 0
class bcolors:
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKCYAN = '\033[96m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   ENDC = '\033[0m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
    
def startT():
    creportG()
    instanteInicial = datetime.now()
    print("Press any key when you finish")
    key = input()
    instanteFinal = datetime.now()
    tiempo = instanteFinal - instanteInicial
    segundos = tiempo.seconds
    minutos = segundos/60
    today = int(minutos)
    success = ""
    if today >= 30:
        succes = "Succesful"
    else:
        succes = "Failed"
    date = time.ctime()
    date = date.split()
    date = date[0] +"-"+ date[1]+"-"+ date[2] 
    print(date)
    reader = csv.DictReader(open("users.csv"))
    for raw in reader:
        a = raw['Age']
        w = raw['Weigth']
        h = raw['Heigth']
        n = raw['Name']
        lista = [date,n,a,w,h,instanteInicial,instanteFinal,today,succes]
        print(a,w,h)
        files = open('generalReport.csv', 'a', encoding='utf-8', newline='')
        csvwriter = csv.writer(files) 
        csvwriter.writerow(lista)
        files.close()
        menu2()
def register():
    try:
            print(f"{bcolors.HEADER}REGISTER{bcolors.ENDC}")
            print("Enter your name")
            name = str(input())
            print("Enter your age")
            age = int(input())
            if age <4 or age >110:
                print (f"{bcolors.FAIL}please enter a valid value{bcolors.ENDC}")
                age = int(input())
            print("Enter your weigth (Pounds)")
            weigth = float(input())
            #csvwrite.writerows(rows)
            #csvwrite.writerows(rows)
            #csvwrite.writerows(rows)
            if weigth > 1199.31 or weigth < 25:
                print(f"{bcolors.FAIL}please enter a valid value{bcolors.ENDC}")
                weigth = float(input())
            print("Enter your heigth (Centimeters)")
            heigth = int(input())
            if heigth <90 or heigth > 230:
                print (f"{bcolors.FAIL}please enter a valid value{bcolors.ENDC}")
                heigth = int(input())
            users = [name,str(age),str(weigth),str(heigth)]
            print(f"{bcolors.OKGREEN}User created ✔{bcolors.OKBLUE}\nPlease login with your new user :){bcolors.ENDC}")
            files = open('users.csv', 'a', encoding='utf-8', newline='')
            csvwriter = csv.writer(files) 
            csvwriter.writerow(users)
            files.close()
            menu()
    except:
            print (f"{bcolors.FAIL}please enter a valid value{bcolors.ENDC}")
def menu2():
    print(f"{bcolors.OKCYAN}Menu{bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}Select a option{bcolors.ENDC}\na) start training\nb) view progres\nc) return to main menu")
    select = input()
    if select.lower() == "a":
        startT()    
    elif select.lower() == "b":
        print("b selected")
    elif select.lower() == "c":
        menu()

def login():
    print(f"{bcolors.HEADER}LOGIN{bcolors.ENDC}")
    print("Insert your name")
    x = input()
    nameS = x
    line_count = 0
    result = [] 
    reader = csv.DictReader(open("users.csv")) #Solucionar, problema al leer: solo accede a la primera fila.
    for raw in reader:
        a = raw['Name']
        print(result)
        if x == a:
            menu2()
            return a
        else:
            print(x + " does not exist, do you want to register it? [Y/n]")
            selector = input()
            if selector.lower() == "y":
                register() 
            else: 
                menu()
def createDB():    #crea el CSV donde se guardan todos los usuarios.
    try:
        with open('users.csv', 'r') as file:
            reader = csv.reader(file)                       #Si ya existe un archivo, lo abre
    except:
        fields = ['Name', 'Age', 'Weigth', 'Heigth']
        filename = "users.csv"
        with open(filename, 'w') as csvfile:
            csvwrite = csv.writer(csvfile)                  # si no existe lo crea, de esta manera evitamos 
            csvwrite.writerow(fields)                       # eliminar el archivo cada ves que iniciemos.
            #csvwrite.writerows(rows)
def creportG():
    fields = ['date','name','age','weigth','heigth','start','end','time','success']
    filename = "generalReport.csv"
    with open(filename,'a')as reportg:
        csvwrite = csv.writer(reportg)
        csvwrite.writerow(fields)
def menu():
    createDB()
    wa = 0
    while wa == 0:
        print(f"{bcolors.HEADER}Wellcome, please select a option{bcolors.ENDC}\n a)Register\n b)Login\n c) exit")
        option = str(input())
        if option.lower() == "a":
            register()
            wa = 1
        elif option.lower() == "b":
            login()
            wa = 1
        elif option.lower() == "c":
            exit()
        else:
            print("plese select a valid option")

menu()       
