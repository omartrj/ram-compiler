import sys

# take the file name from the user
file_name = sys.argv[1]
print("File name: " + file_name + "\n")

with open(file_name, "r") as f:
    ram = f.readlines()

# remove the \n from the end of each line
ram = [line.strip() for line in ram]


ic = 0 # the instruction counter
mem = [0] * 100 # the memory
mem[0] = 0 # the accumulator


while True:
    if ic >= len(ram):
        break

    print("Accumulator: " + str(mem[0]))
    # find the last non-zero element in the memory
    # and print the memory from 1 to that element
    last_non_zero = 0
    for i in range(len(mem)):
        if mem[i] != 0:
            last_non_zero = i
    for i in range(1, last_non_zero + 1):
        print("Register " + str(i) + ": " + str(mem[i]))
    print("Instruction counter: " + str(ic + 1))
    print("\n")

    command = ram[ic]
    if command == "HALT":
        print("Command: " + command)
        break
    else:
        # split the line into the command and the argument
        command, arg = ram[ic].split(" ")
        print("Command: " + command)
        print("Argument: " + arg)

    if command == "LOAD":
        if arg[0] == "#":
            mem[0] = int(arg[1:])
        else:
            mem[0] = mem[int(arg)]
    elif command == "STORE":
        mem[int(arg)] = mem[0]
    elif command == "ADD":
        if arg[0] == "#":
            mem[0] += int(arg[1:])
        else:
            mem[0] += mem[int(arg)]
    elif command == "SUB":
        if arg[0] == "#":
            mem[0] -= int(arg[1:])
        else:
            mem[0] -= mem[int(arg)]
    elif command == "MULT":
        if arg[0] == "#":
            mem[0] *= int(arg[1:])
        else:
            mem[0] *= mem[int(arg)]
    elif command == "DIV":
        if arg[0] == "#":
            mem[0] //= int(arg[1:])
        else:
            mem[0] //= mem[int(arg)]
    elif command == "JUMP":
        ic = int(arg) - 1
        continue
    elif command == "JZERO":
        if mem[0] == 0:
            ic = int(arg) - 1
            continue
    elif command == "JGTZ":
        if mem[0] > 0:
            ic = int(arg) - 1
            continue
    elif command == "WRITE":
        if arg[0] == "#":
            print("Output: " + arg[1:])
        else:
            print("Output: " + str(mem[int(arg)]))
    elif command == "READ":
        mem[int(arg)] = int(input("Enter a number: "))
    else:
        print("Invalid command")
        break
    ic += 1

print("\nTerminated :)")

    