
class Instruction:
    def __init__(self, instruction, value, visited):
        self.instruction = instruction
        self.value = value
        self.visited = visited


def runProgram(program):
    index = 0
    accumulator = 0
    program_is_complete = False

    while True:
        if index == len(program):
            ''' The program arrived at the end '''
            program_is_complete = True
            break

        current_instruction = program[index]

        if current_instruction.visited == 1:
            ''' Termiantion condition: we've already visited this instruction '''
            break


        current_instruction.visited = 1

        next_index_offset = 1
        if current_instruction.instruction == "acc":
            accumulator += current_instruction.value
        elif current_instruction.instruction == "jmp":
            next_index_offset = current_instruction.value

        index += next_index_offset

    return accumulator, program_is_complete



''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

program = []
for line_dirty in content:
    line = line_dirty.replace("\n", "")
    [instruction, value] = line.split(" ")

    '''
    Each instruction is saved in an array, so that their relative position
    is fixed via their index, and the value is an object composed by 
        the name of the instruction, 
        the numerical value associated to it,
        and a flag that is 0 if the instruction hasn't been visited yet 
    '''
    program.append(Instruction(instruction, int(value), 0))

accumulator = 0
for index, instruction in enumerate(program):
    old_instruction = instruction.instruction

    ''' Set all the visited flag to 0 '''
    for iter_instr in program:
        iter_instr.visited = 0


    ''' Change the possibly corrupted instruction '''
    if program[index].instruction == "jmp":
        program[index].instruction = "nop"
    elif program[index].instruction == "nop":
        program[index].instruction = "jmp"
    else:
        continue


    accumulator, program_is_complete = runProgram(program)

    if program_is_complete == True:
        ''' The program was successful '''
        break

    program[index].instruction = old_instruction


print("The accumulator for the corect program is " + str(accumulator))
