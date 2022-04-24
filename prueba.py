import csv
import datetime
from queue import Empty

def requiredFields(row):
    try:
        if (row[2]==''):
            #Para este apartado podríamos tambien tener como obligatorio que la calle
            #tuviera al menos un nombre y un numero pero al no estar especificado en la 
            #prueba solo vemos que no esté vacio
            print("Street field was empty")
            return False
        if(int(row[3]) < 9999):
            #Para el zip veremos si el digito es menor que 5 digitos ya que es el minimo 
            #y a su vez en caso de que no sea un numero saltará la excepción
            return False 
        if(row[4]==''):
            #De la misma forma que la calle, podríamos añadir la complejidad de que en este apartado
            #el valor escrito pertenezca a una base de datos que almacena todas las cuidades, pero 
            #para hacerlo simple, vemos si está vacío el campo
            return False
        #Ahora simplemente trataremos de cambiar el formato str a date para ver si respeta el formato
        #, de no ser así, saltaría la excepción
        date_time_str = row[6]
        date_time_obj = datetime.datetime.strptime(date_time_str, '%d/%m/%Y')
        if (row[5]==''):
            #Por ultimo comprobaremos si el campo empresa está vacio
            return False
        #LLegados a este punto, si hemos pasado todos los if sin entrar a devolver, y en el código no
        #ha saltado ninguna excepcion, significará que nuestra fila cumple los requisitos de los
        #required files para que esta no sea ignorada, y por ello devolvemos True  
        return True
    except ValueError:
        print('salto la excepcion en required fields')
        return False
    except TypeError:
        print('excepcion de tipo')
        return False

def checkInAntiguo():
    with open('Sample test file - Sheet1.csv', newline='', encoding="utf8") as csvFile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='|')
        max = 0
        for row in reader :
            if(requiredFields(row)):
                if(row[0]!='First Name'):
                    try:
                        date_time_str = row[6]
                        date_time_obj = datetime.datetime.strptime(date_time_str, '%d/%m/%Y')
                        if(max==0):
                            max = date_time_obj
                        else:
                            if(max > date_time_obj):
                                max = date_time_obj
                    except ValueError:
                        print("erooor loco")
        print(max.date())

def checkInReciente():
    with open('Sample test file - Sheet1.csv', newline='', encoding="utf8") as csvFile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='|')
        min = 0
        for row in reader :
            if(requiredFields(row)):
                if(row[0]!='First Name'):
                    try:
                        date_time_str = row[6]
                        date_time_obj = datetime.datetime.strptime(date_time_str, '%d/%m/%Y')
                        if(min==0):
                            min = date_time_obj
                        else:
                            if(min < date_time_obj):
                                min = date_time_obj
                    except ValueError:
                        pass
        print(min.date())

def customersByOrder():
    with open('Sample test file - Sheet1.csv', newline='', encoding="utf8") as csvFile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='|')
        listCustomers = []
        for row in reader :
            if(requiredFields(row)):
                if(row[0]!='First Name'):
                    try:
                        if(row[0]!='' and row[1]!=''):
                            customer = f"{row[0]} {row[1]}"
                            listCustomers.append(customer)
                    except ValueError:
                        pass
        listCustomers.sort()
        print(listCustomers)


def main():
    checkInAntiguo()
    checkInReciente()
    customersByOrder()


if __name__ == "__main__":
    main()