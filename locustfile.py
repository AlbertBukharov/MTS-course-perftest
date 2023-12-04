from locust import HttpUser, task, between
import random
import json

class MyLocust(HttpUser):
    def on_start(self):
        self.headers = {
            'Host': 'alb-sre.lol',
        }
        self.headers_put = {
            'Host': 'alb-sre.lol',
            'Content-Type': 'application/json',
        }
### CITIES SECTION
    #GET /Cities
    @task(20)    #будем считать, что частота использования запроса - средняя = 20
    def get_cities(self):
        self.client.get("/cities", headers=self.headers)

    #GET /Cities/{id}
    @task(20)    #будем считать, что частота использования запроса - средняя = 20
    def get_cities_w_id(self):
        url_randomcityid="/cities/"+str(1000+random.randint(1,37))
        self.client.get(url_randomcityid, headers=self.headers)
    
    #PUT /Cities/{id}
    @task(5)    #будем считать, что частота использования запроса - редкая = 5
    def put_cities_w_id(self): #тестовый город с id=1003
        payload = {'name': random.choice(['testcity','TestCity','Test-City','City Test'])}
        url_putcityid="/Cities/1003"
        self.client.put(url_putcityid, data=json.dumps(payload), headers=self.headers_put)

    #POST /Cities
    @task(1)    #будем считать, что частота использования запроса - очень редкая = 1
    def post_cities(self): #создание тестового города с id по порядку
        payload = {'name': random.choice(['testcity','TestCity','Test-City','City Test'])}
        url_postcity = "/Cities"
        self.client.post(url_postcity, data=json.dumps(payload), headers=self.headers_put)

### FORECAST SECTION
    #GET /Forecast
    @task(5)    #будем считать, что частота использования запроса - редкая = 5
    def get_forecast(self):
        self.client.get("/Forecast", headers=self.headers)

    #PUT /Forecast/{id}
    @task(1)    #будем считать, что частота использования запроса - очень редкая = 1 (зачем менять прогноз)
    def put_forecast_w_id(self):
        data_forecastid = {"id": 1003, "cityId": 1003, "dateTime": str(5550000 + random.randint(1,5000)), "temperature": 55, "summary" : "test test"}
        url_randomforecastid="/Forecast/1003"
        self.client.put(url_randomforecastid, data=json.dumps(data_forecastid),headers=self.headers_put)
    

    #POST /Forecast/{cityId}
    @task(5)    #будем считать, что частота использования запроса - редкая = 5
    def post_forecastcity(self): #создание тестового города с id по порядку
        data_forecastid = {"id": 1003, "cityId": 1003, "dateTime": str(5550000 + random.randint(1,5000)), "temperature": 55, "summary" : "test test"}
        url_postforecastcity = "/Forecast/1003"
        self.client.post(url_postforecastcity, data=json.dumps(data_forecastid), headers=self.headers_put)

    #GET /Forecast/{id}
    @task(1)    #будем считать, что частота использования запроса - очень редкая = 1 (дергать по ID - редкость)
    def get_forecastid(self):
        url_randomforecastid="/Forecast/"+str(random.randint(10,1000))
        self.client.get(url_randomforecastid, headers=self.headers)

### WEATHER FORECAST
    #GET /WeatherForecast
    @task(200)    #будем считать, что частота использования запроса - очень частая = 200
    def get_weatherfcast(self):
        self.client.get("/WeatherForecast", headers=self.headers)


if __name__ == '__main__':
    locust = MyLocust()
    locust.run_simulations(10, 1, name='MyHeaderLocust')