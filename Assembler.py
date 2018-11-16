# ARM assembler

"""

 First component: read an input from a textfile, analyzes each line
 Second Component: For each line in the input file, write out to an output file
 New Component:
    - When reading the line have to separate chars in the line to account for each component, we call each character componentChar of that instruction - so get a resulting string
    - We call it instructionComponent which is the operational code - may be RD, ADD, some other instruction and we add that to the resutling string
New Component:
    - Just deal with the basic inputs
"""
def assembler(inputFileArg, outputFileArg):
    inputFile = open(inputFileArg,"r") # r means open for reading
    outputFile = open(outputFileArg,"w+") # w because we will write to the file, + means if no file create one

    for line in inputFile:
        # Holds the resulting string for each component and we send this to a method to analyze what instruction it is
        instructionComponent = ""
        # The machine code that our assembler will send to output
        machineInstruction = ""

        # line is a text string, for every line we have to analyze the strings and iterate through the string for the instructions
        for charComponent in line:
            # * Will mark end of line, Second if statement takes care of last instruction not having a space at the end
            if (charComponent == "-"):
                machineInstruction = instructionToMachine(instructionComponent)  # returns the resulting ones and zeros for that component
                outputFile.write(machineInstruction)
                instructionComponent = ""
            elif(charComponent != " "):
                instructionComponent = instructionComponent + charComponent
            else:
                # If the component is a space that means we first analyze the instructionComponent and send it to our method
                # Then we bring the instructionComponent back to an empty string to analyze next portion
                machineInstruction = instructionToMachine(instructionComponent) #returns the resulting ones and zeros for that component
                outputFile.write(machineInstruction)
                instructionComponent = ""

    outputFile.write("\n")

    inputFile.closed # close the file
    outputFile.closed # close the file



"""

Evaluates the instruction and outputs the machine code

"""
def instructionToMachine(instructionKey):
    # Key - Value

    # Might need to call other helper methods on Instruction Key -- not entirely sure yet
    switch = {
        "ADD":"1",
        "SUB":"0"

    }

    return switch.get(instructionKey,"Invalid") # i is the key, and outputs the value



if __name__ == '__main__':
    assembler("program.txt","output.txt")