first_move=input()
last_alph=first_move[-1]
num_options= int(input())
options=[]
move_valid=[""]
valid_alph={}
output=""
absolute_winner=""
for g in range(num_options):
    options.append(input())
for i in range(len(options)):
    if options[i][0]==last_alph:
        move_valid.append(options[i])
    if options[i][0] not in valid_alph:
        valid_alph[options[i][0]]=[options[i]]
    else:
        valid_alph[options[i][0]].append(options[i])
if len(move_valid)>1:
    for animal in move_valid[1:]:
        sum=0
        move_lastalph=animal[-1]
        if move_lastalph in valid_alph and (len(valid_alph[move_lastalph])>1 or animal not in valid_alph[move_lastalph]) :
            sum+=0
        else:
            sum+=1

        if sum!=0:
            absolute_winner=animal
            break
if len(move_valid)>1:
    if absolute_winner!="":
        output=absolute_winner+"!"
    else:
        output=move_valid[1]
else:
    output="?"
print(output)
