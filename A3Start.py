def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit


def make_address(city, country):
    address = city + ", " + country
    return address


print("Testing make_address function:")
print("... with ATL USA. Expected: 'ATL, USA', got:", make_address("ATL", "USA"))


print("Testing convert_to_fahrenheit function:")
print("... with 0. Expected: 32, got:", convert_to_fahrenheit(0))


print("Testing make_address function:")
print("... with BAR SPN. Expected: 'BAR, SPN', got:", make_address("BAR", "SPN"))


print("Testing convert_to_fahrenheit function:")
print("... with -10. Expected: 14, got:", convert_to_fahrenheit(-10))