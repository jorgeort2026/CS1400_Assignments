# CS1400 Assignment 3: Driving Cost Calculator by Jorge Cid Ortega Letechipia


# Function calculates the trip cost for a gas vehicle
def calculate_gas_vehicle_trip_cost(trip_distance, miles_per_gallon, cost_per_gallon):
    gallons_needed = trip_distance / miles_per_gallon
    trip_cost = gallons_needed * cost_per_gallon
    return trip_cost


# Function calculates the trip cost using the trip distance, the vehicle's watt-hours per mile, and the electricity price per kilowatt-hour
def calculate_electric_vehicle_trip_cost(trip_distance, watt_hours_per_mile, cost_per_kilowatt_hour):
    kilowatt_hours = (watt_hours_per_mile / 1000) * trip_distance
    electric_cost = kilowatt_hours * cost_per_kilowatt_hour
    return electric_cost


# Main asks for input from the user, asks how much is the price of a gallon of gas and price per kilowatt-hour
# Then creates a loop which calculates the trip cost for a truck, gas car, and electric car
def main():
    price_of_gas = float(input("Please enter the price of gallon of gas: "))
    price_per_kilowatt_hour = float(input("Price of electricity per kilowatt hour: "))
    miles_per_gallon_gas_car = 24.4
    miles_per_gallon_truck = 14.2
    watt_hours_per_mile_electric_car = 229
    for trip_distance in range(50, 501, 50):
        truck_trip_cost = calculate_gas_vehicle_trip_cost(trip_distance, miles_per_gallon_truck, price_of_gas)
        gas_car_trip_cost = calculate_gas_vehicle_trip_cost(trip_distance, miles_per_gallon_gas_car, price_of_gas)
        electric_car_trip_cost = calculate_electric_vehicle_trip_cost(trip_distance, watt_hours_per_mile_electric_car, price_per_kilowatt_hour)
        print("For a trip of " + str(trip_distance) + " miles, the costs are: truck $" + str(round(truck_trip_cost)) + ", gas car $" + str(round(gas_car_trip_cost)) + ", electric car $" + str(round(electric_car_trip_cost)) + ".")


# Keep these lines. It helps Python run the program correctly by calling main when the program is run.
if __name__ == "__main__":
    main()