#caculate bmi
# formula: 703x weight (lbs) / [height(in)]2

eve_w = float(input("weight is : "))
eve_h = float(input("height in feet : "))
print("My bmi is : ", 703 * eve_w / (eve_h ** 2), ".")
