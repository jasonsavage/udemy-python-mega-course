r"""
Consider the following list:

temperatures=[10,-20,-289,100]

Then, iterate over the temperature converter function that you created in execise 3 and print out the following output.
"""

# code
temperatures = [10, -20, -289, 100]
def convert_c_to_f (celsius):
	if(celsius < -273.15):
		return "That temperature doesn't make sense!"

	return celsius * 9/5 + 32.0


# result
for i in temperatures:
	print(convert_c_to_f(i))