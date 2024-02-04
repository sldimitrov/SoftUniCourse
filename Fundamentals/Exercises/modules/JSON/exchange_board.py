import requests

def get_price_usd_eur(operation):
    url = 'https://www.freeforexapi.com/api/live?pairs=USDEUR'
    try:
        response = requests.get(url)
        date = response.json()
        rate = date['rates']['USDEUR']['rate']
        print()
        print(f'The current rate is {rate}(USD-EUR)')
        usd_exchange = float(input("Please input a valid value to transfer(50): "))
        eur = usd_exchange * rate
        print(f' - {usd_exchange:.2f} USD are {eur:.2f} EUR')
        print()

    except requests.exceptions.RequestException as e:
        print('Error', e)


def get_price_eur_usd(operation):
    url = 'https://www.freeforexapi.com/api/live?pairs=EURUSD'
    try:
        response = requests.get(url)
        date = response.json()
        rate = date['rates']['EURUSD']['rate']
        print()
        print(f'The current rate is {rate}(EUR-USD)')
        eur_exchange = float(input("Please input a valid value to transfer(50): "))
        usd = eur_exchange * rate
        print(f' - {eur_exchange:.2f} EUR are {usd:.2f} USD')
        print()

    except requests.exceptions.RequestException as e:
        print('Error', e)


def user_menu():
    print()
    print(6 * "* " + 'Welcome to our exchange board' + 6 * " *")
    while True:
        print()
        operation_type = input("Please input 1 if you want to exchange USD into EUR\n"
                               "           and 2 for the opposite ")
        print()
        if int(operation_type) == 1:
            current_rate = get_price_usd_eur(operation_type)
        elif int(operation_type) == 2:
            current_rate = get_price_eur_usd(operation_type)
        answer = input('Do you want to continue? - (y/n): ')
        if answer == 'y':
            print(current_rate)
        else:
            break



user_menu()
print()
print()
print('Operation has been finished,')
print('have a nice trading!')
# current_rate_USDEUR = get_price_usd_eur()
# print(current_rate_USDEUR)
