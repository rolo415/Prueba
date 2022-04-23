import csv
import datetime

def requiredFields(row):
    try:
        
        
        print('hola')
    except ValueError:
        print('hola')

    return 

def checkInAntiguo():
    with open('Sample test file - Sheet1.csv', newline='', encoding="utf8") as csvFile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='|')
        max = 0
        for row in reader :
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
                    print("")
        print(max.date())

def checkInReciente():
    with open('Sample test file - Sheet1.csv', newline='', encoding="utf8") as csvFile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='|')
        min = 0
        for row in reader :
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

def main():
    checkInAntiguo()
    checkInReciente()


if __name__ == "__main__":
    main()