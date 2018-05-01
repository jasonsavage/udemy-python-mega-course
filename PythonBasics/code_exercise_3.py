r"""
In exercise 1 you created a function that converted Celsius degrees to Fahrenheit.

The lowest possible temperature that physical matter can reach is -273.15 C. With that in mind, please improve the
function by making it print out a message in case a number lower than -273.15 is
passed as input when calling the function.
"""

# result
def convert_c_to_f (celsius):
	if(celsius < -273.15):
		print("Warn: celsius value below the lowest possible temperature of physical matter (-273.15 C)")

	return celsius * 9/5 + 32.0


# test
convert_c_to_f(-300)