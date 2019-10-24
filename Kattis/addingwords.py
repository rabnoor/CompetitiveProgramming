import sys as sys
word_val = {}
val_word = {}
for i in sys.stdin:
    i = str(i).strip()
    if i == "clear":
        word_val = {}
        val_word = {}
    else:
        stdcond = True
        sum = 0
        def_quest = [x for x in i.split(" ")]
        if def_quest[0] == "def":
            if def_quest[1] in word_val:
                del val_word[word_val[def_quest[1]]]
            word_val[def_quest[1]] = int(def_quest[2])

            val_word[int(def_quest[2])] = def_quest[1]

        elif def_quest[0] == "calc":
            valu = def_quest[1]
            if valu not in word_val:
                stdcond = False
            else:
                sum += word_val[def_quest[1]]
            for i in range(3, len(def_quest), 2):
                if def_quest[i] in word_val:
                    if def_quest[i - 1] == "+":
                        sum += word_val[def_quest[i]]
                    else:
                        sum -= word_val[def_quest[i]]
                else:
                    stdcond = False
            if sum not in val_word:
                stdcond = False
            if stdcond == False:
                for i in range(1, len(def_quest)):
                    print(def_quest[i], end=" ")
                print("unknown")

            else:
                for i in range(1, len(def_quest)):
                    print(def_quest[i], end=" ")
                print(val_word[sum])
