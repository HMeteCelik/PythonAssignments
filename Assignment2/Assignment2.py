print("""<-----RULES----->
1. BRUSH DOWN
2. BRUSH UP
3. VEHICLE ROTATES RIGHT
4. VEHICLE ROTATES LEFT
5. MOVE UP TO X
6. JUMP
7. REVERSE DIRECTION
8. WIEW THE MATRIX
0. EXIT
""")
command_line = input("Please enter the commands with a plus sign (+) between them.""\n")
command_line = command_line.split("+")
must_command_line = ["0","1","2","3","4","5","6","7","8"]
for i in command_line[1: ]:
    for i in command_line[1: ]:
        while i[0] not in must_command_line:
            print("You entered an incorrect command. Please try again!")
            command_line = input("")
            command_line = command_line.split("+")
            break
for i in command_line[1:]:
    for i in command_line[1:]:
        if i[0] == "5":
            while i[1] != "_":
                print("You entered an incorrect command. Please try again!")
                command_line = input("")
                command_line = command_line.split("+")
                break
            while i[2:].isdigit == False:
                print("You entered an incorrect command. Please try again!")
                command_line = input("")
                command_line = command_line.split("+")
                break
command_line[0] = int(command_line[0])
matrix = [["0" for c in range(command_line[0])] for p in range(command_line[0])]
cars_direction = 0
brush_position = 0
current_position = [0,0]
command_line = command_line[1:]
def rotate(x):                      # 0 = turn right 1 = turn left
    global cars_direction 
    if x ==0:
        cars_direction = (cars_direction+1)%4 
    elif x ==1:
        cars_direction = (cars_direction-1)%4
def change_brush_position(y):
    global brush_position
    if y ==0:                       # 0 = brush up 1 = brush down
        brush_position = 0
    elif y ==1:
        brush_position = 1
        matrix[current_position[0]][current_position[1]]="1"
def move(z):                        # 0=right 1=down 2=left 3=up
    global current_position
    global matrix
    global cars_direction
    if cars_direction ==0:
        for i in range(z):
            current_position[1] = (current_position[1]+1)%len(matrix)
            if brush_position ==1:
                matrix[current_position[0]][current_position[1]]="1"
    elif cars_direction ==1:
        for i in range(z):
            current_position[0] = (current_position[0]+1)%len(matrix)
            if brush_position ==1:
                matrix[current_position[0]][current_position[1]]="1"
    elif cars_direction ==2:
        for i in range(z):
            current_position[1] = (current_position[1]-1)%len(matrix)
            if brush_position ==1:
                matrix[current_position[0]][current_position[1]]="1"
    elif cars_direction ==3:
        for i in range(z):
            current_position[0] = (current_position[0]-1)%len(matrix)
            if brush_position==1:
                matrix[current_position[0]][current_position[1]]="1"
def reverse():
    global cars_direction 
    if cars_direction ==0:
        cars_direction = 2
    elif cars_direction ==1:
        cars_direction =3
    elif cars_direction == 2:
        cars_direction =0
    elif cars_direction == 3:
        cars_direction=1
def jump():
    global brush_position 
    brush_position = 0
    if cars_direction ==0:
        current_position[1] = (current_position[1]+3)%len(matrix)
    elif cars_direction==1:
        current_position[0] =  (current_position[0]+3)%len(matrix)
    elif cars_direction ==2:
        current_position[1] = (current_position[1]-3)%len(matrix)
    elif cars_direction==3:
        current_position[0] = (current_position[0]-3)%len(matrix)
for i in command_line:
    if i =="1":
        change_brush_position(1)
    elif i =="2":
        change_brush_position(0)
    elif i =="3":
        rotate(0)
    elif i =="4":
        rotate(1)
    elif i[0]=="5":
        j = i.split("_")
        j[1] = int(j[1])
        move(j[1])
    elif i =="6":
        jump()
    elif i == "7":
        reverse()
    elif i == "8":
        for m in range(len(matrix)):
            for n in range(len(matrix)):
                if matrix[m][n] == "0":
                    matrix[m][n] =" "
                else:
                    matrix[m][n] = "*"
        print("+"*(len(matrix)+2))
        for q in matrix:
            print("+",*q,"+",sep="")
        print("+"*(len(matrix)+2))
    elif i =="0":
        exit()