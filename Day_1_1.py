
#Read all input from file
input_file = open("Day_1_Input.txt", "r")
lines = input_file.read()
input_file.close()

#Add all line from file to a list named list_of_lines
list_of_lines = lines.splitlines()

#counter for the for loop
for_count = 0
first_num = 0
sec_num = 0

for i in list_of_lines:
    for a in list_of_lines[for_count:]:
        ans = int(i) + int(a)
        if ans == 2020:
            first_num = int(i)
            sec_num = int(a)
            break
    else:
        continue
    break
    for_count = for_count + 1

answer = first_num * sec_num
print(answer)