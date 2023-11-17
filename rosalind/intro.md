### Solution to problem INI1
When typing
```python
import this
```
into the Phyton command line, a poem called "The Zen of Phyton" by Tim Peters gets printed (I solved this problem by typing "import this" into the command line and pasting the output into the answer file provided by Rosalind). 

### Solution to problem INI2
Since my dataset provided was a = 834 and b = 893, I solved this problem by typing
```python
834**2 + 893**2
```
into the Phyton command line, which gave me 1493005 as output (i. e. c squared = 1493005).

### Solution to problem INI3
~~Unfortunately, I wasn't able to solve this problem. When trying to define the string by typing s="ZC9hYu1oAfvdSS09ebCHVoVCyFH9f5BJVzn7CRipariaHQXv0e2cMU70hoTkG32hHh80jYDTQp9PMz6KwNjly6vauQpde7RXNijcR6KqPwFpsc11eoNFbmwfjmQMPgvBwTdzFxYGiJVDXzonata6JBFsN08VRUyLOxhzdzoqasRAzWpFLx0CvLUqLlmtTw.
37 43 141 146" into the Phyton command line, the error message "SyntaxError: unterminated string literal (detected at line 1)" showed up. Also, I'm actually not sure how to solve this problem even if I was able to define s.~~\
**Update:** I must have misunderstood something, but now I get it! I solved this problem by downloading my dataset (_Dg25Ay3qIkEy6UQhGxqQy5EPtl5OKdJJhzTplEU5c2q2B4ParabuthusAturtornvu0VzgGUPkPrzTo1l9xMxnz0DywfCZrzUs9DsMTq39EJ0WUZlFQccSXqTyjkjlrJ2spu41mSXcK9sd4yFOcFc4M2mB6JD4eWfyiKVyZmkN4RLq2qBXesIRgTZky9Z9JTeI.
46 55 57 62_). Then, I defined the string s and the four integers a, b, c and d:
```phyton
s = "Dg25Ay3qIkEy6UQhGxqQy5EPtl5OKdJJhzTplEU5c2q2B4ParabuthusAturtornvu0VzgGUPkPrzTo1l9xMxnz0DywfCZrzUs9DsMTq39EJ0WUZlFQccSXqTyjkjlrJ2spu41mSXcK9sd4yFOcFc4M2mB6JD4eWfyiKVyZmkN4RLq2qBXesIRgTZky9Z9JTeI."
a = 46
b = 55 
c = 57
d = 62
```
I then defined two slices of the string s:
```phyton
slice_1 = s[a:b+1]
slice_2 = s[c:d+1]
```

... and printed them:
```phyton
print(slice_1 + " " + slice_2) 
```
I got **Parabuthus turtor**!
