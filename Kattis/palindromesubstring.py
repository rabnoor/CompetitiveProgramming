import sys as sys

for word in sys.stdin:
    num_alph={}
    alph_index = {}
    repeated = set()
    palindromes = set()
    reverse_word = ""
    for i in range(1, len(word) + 1):
        reverse_word += word[-i]
    for letter in word:
        if letter not in num_alph:
            num_alph[letter] = 1
        else:
            num_alph[letter] += 1
    for letter in num_alph:
        if num_alph[letter] > 1:
            repeated.add(letter)

    for v in range(len(word)):
        if word[v] in repeated:
            if word[v] not in alph_index:
                alph_index[word[v]] = [v]
            else:
                alph_index[word[v]].append(v)
    for letter in alph_index:
        for c in (alph_index[letter][:-1]):
            letter_index = alph_index[letter].index(c)
            for n in (alph_index[letter][letter_index + 1:]):
                # print(n,c)

                if word[c:n + 1] == reverse_word[len(word) - n - 1:len(word) - c] and len(word[c:n + 1]) > 1:
                    if word[c:n + 1] not in palindromes:
                        palindromes.add(word[c:n + 1])
    for pal in sorted(palindromes):
        print(pal)
    print()
