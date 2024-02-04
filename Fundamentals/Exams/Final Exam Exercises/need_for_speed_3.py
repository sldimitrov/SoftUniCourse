def create_a_car(name: str, distance: int, fuel: int) -> dict:
    """
    This function take 3 params from the main.
    Initialise a dictionary with the car information given
    and returns it to the main
    """
    return {'name': name, 'distance': distance, 'fuel': fuel}


def drive_car(car, mileage: int, fuel_needed: int):
    """
    This function print out in the console which car is being driven and how much
    liters of fuel are being consumed. If there are not enough, it also prints.
    At the end we check if its time to sell the car (distance >= 100000)
    :return: list
    """
    if car['fuel'] >= fuel_needed:
        car['distance'] += mileage
        car['fuel'] -= fuel_needed
        print(f"{car['name']} driven for {mileage} kilometers. {fuel_needed} liters of fuel consumed.")
        if car['distance'] >= 100000:
            print(f"Time to sell the {car['name']}!")
            return True
    else:
        print('Not enough fuel to make that ride')
        return False


def refuel_tank(model, fuel_to_add: int):
    """
    This function calculate the addition fuel and add it to the tank of
    the vehicle. It prints the model and the added liters in the console
    :return: dict
    """
    maximum = 75
    fuel_to_add = min(fuel_to_add, maximum - model['fuel'])
    model['fuel'] += fuel_to_add  # Check for the value > 75
    print(f"{model['name']} refueled with {fuel_to_add} liters")
    return True


def revert_func(car, kilometres_to_revert: int):
    """
    This function represent something which is a COMMON THING in Bulgaria.
    It reverts the mileage of the vehicle but not below 10000. It prints
    the value after doing it
    :return: list
    """
    car['distance'] -= kilometres_to_revert
    if car['distance'] < 10000:
        car['distance'] = 10000
    else:
        print(f"{car['name']} mileage decreased by {kilometres_to_revert} kilometers")


def main_function():
    """"
    This is the main function. Here we will implement
    the essentials of the logic in this exercises.
    We will also call the other additional functions
    when we need them. Okay, lets go!
    """
    cars = []
    num = int(input())
    for _ in range(num):
        car_info = input().split('|')
        car_model, mileage, fuel_available = car_info[0], int(car_info[1]), int(car_info[2])
        current_car = create_a_car(car_model, mileage, fuel_available)
        cars.append(current_car)

    is_stopped = False
    while True:
        command = input()

        if command == 'Stop':
            break

        tokens = command.split(' : ')
        action = tokens[0]
        car_name = tokens[1]
        for car in cars:
            if car['name'] == car_name:
                if action == 'Drive':
                    distance, fuel = int(tokens[2]), int(tokens[3])
                    if drive_car(car, distance, fuel):
                        cars.remove(car)

                elif action == 'Refuel':
                    added_fuel = int(tokens[2])
                    refuel_tank(car, added_fuel)

                elif action == 'Revert':
                    kilos = tokens[2]
                    revert_func(car, int(kilos))

    for car in cars:
        name, mileage, tank = car['name'], car['distance'], car['fuel']
        print(f"{name} -> Mileage: {mileage} kms, Fuel in the tank: {tank} lt.")


main_function()
