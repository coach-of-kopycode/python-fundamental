print('\nPerintah del')
my_hobby = ['Swimming', 'Travelling', 'Learning']
del my_hobby[1]
for i in range(0, len(my_hobby)):
    print(my_hobby[i])

print('\nPerintah del dengan list comprehension')
my_hobby = ['Swimming', 'Travelling', 'Learning', 'Football']
del my_hobby[:]
for i in range(0, len(my_hobby)):
    print(my_hobby[i])

print('\nPerintah del dengan list comprehension start:end')
my_hobby = ['Swimming', 'Travelling', 'Learning', 'Football']
del my_hobby[0:-1] #start:end
for i in range(0, len(my_hobby)):
    print(my_hobby[i])

print('\nPerintah del dengan list comprehension: hapus genap')
my_hobby = ['1. Swimming', '2. Travelling', '3. Learning', '4. Eating']
del my_hobby[1::2] #start:stop:step
for i in range(0, len(my_hobby)):
    print(my_hobby[i])

print('\nlist comprehension')
my_hobby = ['1. Swimming', '2. Travelling', '3. Learning', '4. Eating']
my_hobby_new = my_hobby[:]
del my_hobby[:]
for i in range(0, len(my_hobby_new)):
    print(my_hobby_new[i])


print('\nlist comprehension buang data 2 terkahir')
my_hobby = ['1. Swimming', '2. Travelling', '3. Learning', '4. Eating']
new_hobby = my_hobby[0:-2]
for i in range(0, len(new_hobby)):
    print(new_hobby[i])

print('\nPerintah del dengan list comprehension: hapus genap')
my_hobby = ['1. Swimming', '2. Travelling', '3. Learning', '4. Eating']
print(my_hobby[0::2]) #start:stop:step