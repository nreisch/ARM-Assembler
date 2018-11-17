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

#####################################
# Global Variables

instructionComponent = ""  # We append to the instruction component the characters to get the instruction component like "ADD"
machineInstruction = ""
isData = False
isMemory = False
isBranch = False

# Boolean variables to check what we have analyzed so far

# Data Booleans and bits
cmdBool = False
cmd = ""
sBool = False
s = ""

############################

# Key - Value pair for Data, Memory, and Branch
Data = dict(ADD="0100", SUB="0010", AND="1000", OR="1111", ) # S is 0,
dataBranch = dict(ADDS="0100", SUBS="0010", ANDS="10", ORS="11", ) # S will be 1



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

        # After we have scanned the line, append to the String each of the bits

        # machineInstruction = cond + op + I + cmd + s + Rn + Rd + SRC2
        machineInstruction = cmd + s

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

    # Data Boolean vars and Strings
    global cmdBool
    global cmd
    global sBool
    global s

    # If the instruction is one of the following then it is indeed associated with Data Therefore we set the boolean
    # value to true, and then we begin to translate from assembly to machine based on instruction set\
    # Handles bits 27 : 26 of machineInstruction

    # iterate over Data dictionary and if value is spotted then we can append to the machineInstructions and set
    # boolean vars

    # Iterate through dictionary and see if the instruction component is there, if it is set boolean val to true and append to machineInstruction
    # First analyze the type of data instruction
    if instructionComponent in Data:

        if cmdBool == False and sBool == False:
            cmd = Data[instructionComponent]
            s = "0"
            cmdBool = True
            sBool = True

        isData = True

    ## Has an extra s for data instruction so sets certain flags
    elif instructionComponent in dataBranch:
        if cmdBool == False and sBool == False:
            cmd = dataBranch[instructionComponent]
            s = "1"
            cmdBool = True
            sBool = True

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
