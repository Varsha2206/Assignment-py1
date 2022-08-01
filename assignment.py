# 1
inp = ['work', 'office', 'work from home']
for i in range(0, len(inp)):
    for j in range(i+1, len(inp)):
        if inp[i] in inp[j]:
            inp.remove(inp[i])

print(inp)


# 2
string = input("Enter a String")
result = []
for i in range(len(string)):
    test = string[i]
    for j in range(i+1, len(string)):
        if test == string[j]:
            test2 = string[i:j+1]
            if test2 == test2[::-1]:
                if i == 0 or j == len(string)-1:
                    result.append(string[i:j+1]+' : '+str(1))
                elif i == 0 and j == len(string)-1:
                    result.append(string[i:j+1]+' : '+str(0))
                else:
                    result.append(string[i:j+1]+' : '+str(2))
print(result)


# 3
n = int(input("Enter the array height: "))
height = list(map(int, input().split()))
res = 0
for i in range(n):
    for j in range(i+1, n):
        amount_of_water = (j-i) * min(height[i], height[j])
        res = max(res, amount_of_water)
print(res)


# 4
list2 = [10, 140, 155, 550]
for i in list2:
    if i % 5 == 0:
        if i > 150:
            continue
        elif i > 500:
            break
        else:
            print(i)


# 5
list_1 = [-2, 3, 2, -4]
maxp = list_1[0]
for i in range(0, len(list_1)):
    a = list_1[i]
    for j in range(i+1, len(list_1)):
        a = a*list_1[j]
        maxp = max(a, maxp)
print(maxp)

# 6
n = 2
sum = 0
for i in range(1, n+1):
    sum = sum+(1/i)
print(sum)


# 7
binary_form = "101111"
dec = 0
list_1 = list(reversed(binary_form))
for i in range(0, len(list_1)):
    dec = dec+(int(list_1[i])*(2**i))
print(dec)


num=int(input('enter a number'))
print(f'{num:b} is binary {num:0X} is hexadecimal')


# 8
def getfibsequence(x):
    a = 0
    b = 1
    yield(a)
    yield(b)
    for i in range(x):
        c = a+b
        yield(c)
        a = b
        b = c


fib = getfibsequence(5)
next(fib)


# 9
S = "silent is the anagram of listen"
list_1 = S.split(' ')
for i in range(0, len(list_1)):
    for j in range(i+1, len(list_1)):
        if(sorted(list_1[i]) == sorted(list_1[j])):
            print(list_1[i])
            print(list_1[j])


# 10
a = 45328
b = str(a)
c = list(b)
min = int(("".join(sorted(c))))
max = int(("".join(sorted(c, reverse=True))))
print(max-min)


# 11
s = input("Enter the parenthesis")
stack = []
for i in s:
    if(i == '(' or i == '[' or i == '{'):
        stack.append(i)

    elif(len(stack) > 0 and
         ((i == ')' and stack[len(stack)-1] == '(') or
         (i == '}' and stack[len(stack)-1] == '{') or
         (i == ']' and stack[len(stack)-1] == '['))):

        stack.pop()
    else:
        stack.append(i)

if len(stack) == 0:
    print(True)
else:
    print(False)

# 12
list1 = [1, 5, 6, 8, 7, 3]
list2 = [8, 6, 7, 9, 2]
list3 = []
intersection = []
unique = []

for i in list1:
    if i in list2:
        intersection.append(i)
print(intersection)


for i in list1+list2:
    if i not in intersection:
        unique.append(i)
print(unique)

# 13
# l=[3,8,5,9,98,101]
l = [1, 2, 3]
for i in range(len(l)):
    l[i] = str(l[i])
for i in range(len(l)):
    for j in range(1+i, len(l)):
        if l[j]+l[i] > l[i]+l[j]:
            l[i], l[j] = l[j], l[i]

print(''.join(l))


# 14
S = "Varsha"
dict = {}
for i in S:
    count = 0
    for j in S:
        if i == j:
            count = count+1
    dict[i] = count
for i in S:
    if(dict[i] == 1):
        print(i)
        break


# 15
n = int(input("enter the number of rows"))
for i in range(1, n+1):
    # print(str(l[i])*(l[i]))
    print('{} '.format(i)*i)
