# Beginner Python Exercises (https://holypython.com/beginner-python-exercises/)

## Exercise 1-a
```phyton
print ("Hello World!")
```

## Exercise 1-b
```phyton
my_text = "Hello World"
print(my_text)
```

## Exercise 1-c
```phyton
print(1, 9, "Low", 7, 7)
```

## Exercise 2-a
```phyton
glass_of_water = 3
print("I drank", glass_of_water, "glasses of water today.")
```

## Exercise 2-b
```phyton
glass_of_water=glass_of_water + 1
print(glass_of_water)
```

## Exercise 3-a
```phyton
men_stepped_on_the_moon = 12
print(men_stepped_on_the_moon)
```

## Exercise 3-b
```phyton
my_reason_for_coding = "Zu viel Hitze im Tiefkühlfach"
print(my_reason_for_coding)
```

## Exercise 3-c
```phyton
global_mean_sea_level_2018 = 21
global_mean_sea_level_2018 = 21.36
print(global_mean_sea_level_2018)
```

## Exercise 3-d
**Note to self: Find out more about Booleans!**
```phyton
staying_alive = False
print(staying_alive)
```

## Exercise 4-a
```phyton
answer_1 = type(men_stepped_on_the_moon)
print(answer_1)
```

## Exercise 4-b
```phyton
answer_2 = type(my_reason_for_coding)
print(answer_2)
```

## Exercise 4-c
```phyton
answer_3 = type(global_mean_sea_level_delta_2018)
print(answer_3)
```

## Exercise 4-d
```phyton
answer_4 = type(staying_alive)
print(answer_4)
```

## Exercise 4-e
```phyton
my_grade = "10"
answer_5 = type(my_grade)
print(answer_5)
answer_5 = int(my_grade)
```

## Exercise 4-f
```phyton
my_temp=97.70
answer_6 = type(my_temp)
print(answer_6)
answer_6 = int(my_temp)
```

## Exercise 4-g
```phyton
shoe_price = "69.99"
answer_7 = type(shoe_price)
print(answer_7)
answer_7 = float(shoe_price)
```

## Exercise 4-h
```phyton
gross_world_product = 84.84
gwp_str = str(gross_world_product)
answer_8 = "In 2018 gross product of the world (GWP) was " + gwp_str + " in trillion US dollars."
print(answer_8)
```

## Exercise 6-a
```phyton
lst = [11, 100, 99, 1000, 999]
answer_1 = lst[0]
print(answer_1)
```

## Exercise 6-b
```phyton
lst = [11, 100, 101, 999, 1001]
print(lst[1])
```
 
## Exercise 6-c
```phyton
answer_1 = lst[-1]
print(answer_1)
```

## Exercise 6-d
```phyton
gift_list = ['socks', '4K drone', 'wine', 'jam']
gift_list.append("pajamas")
print(gift_list)
```

## Exercise 6-e
```phyton
gift_list = ['socks', '4K drone', 'wine', 'jam']
gift_list.append(["socks", "tshirt", "pajamas"])
print(gift_list)
```

## Exercise 6-f
**Question: Why 2? It says index 3 which should refer to the fourth element in the list, right?**
```phyton
gift_list = ['socks', '4K drone', 'wine', 'jam']
gift_list.insert(2, "slippers")
print(gift_list)
```

## Exercise 6-g
```phyton
lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
answer_1 = lst.index(8679)
print(answer_1)
```

## Exercise 6-h
```phyton
lst =["CRV", "Outback", "XC90", "GL", "Cherokee", "Escalade"]
lst.append(["Navigator","Suburban"])
print(lst)
```

## Exercise 6-i
```phyton
lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
lst.remove(99)
print(lst)
```

## Exercise 6-j
```phyton
ls t =[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
lst.reverse()
print(lst)
```

## Exercise 6-k
```phyton
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
answer_1 = lst.count(6)
print(answer_1)
```

## Exercise 6-l
```phyton
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
answer_1 = sum(lst)
print(answer_1)
```

## Exercise 6-m
```phyton
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
answer_1 = min(lst)
print(answer_1)
```

## Exercise 6-n
```phyton
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
answer_1 = max(lst)
print(answer_1)
```

## Exercise 9-a
```phyton
str = "It's always darkest before dawn."
print(str)
```

## Exercise 9-b
```phyton
str = "It's always darkest before dawn."
ans_1 = str[0] + str[1] + str[-1]
print(ans_1)
```

## Exercise 9-c
```phyton
str = "It's always darkest before dawn."
str = str.replace(".", "!")
print(str)
```

## Exercise 9-d
```phyton
str = "EVERY Strike Brings Me Closer to the Next Home run."
str = str.lower()
print(str)
```

## Exercise 9-e
```phyton
str = "don't stop me now."
str = str.upper()
print(str)
```

## Exercise 9-f
```phyton
str = "there are no traffic JamS Along The extra mile."
str = str.capitalize()
print(str)
```

## Exercise 9-g
```phyton
str = "There are no traffic jams along the extra mile."
ans_1 = str.startswith("A")
print(ans_1)
```

## Exercise 9-h
```phyton
str = "There are no traffic jams along the extra mile."
ans_1 = str.endswith(".")
print(ans_1)
```

## Exercise 9-i
```phyton
str="The best revenge is massive success."
ans_1=str.index("v")
print(ans_1)
```

## Exercise 9-j
**Question: So there is really no difference between the .index() and .find() function?**
```phyton
str="The best revenge is massive success."
ans_1=str.find("m")
print(ans_1)
```

## Exercise 9-k
**Question: When running Python in JupyterLab, str.find("X") doesn't return the value -1, as it should apparently. Why?**
```phyton
str = "The best revenge is massive success."
ans_1 = str.find("X")
print(ans_1)
ans_1 = str.index("X")
print(ans_1)
```

## Exercise 9-l
```phyton
str = "People often say that motivation doesn't last. Well, neither does bathing.  That's why we recommend it daily."
ans_1 = str.count("a")
ans_2 = str.count("o")
print("count of a is: ", ans_1, " count of o is: ", ans_2)
```

## Exercise 9-m
```phyton
v_1 = "1"
v_2 = 1
ans_1 = type(v_1)
ans_2 = type(v_2)
print(ans_1)
print(ans_2)
```

## Exercise 9-n
```phyton
str = "1.975.000"
ans_1 = len(str)
print(ans_1)
```

## Exercise 11-a
```phyton
lst = [11, 100, 99, 1000, 999]
lst.sort()
print(lst)
```

## Exercise 11-b
**Question: The solution says lst.sort(reverse = False) - but this is the default argument, so why write it down?**
```phyton
lst = ["Ukraine", "Japan", "Canada", "Kazakhstan", "Taiwan", "India", "Belize"]
lst.sort()
print(lst)
```

## Exercise 11-c
```phyton
lst = [11, 100, 101, 999, 1001]
lst.sort(reverse = True)
print(lst)
```

## Exercise 11-d
```phyton
gift_list = ['socks', '4K drone', 'wine', 'jam']
gift_list.sort(reverse = True)
print(gift_list)
```

## Exercise 11-e
```phyton
NFL = ["Panthers", "Bears", "Dolphins" "Patriots", "Saints", "Giants"]
NFL.sort(reverse = True)
answer_1 = NFL[-1]
print(answer_1)
```

## Exercise 11-f
```phyton
muni = ["Melbourne", "Shanghai", "Delhi", "Atlanta", "Moscow", "Montreal"]
muni.sort(reverse = True)
print(muni)
```

## Exercise 12-a
```phyton
lst = [11, 100, 99, 1000, 999]
popped_item = lst.pop()
print(popped_item)
print(lst)
```

## Exercise 12-b
**Question: Why does lst.pop(a) work with round brackets? We're working with indexing here, shouldn't we use square brackets: lst.pop[a]?**
```phyton
lst = ["milk", "banana", "eggs", "bread", "broccoli", "lemons"]
item = lst.pop(lst.index("broccoli"))
print(lst, item)
```

## Exercise 17-a
```phyton
wrd = "Toscana"
ans_1 = wrd[0:4]
print(ans_1)
```

## Exercise 17-b
```phyton
wrd = "Toscana"
ans_1 = wrd[3:]
print(ans_1)
```

## Exercise 17-c
```phyton
wrd = "Toscana"
ans_1 = wrd[3:6]
print(ans_1)
```

## Exercise 17-d
**Question/having trouble understanding this!**\
**Update/Answer: [x:y:z] means "from x to y-1 in steps of z"** 
```phyton
wrd = "Toscana"
ans_1 = wrd[0::2]
print(ans_1)
```

## Exercise 17-e
**Question/having trouble understanding this!**\
**Update/Answer: See exercise 17-d**
```phyton
wrd = "Toscana"
ans_1 = wrd[1:-1:2]
print(ans_1)
```

## Exercise 17-f
**Question/having trouble understanding this!**\
**Update/Answer: See exercise 17-d**\
**Note to self: This is actually not a good way to do it - it's not immediately clear what's happening here! What we should be doing: .reverse()! So for the future, resist the temptation and use the reverse-function so other people will understand as well!**
```phyton
lst = [0,1,2,3,4]
ans_1 = lst[::-1]
print(ans_1)
```

## Exercise 17-g
**Question/having trouble undertstanding this!**\
**Update/Answer: See exercise 17-d"**
```phyton
lst = [0,1,2,3,4]
ans_1 = lst[-2:]
print(ans_1)
```

## Exercise 17-h
```phyton
lst = [40,50,20,30,90]
ans_1 = lst[1:3] 
print(ans_1)
```

