import requests as req

message = input('0 - Завершение\n' 
                '1 - Геоположение по IP\n'
                '2 - Текущая температура\n')

if message == '0':
    exit()
elif message == '1':
    ip = input('Введите ip: ')
    res = req.get(f'https://ipinfo.io/{ip}/geo')
    print(f'INFO: {res.json()}')
    print(f'STATUS: {res.status_code}')
elif message == '2':
    API_key = '167f1511dfe6f9f176f4d86cc1f32e34'
    lat, lon = input('Введите широту\n: '), input('Введите долготу\n: ')
    url = 'https://api.openweathermap.org/data/2.5/weather'
    res = req.get(f'{url}?lat={lat}&lon={lon}&appid={API_key}&units=metric&lang=ru')
    a = res.json()['main']
    print(f'\nINFO: {a}')
    print(f'\nSTATUS: {res.status_code}')