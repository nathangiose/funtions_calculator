def hotel_cost(nights):
    return nights * 140


def plane_ride_cost(city):
    if "cape_town" == city:
        return 2500

    elif "durban" == city:
        return 2300

    elif "JHB" == city:
        return 2000

    elif "BFN" == city:
        return 1800

    else:
        return "The location is not in our database"


def rental_car_cost(day):
    car_cost = 40 * day

    if days >= 7:
        car_cost = car_cost - 50
    elif 3 <= days < 7:
        car_cost = car_cost - 20
    return car_cost


def trip_cost(city, day, spending_money):
    return rental_car_cost(day) + hotel_cost(day) + plane_ride_cost(city) + spending_money


location = input("Where did you go: ")
days = int(input("How many days did you stay? "))
extras = float(input("How much did you spend on extras: "))
print(trip_cost("BFN", 2, 1000))
