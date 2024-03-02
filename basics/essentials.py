# Arrays
name = ['Jose','João','Maria']
score = [9,8,7]

print(sum(score)/len(score))

# Tuples (Different of arrays, tuples cannot be modified)
name_2 = ('Jose','João','Maria')
score_2 = (9,8,7)

# Dictionary
students = {'students':['rafael','ana','maria'],'score':[9,10,7]}

# If
x = 1

if x == 1:
    print('Condition IF')
elif x == 0:
    print('Condition Else If')
else:
    print('Condition Else')

# For
ages = [10,15,20,30,25]

## Vector
for age in ages:
    print(age)

print('Fim vector print')

## Range

for age in range (0,10):
    print(age)

print('Fim range print')

# While
count = 0
while (count < 5):
    print(count)
    count = count + 1

## Inline commands
ages = [10,15,20,30,25]

double_ages = [2*(x) for x in ages]
print(double_ages)

double_ages = [2*(x+1) for x in ages]
print(double_ages)

double_ages = [2*(x+1) if x>15 else x for x in ages]
print(double_ages)

## Functions
def my_sum(x,y):
    msum = x+y
    return msum

def my_mult(x,y):
    mmult = x*y
    return mmult

## Class
class structure():
    pass