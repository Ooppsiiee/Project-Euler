
#%%
sum = 0 
first = 1
second = 2

while first <= 4000000:
    if first % 2 == 0:
        sum = sum + first
    
    first, second = second, first + second

print(sum)

#%%
s = [1, 2, 3 , 4]
s.pop()
print(s)
print(s.insert)


#%%
