list1 = []
list2 = []
list3 = []

count = {}

T = int(input('Enter the length:'))
for i in range(0, T):
    list1.append(int(input()))
    
# print(list1)
m = list1[0]
for i in range(0, len(list1)):
    if list1[i] == m:
        list2.append(list1[i])
    elif list1[i] > m:
        list2.append(list1[i])
        m = list1[i]
        
    else:
        list3.append(list2)
        list2 = []
        list2.append(list1[i])
        m = list1[i]
        
list3.append(list2)

# print(list3)
    
for i in range(0, len(list3)):
    count[i] = len(list3[i])

q = list(count.items())

q1 = max(q, key=lambda x:x[1])

print("The longest sequence(s) is/are:")
for i in range(0, len(q)):
    if q[i][1] == q1[1]:
        print(list3[q[i][0]])
                    
