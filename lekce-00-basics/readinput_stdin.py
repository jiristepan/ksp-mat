nq = input().strip().split(" ")

if len(nq) != 2:
    print("Error - i need two numbers")
    quit()

N = int(nq[0])
Q = int(nq[1])

words=[]
for i in range(N):
    w=input()
    words.append(w)

questions=[]
for i in range(Q):
    q=input()
    questions.append(q)

print("-----------------------------------")
print(f"Words: {words}")
print(f"questions: {questions}")

