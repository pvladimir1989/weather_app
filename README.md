# weather_app
Для запуска приложения:
1.git clone https://github.com/pvladimir1989/weather_app.git

2.В папке weather_app создаем файл .env и вставляем туда ключи

SECRET_KEY="django-insecure-9h+f=h7e8nwnu^*b*rp=oxb1rofl=b&u=-k^@+d(s@p1e4=%fx"

BACKEND_DB_ENGINE=postgresql_psycopg2

BACKEND_DB_NAME=postgres

BACKEND_DB_USER=postgres

BACKEND_DB_PASSWORD=123456

BACKEND_DB_HOST=db

BACKEND_DB_PORT=5432

PG_PORT=5432

POSTGRES_PASSWORD=123456

WEATHER_KEY=12e5ff8f3f89d015e050dbdab7b7655f


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



