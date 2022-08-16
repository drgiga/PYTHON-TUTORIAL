data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
at_pos = data.find('@')
print(at_pos)

space_pos = data.find(' ',at_pos) # find first space after @ sign
print(space_pos)

domain = data[at_pos+1:space_pos]
print("domain is : "+domain)

