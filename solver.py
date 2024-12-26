def main():
    wordlist_file = open("wordlist.txt")
    wordlist = wordlist_file.readline()[:-1].split(" ")
    wordlist_file.close()
    p_l, c_l, w_l = set({}), set({}), set({})
    c = "adieu"
    print("'.' for wrong, 'c' for misplaced, 'x' for correct, hit return to skip word")
    while True:
        print(f"Guess: \n  {c}")
        g = input("> ") # no input checking, if you mess it up it's your fault
        if g == "":
            wordlist.remove(c)
            c = wordlist[0]
            continue
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
        if len(wordlist) == 1:
            print(c)
            break

if __name__ == "__main__":
    main()
