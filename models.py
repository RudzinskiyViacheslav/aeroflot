import json
from datetime import datetime
from datetime import *

with open("data_file.json", "r") as write_file:
    DataBase = json.load(write_file)

def find_Flights(name = ''):
    data_return = []
    indexes_to_return = []
    i = 0

    for item in DataBase['flights']:
        temp = ''
        for key, value in item.items():
            if key == 'number':
                temp += "Рейс номер " + str(value)
            elif key == 'destination':
                temp += " в " + str(value)
            elif key == 'departure_time':
                temp += " " + str(value)
            elif key == 'stopover_points':
                temp += ' с пересадками: ' + str(value)
            elif key == 'flight_days':
                temp += '. Дни перелета: ' + str(value)
            elif key == 'free_seats':
                temp += ' (мест: ' + str(value) + ')'

        if name == '':
            indexes_to_return.append(i)

        if item['destination'] == name:
            data_return.append([temp, True, item['departure_time']])
            indexes_to_return.append(i)
        else:
            data_return.append([temp, False, item['departure_time']])

        i += 1
    return data_return, indexes_to_return

def sort(array, indexes):
    for i in range (len(array)-1):
        for j in range(len(array) - i - 1):
            if datetime.strptime(array[j][2], "%Y-%d-%m %H:%M") > datetime.strptime(array[j+1][2], "%Y-%d-%m %H:%M"):
                array[j], array[j + 1] = array[j + 1], array[j]
                indexes[j], indexes[j + 1] = indexes[j + 1], indexes[j]

    return array, indexes

def check_For_Value(flights):
    check_Flag = False

    for item in flights:
        if item[1] == True:
            check_Flag = True
    return check_Flag

def data_Rewrite():
    DB_Json = json.dumps(DataBase)

    with open("data_file.json", "w") as my_file:
        my_file.write(DB_Json)