# this is homework for Temperature converters

#  from °C to °F
print("\n")
print("----- This is a converter from °C to °F -----")
temp_c = float(input("Please input °C : "))
print(temp_c, "°C into °F is", (temp_c * 9 / 5) + 32)


#  from °F to °C
print("\n")
print("----- This is a converter from °F to °C -----")
temp_f = float(input("Please input °F : "))
print(temp_f, "°F into °C is", (temp_f - 32) * 5 / 9)