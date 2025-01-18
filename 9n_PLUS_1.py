import sys
import os
import math
import json

sys.set_int_max_str_digits(2147483647)

number_of_executions = int(sys.argv[1])
section_range = int(sys.argv[2])
num = int(open('n.txt', 'r'))
n_sequence = int(open('n_sequence.txt', 'r'))
maximum = int(open('maximum.json', 'r'))
max_and_min = int(open('max_and_min.json', 'r'))

os.system(f'echo "Number: {num} <br> 계산할 항의 개수: {number_of_executions} ( {n_sequence + 1} ~ {n_sequence + number_of_executions} ) <br> 구간 범위: {section_range} <br> <hr>" >> $GITHUB_STEP_SUMMARY')

Hailstone_Num = [num]
temp = num
is_loop = False
is_end = False
for i in range(n_sequence + 1, n_sequence + number_of_executions + 1):
  print(temp, end="\n")
  if (temp%2 == 1):
    temp = (temp * 9) + 1
  else:
    temp = temp/2
    if "e" in str(temp):
      temp = int(str(temp)[0] + str(temp)[(str(temp).find(".") + 1):str(temp).find("e")] + ("0" * (int(str(temp)[((str(temp).find("+")) + 1):(len(str(temp)) + 1)]) - len(str(temp)[(str(temp).find(".") + 1):str(temp).find("e")]))))
    elif ".0" in str(temp):
      temp = math.ceil(temp)
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

if (is_end == False):
  os.system(f'echo "question:" >> $GITHUB_STEP_SUMMARY')

with open('n.txt', 'w') as file:
    file.write(str(temp))

with open('n_sequence.txt', 'w') as file:
    file.write(str(n_sequence + number_of_executions + 1))

maximums_arr = []
minimums_arr = []
for j in range(0, math.ceil(len(Hailstone_Num)/section_range)):
  
  maximums_arr.append(max(Hailstone_Num[(section_range*j):(section_range*(j+1) - 1)]))
  minimuns_arr.append(min(Hailstone_Num[(section_range*j):(section_range*(j+1) - 1)]))
# os.system(f'echo "구간별 최솟값: {str(minimuns_arr)}" >> $GITHUB_STEP_SUMMARY')
