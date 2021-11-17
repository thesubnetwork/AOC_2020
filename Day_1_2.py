
#Read all input from file
input_file = open("Day_1_Input.txt", "r")
lines = input_file.read()
input_file.close()

#Add all line from file to a list named list_of_lines
list_of_lines = lines.splitlines()

for i in list_of_lines:
    for a in list_of_lines:
        for z in list_of_lines:
            ans = int(i) + int(a) + int(z) 
            if ans == 2020:
                answer = int(i) * int(a) * int(z)

print(answer)

        
