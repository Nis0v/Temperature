import requests

def write_city():
    c = input("Please write: City or exit: ").lower().title()
    if c != "Exit":
        request(c)
    else:
        print("Your welcome")
def request(city):
    try:
        api_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': '11c0d3dc6093f7442898ee49d2430d20',
            'units': 'metric'
        }
        res = requests.get(api_url, params=params)
        print(f"Temperatur in {city}: {res.json()['main']['temp']}")
        again()
    except KeyError:
        print("This is city not in database, please write again")
        write_city()
def again():
    n = input("Again?[Y/N]: ")
    if n == "Y":
        write_city()
    else:
        print("Your welcome")
write_city()
