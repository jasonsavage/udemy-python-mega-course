
# Please create a function that converts Celsius degrees to Fahrenheit.
# The formula to convert Celsius to Fahrenheit is F = C x 9/5 + 32.


# result
def convert_c_to_f (celsius):
	return celsius * 9/5 + 32.0


# test
print('given 0 C expect 32 F : %d' % convert_c_to_f(0))
print('given 45 C expect 113 F : %d' % convert_c_to_f(45))
