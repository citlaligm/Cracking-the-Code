def URLify(str_in,n):
	ulr_part = str_in.split()
	return "%20".join(ulr_part)

str_in = "Mr John Smith"

print(URLify(str_in,13))


