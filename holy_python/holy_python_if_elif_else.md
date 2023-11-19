## Holy Python: If, Elif, Else Exercises

### Exercise 7-a
```python
name = input("Please enter your name.")
if name == "Bond":
    print("Welcome on board 007.")
else:
    print("Good morning " + name)
```
**Had trouble finding a solution by myself here. ~~Don't get the concept of the input function - will have a look at it later!~~ Update: I get it know! :smile:**

### Exercise 7-b
```python
# Do the same thing as exercise 7-a this time making sure if the name is bond with lower case b it still prints "Welcome on board 007.":
name = input("Please enter your name.")
if name.lower() == "bond":
    print("Welcome on board 007")
else:
    print("Good morning " + name)
# Answer: if you construct your logical statement with name.lower() it will work either way!
```
** Had trouble finding a solution by myself here. Couldn't come up with the .lower() part. Maybe revisit and try again later!**

### Exercise 7-c
```python
def evens(i):
    if i % 2 == 0:
        return True
    else:
        return False
```

### Exercise 7-d
```python
def thedecimal(i):
    if i - int(i) != 0:
        return i-int(i)
    else:
        return "INTEGER"
```
** Had trouble finding a solution by myself here. Esp. coming up with the i-int(i) part. Maybe revisit and try again later!**

### Exercise 7-e
```python
treepersqkm = {"Finland": 90652, "Taiwan": 69593, "Japan": 49894, "Russia": 41396, "Brazil": 39542, "Canada": 36388, "Bulgaria": 24987, "France": 24436, "Greece": 24323, "United States": 23513, "Turkey": 11126, "India": 11109, "Denmark": 6129, "Syria": 534, "Saudi Arabia": 1}
def moretrees(dict):
    greencountries = []
    for key in dict:
        if dict[key] > 20000:
            greencountries.append(key)
        else:
            pass
    return greencountries
print(moretrees(treepersqkm))
```
** Had trouble finding a solutiuon by myself here. Maybe revist and try again later!**

### Exercise 7-f
```python
str = "Oranges and lemons, Say the bells of St. Clement's. You owe me three farthings, Say the bells of St. Martin's"
def count_l(a):
    c = 0
    for word in a.split():
        if "l" in word:
            c = c + 1
        else:
            pass
    return c
print(count_l(str))
```
** Had trouble finding a solution by mself here. Esp. the part with _if "l" in i_. Maybe revist and try again later!**

### Exercise 7-g
```python
str = "Oranges and lemons, Say the bells of St. Clement's. You owe me three farthings, Say the bells of St. Martin's"
def count_l(a):
    c = 0
    for word in a.split():
        if word[0].lower == a:
            c = c + 1
        else:
            pass
    return c
print(count_l(str))
```

