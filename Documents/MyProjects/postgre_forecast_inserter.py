import psycopg2
import random
import math

#Задача - нагенерить 50+ форекастов каждому городу

# Задаем данные для вставки
#data = [(1003, 'Novosibirsk')]
#print(type(data[0]))
def generateRandomNumber(digits):
    finalNumber = ""
    for i in range(digits // 16):
        finalNumber = finalNumber + str(math.floor(random.random() * 10000000000000000))
    finalNumber = finalNumber + str(math.floor(random.random() * (10 ** (digits % 16))))
    return int(finalNumber)

def inserter(data):
    try:
        # Подключаемся к базе данных
        conn = psycopg2.connect("dbname='weather2' user='postgres' host='91.185.84.156' port=5000 password='Valenok18'")
        cursor = conn.cursor()

        # Создаем команду SQL для вставки данных
        insert_query = """INSERT INTO public.forecast ("id", "cityId", "dateTime", "temperature", "summary") VALUES %s"""
        print(insert_query)
        # Строим кортеж параметров для команды SQL
        parameters = tuple(data)
        print(parameters)
        print(type(parameters))
        # Выполняем команду SQL
        cursor.execute(insert_query, parameters)

        # Сохраняем изменения на сервере
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()



cities=["SaintPetersburg","Novosibirsk","Ekaterinburg","Kazan","NighniiNovgorod","Chelyabinsk","Krasnoyarsk","Samara","Ufa","Rostov","Krasnodar","Voronezh","Volgograd","Donetsk","Saratov","Tyumen","Togliatti","Barnaul","Izhevsk","Makhachkala","Khabarovsk","Ulyanovsk","Irkutsk","Vladivostok","Yaroslavl","Kemerovo","Tomsk","NaberezhnyeChelny","Sevastopol","Stavropol","Orenburg","Novokuznetsk","Ryazan","Penza"]
start_id=1004
idid=4
data=[]
weather_statuses=["Солнечно","Пасмурно","Осадки","Сильный ветер","Затмение","Переменная облачность","Штиль"]

#температура от -50 до +50

for city in cities:
    for i in range(50):
        temperature=int(100*random.random())-50
        weather_status=random.choice(weather_statuses)
        bigserial=generateRandomNumber(16)
        data.append(tuple([idid,start_id,bigserial,temperature,weather_status]))
        inserter(data)
        data=[]
        idid += 1
        i += 1
    start_id += 1
    

print(type(data))