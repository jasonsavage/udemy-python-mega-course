names = ['james', 'john', 'jack']
email_domains = ['gamil', 'hotmail', 'yahoo']

# use zip to iterate more than one list at a time
for i, j in zip(names, email_domains):
	print(i, j)


'''
zip(...)
    zip(seq1 [, seq2 [...]]) -> [(seq1[0], seq2[0] ...), (...)]

    Return a list of tuples, where each tuple contains the i-th element
    from each of the argument sequences.  The returned list is truncated
    in length to the length of the shortest argument sequence.
'''
