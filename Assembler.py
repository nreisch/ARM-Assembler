# ARM assembler

"""
Component:
    - Have to deal with whether the instruction is associated with data, memory, or branching
    -
Idea: Have multiple function calls in instructionToMachine and have that returned from that method
--------------------------------------
New Approach to Assembler -- Get each line and send that to a function
-- First just deal with Datapath instructions

"""

# Global Variables

instructionComponent = ""  # We append to the instruction component the characters to get the instruction component like "ADD"
machineInstruction = ""
isData = False
isMemory = False
isBranch = False

# Key - Value pair for Data, Memory, and Branch
Data = dict(ADD="00", SUB="01", AND="10", OR="11")


# End of Global Variables
def assembler(inputFileArg, outputFileArg):
    inputFile = open(inputFileArg, "r")  # r means open for reading
    outputFile = open(outputFileArg, "w+")  # w because we will write to the file, + means if no file create one

    # Declare global variables for use in method
    global instructionComponent  # We append to the instruction component the characters to get the instruction component like "ADD"
    global machineInstruction
    global isData
    global isMemory
    global isBranch

    for line in inputFile:
        # Analyze until the first space and send that to determine if Datapath, Control, or Branch
        for charComponent in line:
            # To first analyze if this will be a data, control, or branch instruction set
            if charComponent == " ":
                instructionToMachine()  # Argument would be instructionComponent but using globals because not returning any values
                instructionComponent = ""

            else:
                instructionComponent = instructionComponent + charComponent

            # The function that calls it will change the associated boolean and depending on which one it is will
            # call that method
            if isData:
                isDataInstruction()
            elif isMemory:
                isMemoryInstruction()
            elif isBranch:
                isBranchInstruction()

        isData = False
        isMemory = False
        isBranch = False

    outputFile.write(machineInstruction)
    outputFile.write("\n")

    inputFile.closed  # close the file
    outputFile.closed  # close the file


"""

Evaluates the instruction and outputs the machine code

"""


def instructionToMachine():
    # Key - Value

    # Call helper methods to determine if data, control, or branch

    global instructionComponent  # We append to the instruction component the characters to get the instruction component like "ADD"
    global machineInstruction
    global isData
    global isMemory
    global isBranch

    isDataInstruction()
    isMemoryInstruction()
    isBranchInstruction()

    # return switch.get(instructionComponent, "Invalid")  # i is the key, and outputs the value


def isDataInstruction():
    global instructionComponent  # We append to the instruction component the characters to get the instruction component like "ADD"
    global machineInstruction
    global isData
    global isMemory
    global isBranch
    global Data

    machineInstructionComponent = ""

    # If the instruction is one of the following then it is indeed associated with Data Therefore we set the boolean
    # value to true, and then we begin to translate from assembly to machine based on instruction set\
    # Handles bits 27 : 26 of machineInstruction

    # iterate over Data dictionary and if value is spotted then we can append to the machineInstructions and set
    # boolean vars

    # Iterate through dictionary and see if the instruction component is there, if it is set boolean val to true and append to machineInstruction
    if instructionComponent in Data:
        machineInstructionComponent = Data[instructionComponent]
        machineInstruction = machineInstruction + machineInstructionComponent
        isData = True



def isMemoryInstruction():
    global instructionComponent  # We append to the instruction component the characters to get the instruction component like "ADD"
    global machineInstruction
    global isData
    global isMemory
    global isBranch




def isBranchInstruction():
    global instructionComponent  # We append to the instruction component the characters to get the instruction component like "ADD"
    global machineInstruction
    global isData
    global isMemory
    global isBranch



if __name__ == '__main__':
    assembler("program.txt", "output.txt")
