
file = open("example.txt", 'r')

# read file content (moves pointer to end of file)
content = file.read()

# move pointer back to beginning of file
file.seek(0)

# read lines into a list
results = file.readlines()

# close file
file.close()

# print result
print("content", content)
print("results", results)

#clean up
results = [i.rstrip("\n") for i in results]

print("clean results", results)