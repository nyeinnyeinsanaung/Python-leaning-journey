string1 = "5"
print(string1)
print(type(string1))

# string to integer
int1 = int(string1)
print(int1)
print(type(int1))


# string to float
float1 = int(string1)
print(float1)
print(type(float1))


# float to integer
float2 = 1.9
int2 = int(float2)
print(int2)
print(type(int2))


# int to str
int4 = 4
string4 = str(int4)  # "4"
print(string4)
print(type(string4))

# float to str
float3 = 3.5
string5 = str(float3)
print(string5)
print(type(string5))


# boolean casting
# 0, '' empty string, None(null):  False
# otherwise True


int10 = 10
bool1 = bool(int10)
print(bool1)
print(type(bool1))

int11 = 0
bool1 = bool(int11)
print(bool1)
print(type(bool1))

str10 = "a"
bool1 = bool(str10)
print(bool1)
print(type(bool1))

str10 = ""
bool1 = bool(str10)
print(bool1)
print(type(bool1))


# error
# string3 ="name"
# int3 = int(string3)
# print(int3)


# type override
# string1 = float(string1)
# print(string1)
# print(type(string1))