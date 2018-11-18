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
condBool = False
cond = ""

opBool = False
op = ""

cmdBool = False
cmd = ""

sBool = False
s = "0"

rnBool = False
rn = ""

rdBool = False
rd = ""

iBool = False
i = ""

srcBool = False
src = ""

commaSeparated = False

############################

# Key - Value pair for Data, Memory, and Branch
Data = dict(ADD="0100", SUB="0010", AND="1000", OR="1111", )  # S is 0,
dataSet = dict(ADDS="0100", SUBS="0010", ANDS="10", ORS="11", )  # S will be 1
registers = dict(R0="0000", R1="0001", R2="0010", R3="0011", R4="0010", R5="0101", R6="0110", R7="0111", R8="1000",
                 R9="1001", R10="1010", R11="1011", R12="1100", R13="1101", R14="1110", R15="1111")
hexCode = {
    "1":"0001", "2":"0010", "3":"0011", "4":"0100", "5":"0101", "6":"0110", "7":"0111", "8":"1000",
    "9":"1001", 'A':"1010", 'B':"1011", 'C':"1100", 'D':"1101", 'E':"1110", 'F':"1111"
}

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
    global commaSeparated
    global iBool
    global srcBool


    for line in inputFile:
        # Analyze until the first space and send that to determine if Datapath, Control, or Branch
        count = 0
        for charComponent in line:
            length = len(line)
            # To first analyze if this will be a data, control, or branch instruction set After look at comma there
            # will be a space so only evaluate if comma set to False, otherwise if commaTrue neglect the next space
            if charComponent == " "  and commaSeparated == False:
                val = instructionComponent
                instructionToMachine()  # Argument would be instructionComponent but using globals because not returning any values
                instructionComponent = ""
            elif count == length-1:
                val = instructionComponent
                instructionToMachine()  # Argument would be instructionComponent but using globals because not returning any values
                instructionComponent = ""
            elif charComponent == " " and commaSeparated == True:
                commaSeparated = False
                instructionComponent = ""
            elif charComponent == ",":
                val = instructionComponent
                instructionToMachine()  # Argument would be instructionComponent but using globals because not returning any values
                instructionComponent = ""
                commaSeparated = True
            # The value in src is an immediate and not from a Reg
            elif charComponent == '#':
                iBool = True
                srcBool = True
                instructionComponent = ""
            elif charComponent == " " and iBool == True and srcBool == True:
                val = instructionComponent
                instructionToMachine()
                instructionComponent = ""
                iBool = False

            else:
                instructionComponent = instructionComponent + charComponent

                # The function that calls it will change the associated boolean and depending on which one it is will
                # call that method

            count = count + 1
        """
        ## Not really necessary because by the time this is hit, the instructionComponent will be empty
        
        if isData:
            isDataInstruction()
        elif isMemory:
            isMemoryInstruction()
        elif isBranch:
            isBranchInstruction()
        """

        isData = False
        isMemory = False
        isBranch = False

        # After we have scanned the line, append to the String each of the bits

        # machineInstruction = cond + op + I + cmd + s + Rn + Rd + SRC2
        machineInstruction = cond + " " + op + " " + i + " " + cmd + " " + s + " " + rn + " " + rd + " " + src

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
    global condBool
    global cond
    global opBool
    global op
    global iBool
    global i
    global cmdBool
    global cmd
    global sBool
    global s
    global rnBool
    global rn
    global rdBool
    global rd
    global srcBool
    global src

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
    elif instructionComponent in dataSet:
        if cmdBool == False and sBool == False:
            cmd = dataSet[instructionComponent]
            s = "1"
            cmdBool = True
            sBool = True

        isData = True

    #### Now that we know we have a Data instruction use the boolean variable isData and others to test for rest of sequence

    if isData and condBool == False:
        cond = "1110"
        condBool = True

    if isData and opBool == False:
        op = "00"
        opBool = True

    # Test for registers based on immediate and convert those to machine We have reached the point of sequence where
    # we will analyze RD which is the destination and given that opBool is true we know it will either be a register
    # or a # immediate value
    if isData and rnBool == False and rdBool == False and opBool == True:
        if instructionComponent in registers:
            rd = registers[instructionComponent]
            rdBool = True

    elif isData and rnBool == False and rdBool == True and opBool == True:
        if instructionComponent in registers:
            rn = registers[instructionComponent]
            rnBool = True

    if isData and iBool == False:
        i = "0"

    elif isData and iBool == True:
        i = "1"

    # Converting from Hex to Bit value
    if isData and iBool == True and srcBool == True:
        src = fromHexToBinary(instructionComponent)

    elif isData and iBool == False and srcBool == False:
        src = "00000000000"


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


def fromHexToBinary(instructionComponent):
    # Hex to Binary
    result = ""
    for key in instructionComponent:
        if key in hexCode:
            result += hexCode[key]

    return result

if __name__ == '__main__':
    assembler("program.txt", "output.txt")
