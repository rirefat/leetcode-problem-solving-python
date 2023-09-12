# https://leetcode.com/problems/length-of-last-word/

s = "Hello World"
stripped = s.strip()
strList = stripped.split(" ")
lastWord = strList[-1]
print(len(lastWord))