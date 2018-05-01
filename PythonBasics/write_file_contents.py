
file = open("output.txt", 'w')  # use 'a' to append

# write content to a file
file.write("Line 1\n")
file.write("Line 2")

# close file
file.close()


# better way
with open("output.txt", 'w') as f:
	f.write("Line 3\n")
	f.write("Line 4")
