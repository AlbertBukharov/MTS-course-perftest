import psycopg2

# Задаем данные для вставки
#data = [(1003, 'Novosibirsk')]
#print(type(data[0]))


def inserter(data):
    try:
        # Подключаемся к базе данных
        conn = psycopg2.connect("dbname='weather2' user='postgres' host='91.185.84.156' port=5000 password='Valenok18'")
        cursor = conn.cursor()

        # Создаем команду SQL для вставки данных
        insert_query = "INSERT INTO public.cities (id, name) VALUES %s"
    #    print(insert_query)
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
data=[]

for city in cities:
    data.append(tuple([start_id,city]))
    inserter(data)
    start_id += 1
    data=[]

print(type(data))