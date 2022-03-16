def ageChange(age1, age2):
    print(age1, age2)
    if (age1 > age2):
        num = age1
        age1 = age2
        age2 = num
    return age1,age2
print( ageChange(3, 7) )
print ( ageChange(7, 3) ) 
