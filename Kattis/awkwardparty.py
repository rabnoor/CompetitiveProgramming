guests=input()
guest_order=[x for x in input().split(" ")]
guest_lang_pos={}
for i in range(0,len(guest_order)):
    if guest_order[i] in guest_lang_pos:
        guest_lang_pos[guest_order[i]].append(i)
    else:
        guest_lang_pos[guest_order[i]]=[i]
ind_awkwardness=[]
for lang in guest_lang_pos:
    if len(guest_lang_pos[lang])>1:
        for k in range(0,len(guest_lang_pos[lang])-1):
            ind_awkwardness.append(guest_lang_pos[lang][k+1]-guest_lang_pos[lang][k])
    else:
        continue
if len(ind_awkwardness)==0:
    print(guests)
else:
    print(min(ind_awkwardness))
