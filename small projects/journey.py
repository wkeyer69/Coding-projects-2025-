t = int(input())
numbers = input()
str_num = numbers.split()
int_num = []
for num in str_num: 
    int_num.append(num)


n = int(int_num[0])
a = int(int_num[1])
b = int(int_num[2])
c = int(int_num[3])


number = 0 
total_number = 0 
count = 0 


while n >= total_number: 
    count += 1 
   
    total = a + total_number 
    total_number += total 
    if total_number != n:
        count += 1
        total = b + total_number
        total_number += total 
    if total_number != n:
        count += 1
        total = c + total_number
        total_number += total 
    print(count, total_number)
    



    
