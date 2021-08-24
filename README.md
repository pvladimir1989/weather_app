# weather_app
Для запуска приложения:
1.git clone https://github.com/pvladimir1989/weather_app.git

2.В корне проекта weather_app меняем название файла example.env на .env

3.Устанавливаем Docker

4.Из командной строки/терминала IDE заходим в папку weather_app и выполняем команду docker-compose up --build

5.Запустится http://0.0.0.0:8000

6.http://0.0.0.0:8000/v1/city/  -   route для GET-запроса 

7.Вернутся следующие значения 

[

    {
    
        "id": 61,
        
        "city": "Novosibirsk",
        
        "time": "2021-08-23T18:17:13Z",
        
        "longitude": 82.9344,
        
        "latitude": 55.0411,
        
        "temperature": 63.7
        
    },
    
    {
    
        "id": 62,
        
        "city": "Saint Petersburg",
        
        "time": "2021-08-23T18:07:10Z",
        
        "longitude": 30.2642,
        
        "latitude": 59.8944,
        
        "temperature": 51.94
        
    },
    
    {
    
        "id": 63,
        
        "city": "Delhi",
        
        "time": "2021-08-23T18:04:08Z",
        
        "longitude": 77.2167,
        
        "latitude": 28.6667,
        
        "temperature": 86.09
        
    }
    
]



