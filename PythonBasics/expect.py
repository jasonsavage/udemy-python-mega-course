

# expect(object).toEqual(value, [message])
def expect(value):
	return {'toEqual': lambda x: x == value}
