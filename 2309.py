dwarf_tall = []
temp_tall = 0

for i in range(1,10):
  temp_tall = input()
  dwarf_tall.append(int(temp_tall))

dwarf_tall.sort()

for i in range(0,len(dwarf_tall)):
    for j in range(1+i,len(dwarf_tall)):
        dwarf_sum = 0
        for k in range(0,len(dwarf_tall)):
            if k != i and k != j:
                dwarf_sum = dwarf_sum+dwarf_tall[k] 
                if dwarf_sum == 100:
                    first_except = i
                    second_except = j
                    break

for i in range(0,len(dwarf_tall)):
    if (i != first_except) and (i != second_except):
        print(dwarf_tall[i])
       