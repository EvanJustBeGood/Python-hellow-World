url = "https://github.com/EvanJustBeGood/Python-hellow-World"
response = requests.get(url)


if response.status_code == 200:
    data = response.json()  
    print(data)
else:
    print("Ошибка запроса:", response.status_code)
