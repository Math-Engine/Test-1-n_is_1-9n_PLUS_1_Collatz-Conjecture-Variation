import sys
import os
import math
import json

sys.set_int_max_str_digits(2147483647)

def dividing_2(n):
  if (len(str(n)) < 16):
    return n//2
  n = str(n)
  r = 0
  for i in range(len(n) - 1):
    r = r + int(str(int(n[i] + "0")//2) + ("0" * (len(n) - 2 - i)))
  r = r + int(n[-1])//2
  return r

number_of_executions = int(sys.argv[1])
# section_range = int(sys.argv[2])
with open('n.txt', 'r') as file:
    num = int(file.read().strip())
with open('n_sequence.txt', 'r') as file:
    n_sequence = int(file.read().strip())
with open('maximum.json', 'r') as file:
    maximum = json.load(file)
with open('HailstoneArray.json', 'r') as file:
    HailstoneArray = json.load(file)

os.system(f'echo "Number: {num} <br> 계산할 항의 개수: {number_of_executions} ( {n_sequence + 1} ~ {n_sequence + number_of_executions} ) <br> <hr>" >> $GITHUB_STEP_SUMMARY')

Hailstone_Num = [num]
temp = num
is_loop = False
is_end = False
for i in range(n_sequence + 1, n_sequence + number_of_executions + 1):
  print(temp)
  if (int(str(temp)[-1])%2 == 1):
    temp = (temp * 9) + 1
  else:
    temp = dividing_2(temp)
  if temp in Hailstone_Num:
    is_loop = True
    Hailstone_Num.append(temp)
    print()
    print(Hailstone_Num)
    os.system(f'echo ":bangbang:" >> $GITHUB_STEP_SUMMARY')
    is_end = True
    break
  elif (temp == 1):
    Hailstone_Num.append(temp)
    print()
    print(Hailstone_Num)
    os.system(f'echo ":ballot_box_with_check:" >> $GITHUB_STEP_SUMMARY')
    is_end = True
    break
  else:
    Hailstone_Num.append(temp)
print()

Hailstone_Num.pop(0)
new_Hailstone_Num_array = Hailstone_Num

if (is_end == False):
  os.system(f'echo "question:" >> $GITHUB_STEP_SUMMARY')

with open('n.txt', 'w') as file:
    file.write(str(temp))

with open('n_sequence.txt', 'w') as file:
    file.write(str(n_sequence + number_of_executions + 1))

HailstoneArray.extend(new_Hailstone_Num_array)

with open('HailstoneArray.json', 'w') as file:
    json.dump(HailstoneArray, file)

if (max(Hailstone_Num) > int(maximum["maximum"])):
  maximum["n_sequence"] = n_sequence + new_Hailstone_Num_array.index(max(Hailstone_Num)) + 1
  maximum["maximum"] = max(Hailstone_Num)
  with open('maximum.txt', 'w') as file:
    file.write(str(maximum))
