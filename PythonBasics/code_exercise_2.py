
# Try to print out number 10 only from the following dictionary.
money = {"saving_account": 200, "checking_account": 100, "under_bed": [500, 10, 100]}

# result
result = money['under_bed'][1]

# test
print('expect 10 : %d' % result)