numbers = [1,2,3,4,5,6,7,8,9,0]
# letters = 'abcdefghijklmnopqrstuvwxyz'
# letters = list[tuple(letters)]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
names = ['David','Alex','Hadi','Roberto','Alexis','James','Niloofar','Davoud','Armin','Farbod']
#=============================================
ziped_output = list(zip(numbers,letters,names))
print(ziped_output)
print('---------------------------------------')
n1,n2,n3 = zip(*ziped_output)
print(n1)
print(n2)
print(n3)
#=============================================


