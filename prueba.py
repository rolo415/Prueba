import csv
import datetime
import unicodedata
#Esta funcion nos devuelve un string sin acentos, es necesaria para la ordenacion de 
#clientes que veremos mas adelante
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def requiredFields(row):
    try:
        if (row[2]==''):
            #Para este apartado podríamos tambien tener como obligatorio que la calle
            #tuviera al menos un nombre y un número pero al no estar especificado en la 
            #prueba solo miramos que no esté vacio
            print("Street field was empty, row wont be read")
            return False
        if(int(row[3]) < 9999):
            #Para el zip veremos si el digito es menor que 5 digitos ya que es el minimo 
            #y a su vez en caso de que no sea un numero saltará la excepción
            print("Zip Code not Valid, row wont be read")
            return False 
        if(row[4]==''):
            #De la misma forma que la calle, podríamos añadir la complejidad de que en este apartado
            #el valor escrito pertenezca a una base de datos que almacena todas las cuidades, pero 
            #para hacerlo simple, vemos si está vacío el campo
            print('City field was empty, now wont be read')
            return False
        if(row[8]==''):
            print('Date field was empty, row wont be read')
        else:
            #Ahora simplemente trataremos de cambiar el formato str a date para ver si la fecha de esta fila 
            # respeta el formato date, de no ser así, saltaría la excepción
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
        print('ValueError exception, row wont be read')
        return False
    except TypeError:
        print('TypeError exception, row wont be read')
        return False

def checkInAntiguo():
    with open('Sample test file - Sheet1.csv', newline='', encoding="utf8") as csvFile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='|')
        max = 0
        for row in reader :
            #Vemos si la fila tiene los campos requeridos para continuar
            if(requiredFields(row)):
                #Evitamos leer la fila del header
                if(row[0]!='First Name'):
                    #En este caso el try/except no es necesario ya que capturamos las excepciones de las 
                    #fecha en la funcion requiredFields() pero lo usamos por buena praxis para futuras ocasiones
                    #donde no esten cubiertas las excepciones
                    try:
                        date_time_str = row[6]
                        date_time_obj = datetime.datetime.strptime(date_time_str, '%d/%m/%Y')
                        if(max==0):
                            max = date_time_obj
                        else:
                            if(max > date_time_obj):
                                max = date_time_obj
                    except ValueError:
                        print("Value error")
        print(f"\nCustomer con check-in mas antiguo: {max.date()}\n")

def checkInReciente():
    with open('Sample test file - Sheet1.csv', newline='', encoding="utf8") as csvFile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='|')
        min = 0
        for row in reader :
            #Vemos si la fila tiene los campos requeridos para continuar
            if(requiredFields(row)):
                #Evitamos leer la fila del header
                if(row[0]!='First Name'):
                    #En este caso el try/except no es necesario ya que capturamos las excepciones de las 
                    #fecha en la funcion requiredFields() pero lo usamos por buena praxis para futuras ocasiones
                    #donde no esten cubiertas las excepciones
                    try:
                        date_time_str = row[6]
                        date_time_obj = datetime.datetime.strptime(date_time_str, '%d/%m/%Y')
                        if(min==0):
                            min = date_time_obj
                        else:
                            if(min < date_time_obj):
                                min = date_time_obj
                    except ValueError:
                        print('ValueError')
        print(f"\nCustomer con check-in mas reciente: {min.date()}\n")

def customersByOrder():
    with open('Sample test file - Sheet1.csv', newline='', encoding="utf8") as csvFile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='|')
        listCustomers = []
        for row in reader :
            if(requiredFields(row)):
                if(row[0]!='First Name'):
                    try:
                        if(row[0]!='' and row[1]!=''):
                            #Para resolver la ordenacion me he dado cuenta de que el metodo sort() no era suficiente porque no tenía en cuenta
                            #los acentos y por ello Ángel Gavinet salía despues de Paul Hudson. Para arreglarlo usamos la operacion definida al 
                            #principio del codigo "strip_accents()"
                            customer = strip_accents(f"{row[0]} {row[1]}")
                            listCustomers.append(customer)
                    except ValueError:
                        pass
        listCustomers.sort()
        #Debido a que imprimimos por pantalla las excepciones he añadido en todos los print dos saltos 
        # de pagina para que se vea mejor en la ejecucion del programa 
        print(f"\nLista de Customers ordenada: {listCustomers}\n")


def main():
    checkInAntiguo()
    checkInReciente()
    customersByOrder()


if __name__ == "__main__":
    main()