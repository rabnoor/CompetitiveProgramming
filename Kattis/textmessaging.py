tests = int(input())
for t in range(tests):
    count = 1
    total = 0
    phone_system = [int(x) for x in input().split(" ")]
    maxi = phone_system[0]
    keys = phone_system[1]
    alph = phone_system[2]
    freq = [int(x) for x in input().split(" ")]
    freq.sort(reverse=True)
    while len(freq) > keys:
        for i in range(0, keys):
            total += count * freq[i]
            if i==(keys-1):
                count += 1
                del freq[0:keys]
    while len(freq) != 0:
        for cu in range(len(freq)):
            total += count * freq[0]
            del freq[0]
    print("Case #"+str(t+1)+": "+str(total))