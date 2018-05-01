# greeting = input("Write a greeting: ")
# print(greeting)


def age_foo(age):
	new_age = age + 50
	return new_age


age = int(input("Enter your age: "))

if(age < 150):
	print(age_foo(age))
else:
	print("How is that possible?")
