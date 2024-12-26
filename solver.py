with open("wordlist.txt", 'r') as f:
    wordlist = f.readline()[:-1].split(" ")
p_l, c_l, w_l = set({}), set({}), set({})
c = "salet"
print("'.' for wrong, 'c' for misplaced, 'x' for correct")
while True:
    print(f"Guess: \n  {c}")
    g = input("> ") # no input checking, if you mess it up it's your fault
    for i in range(0, 5, +1):
        if g[i] == 'c':
            c_l.add((c[i], i))
        elif g[i] == 'x':
            p_l.add((c[i], i))
        elif g[i] == '.':
            w_l.add((c[i], i))
    for e in p_l:
        wordlist[:] = [word for word in wordlist if e[0] == word[e[1]]]
    for e in c_l:
        wordlist[:] = [word for word in wordlist if e[0] in word and e[0] != word[e[1]]]
    for e in w_l:
        wordlist[:] = [word for word in wordlist if not (e[0] == word[e[1]] or e[0] in word and e[0] not in [l[0] for l in p_l] + [l[0] for l in c_l])]
    c = wordlist[0]
