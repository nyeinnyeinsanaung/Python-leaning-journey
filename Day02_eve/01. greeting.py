name = input("What is your name : ")
print("hello", name, "!")

# age # color of eye

age = input("How old are you? : ")
print("I am", age,)

eye_color = input("What's your eyes color? :")
print("My eyes is", eye_color)

# method 01
age = input("Input age again to know after 5 years : ")
print("age is", age, ',')
future_age_5 = int(age) + 5
print("My age will be", future_age_5, "after 5 years.")

# method 02
age = int(input("Input age again to know after 10 years : "))
future_age_10 = int(age) + 10
print("My age will be", future_age_10, "after 10 years.")

# method 03
print("My age will be", int(input("Enter your age : ")) + 5, "after 5 years")
