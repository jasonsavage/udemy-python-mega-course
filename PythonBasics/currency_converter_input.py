def currency_converter(rate, euros):
	dollars = euros*rate
	return dollars


r = float(raw_input("Enter rate: "))
e = float(raw_input("Enter euros: "))

result = currency_converter(r, e)

print(result)