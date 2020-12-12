
with open('Test.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()]
def final_layout(inputs):
    inputs_layout = ""
    for i in range(len(inputs)):
        inputs_layout += inputs[i]
    return inputs_layout
def double_check(inputs, checks, zahl):
    belegt = 0
    for i in range(len(checks)):
        if inputs[zahl+checks[i]] == "#":
            belegt += 1
    return belegt

def check(inputs):
    copy =(inputs + '.')[:-1]
    for i in range(len(inputs)):
        if inputs[i] == "L" or inputs[i] == "#":
            belegt = 0
            if i % 10 == 0 and i-9 < 0:
                belegt += double_check(inputs, [1,10,11], i)
            elif (i-9) % 10 == 0 and i-10 < 0:
                belegt += double_check(inputs, [-1,9,10,], i)
            elif i % 10 == 0 and i >len(inputs)-11:
                belegt += double_check(inputs, [-10,-9,1], i)
            elif (i-9) % 10 == 0 and i >len(inputs)-10:
                belegt += double_check(inputs, [-11,-10,-1], i)
            elif i % 10 == 0:
                belegt += double_check(inputs, [-10,-9,1,10,11], i)
            elif (i-9) % 10 == 0:
                belegt += double_check(inputs, [-11,-10,-1,9,10], i)
            elif i-9 < 0:
               belegt += double_check(inputs, [1,9,10,11], i)
            elif i >len(inputs)-10:
                belegt += double_check(inputs, [-11,-10,-9,-1,1], i)
            else:
                belegt += double_check(inputs, [-11,-10,-9,-1,1,9,10,11], i)
            
            if belegt < 4 and inputs[i] == "#":
                copy = copy[:i] + "#" + copy[i + 1:]
            elif belegt == 0 and inputs[i] == "L":
                copy = copy[:i] + "#" + copy[i + 1:]
            else:
                 copy = copy[:i] + "L" + copy[i + 1:]
    return copy
            
                        
    
def ausgabe(inputs):
    x = 0
    y = 10
    for i in range(len(inputs)//10):
        print(inputs[x:y])
        x+=10
        y+=10
    
    
inputs = final_layout(inputs)
ausgabe(inputs)
for i in range(5):
    inputs = check(inputs)
    ausgabe(inputs)
    print("--------------")
print(inputs.count("#"))
 
