

class Instruction:
    def __init__(self, instruction, value, visited):
        self.instruction = instruction
        self.value = value
        self.visited = visited

def runProgram(program):
    index = 0
    accumulator = 0

    while True:
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

    return accumulator



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

accumulator = runProgram(program)

print("The last valid value of the accumulator is " + str(accumulator))

