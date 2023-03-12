# read one line from input
#line = input().strip()
line = "jirka"

print(line)
print(line[1])
print(len(line))

chars=list(line) # prevedu na pole
print(chars)
chars[2]="R" # zmenim treti prvek pole na jine
print(chars)
newline="".join(chars)  # spojim pole do retezce
print(newline)

# jestli je v retezci za znakem r, tak udělej z něj X
for i in range(len(chars)-1):
    actual_char = chars[i]
    next_char = chars[i+1]
    print(actual_char, next_char)
    if next_char == "r" or next_char == "R":
        chars[i] = 'X'

print(chars)

