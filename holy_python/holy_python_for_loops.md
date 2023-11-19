## Holy Python exercises: For Loops
Exercise 8-a
```python
lst=["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]
for item in lst:
    print(item)
```

Exercise 8-b
```python
lst=["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]
for name in lst:
    print("Hello!, " + name)
```
**Question: Is the + necessary here? My solution would be:**
```python
lst=["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]
for name in lst:
    print("Hello!,", name)
```

Exercise 8-c
```python
str="Antarctica"
for letter in str:
    print(letter)
```

Exercise 8-d
```python
str="Civilization"
c=0
for i in str:
    c = c + 1
    print(c)
```

Exercise 8-e
```python
lst1=["Phil", "Oz", "Seuss", "Dre"]
lst2=[]
for name in lst1:
    lst2.append("Dr. "+name)
print(lst2)
```
**Had trouble finding the solution here. Mabye try it again later!**

Exercise 8-f
```python
lst1=[3, 7, 6, 8, 9, 11, 15, 25]
lst2=[]
for number in lst1:
    lst2.append(number**2)
print(lst2)
```

Exercise 8-g
```python
lst1=[111, 32, -9, -45, -17, 9, 85, -10]
lst2=[]
for number in lst1:
    if number > 0:
        lst2.append(number)
print(lst2)
```

Exercise 8-h
```python
dict={"z1":900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
lst=[]
for key in dict:
    if dict[key] > 1000:
        lst.append(dict[key] - 1000)
print(lst)
```
**Generally, I had trouble finding a solution here. Question: Why doesn't the following code work? ...**
```python
dict={"z1":900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
lst=[]
for value in dict[key]:
    if value > 1000:
        lst.append(value - 1000)
print(lst)
```

Exercise 8-i
```python
lst1=[3.14, 66, "Teddy Bear", True, [], {}]
lst2=[]
for item in lst1:
    lst2.append(type(item))
print(lst2)
```
