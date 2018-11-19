# ARM assembler

"""

Approach to Assembler
-- Get each line and send that to a function
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

# data Booleans and bits
condBool = False
opBool = False
cmdBool = False
sBool = False
rnBool = False
rdBool = False
iBool = False
srcBool = False
commaSeparated = False
cond = ""
op = ""
cmd = ""
s = ""
rn = ""
rd = ""
i = ""
src = ""
imm8 = ""
shiftBool = False

regCount = 0

############################

# Key - Value pair for data, Memory, and Branch
data = dict(ADD="0100", SUB="0010", AND="0000", ORR="1100", )  # S is 0,

dataSet = dict(ADDS="0100", SUBS="0010", ANDS="0000", ORS="1100", )  # S will be 1

registers = dict(R0="0000", R1="0001", R2="0010", R3="0011", R4="0100", R5="0101", R6="0110", R7="0111", R8="1000",
                 R9="1001", R10="1010", R11="1011", R12="1100", R13="1101", R14="1110", R15="1111")
hexCode = {
    "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000",
    "9": "1001", 'A': "1010", 'B': "1011", 'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"
}

branch = {

}

memory = {

}


# End of Global Variables
def assembler(inputFileArg, outputFileArg):
    inputFile = open(inputFileArg, "r")  # r means open for reading
    outputFile = open(outputFileArg, "w+")  # w because we will write to the file, + means if no file create one

    # Declare global variables for use in method
    global instructionComponent, machineInstruction, isData, isMemory, isBranch, commaSeparated, condBool, cond, opBool, op, iBool, i, \
        cmdBool, cmd, sBool, s, rnBool, rn, rdBool, rd, srcBool, src, regCount, imm8, shiftBool
    lineCount = 0
    for line in inputFile:
        lineCount = lineCount + 1
        # Analyze until the first space and send that to determine if Datapath, Control, or Branch
        iBool = False
        srcBool = False
        rdBool = False
        rnBool = False
        commaSeparated = False
        condBool = False
        cmdBool = False
        opBool = False
        sBool = False
        regCount = 0
        regCount = 0
        instructionComponent = ""

        count = 0
        for charComponent in line:
            length = len(line)
            # To first analyze if this will be a data, control, or branch instruction set After look at comma there
            # will be a space so only evaluate if comma set to False, otherwise if commaTrue neglect the next space
            if charComponent == " " and commaSeparated == False:
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
            elif count == length-1:
                if "\n" in charComponent:
                    instructionComponent = instructionComponent
                else:
                    instructionComponent = instructionComponent + charComponent
                instructionToMachine()
                instructionComponent = ""
            else:
                instructionComponent = instructionComponent + charComponent

                # The function that calls it will change the associated boolean and depending on which one it is will
                # call that method

            count = count + 1

        # At the end of the line, set the boolean vars back to False to account for the next line
        isData = False
        isMemory = False
        isBranch = False

        # After we have scanned the line, append to the String each of the bits

        # machineInstruction = cond + op + I + cmd + s + Rn + Rd + SRC2
        # if there is an immediate value, and there is a 2nd source...
        # Then we want to use imm8, if shift == False, rot = 0000
        if iBool is True and srcBool is True:
            machineInstruction = cond + " " + op + " " + i + " " + cmd + " " + s + " " + rn + " " + rd + " " + rot + " " + imm8
        elif iBool is False and srcBool is True:
            machineInstruction = cond + " " + op + " " + i + " " + cmd + " " + s + " " + rn + " " + rd + " " + rot + " " + imm8
        else:
            machineInstruction = cond + " " + op + " " + i + " " + cmd + " " + s + " " + rn + " " + rd + " " + " " + src

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
    global instructionComponent, machineInstruction, isData, isMemory, isBranch, data

    # data Boolean vars and Strings
    global condBool, cond, opBool, op, iBool, i, cmdBool, cmd, sBool, s, rnBool, rn
    global rdBool, rd, srcBool, src, regCount, shiftBool, imm8, rot

    # If the instruction is one of the following then it is indeed associated with data Therefore we set the boolean
    # value to true, and then we begin to translate from assembly to machine based on instruction set\
    # Handles bits 27 : 26 of machineInstruction

    # iterate over data dictionary and if value is spotted then we can append to the machineInstructions and set
    # boolean vars

    # Iterate through dictionary and see if the instruction component is there, if it is set boolean val to true and append to machineInstruction
    # First analyze the type of data instruction
    if instructionComponent in data:

        if cmdBool == False and sBool == False:
            cmd = data[instructionComponent]
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

    #### Now that we know we have a data instruction use the boolean variable isData and others to test for rest of sequence


    if isData and condBool is False:
        cond = "1110"
        condBool = True

    if isData and opBool is False:
        op = "00"
        opBool = True

    if isData and iBool is False:
        i = "0"

    elif isData and iBool is True:
        i = "1"

    # Test for registers based on immediate and convert those to machine We have reached the point of sequence where
    # we will analyze RD which is the destination and given that opBool is true we know it will either be a register
    # or a # immediate value
    if isData and rnBool is False and rdBool is False and opBool is True:
        if instructionComponent in registers:
            rd = registers[instructionComponent]
            regCount = regCount + 1
            rdBool = True
            return

    elif isData and rnBool is False and rdBool is True and opBool is True:
        if instructionComponent in registers:
            rn = registers[instructionComponent]
            regCount = regCount + 1
            rnBool = True
            return

    # If we have encountered Rd and Rn and we have reached a new instruction that is a register then srcBool = True

    if regCount == 2:
        srcBool = True

    val = instructionComponent
    # Converting from Hex to Bit value
    if isData and iBool is True and shiftBool is False and srcBool is True:
        imm8 = decToBinary(instructionComponent)
        rot = "0000"
    # If there is a case of shifting then we have to change rot and then change the src -- COME BACK TO
    elif isData and iBool is True and shiftBool is True and srcBool:
        print("Not sure yet")
    elif isData and iBool is False and srcBool is True:
        imm8 = registers[instructionComponent]
        imm8 = "0000" + imm8
        rot = "0000"
    elif isData and iBool is False and srcBool is False:
        src = "00000000000"
        rot = "0000"


def isMemoryInstruction():
    global instructionComponent
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


def decToBinary(instructionComponent):
    decimalVal = (int)(instructionComponent)
    str = bin(decimalVal)
    result = ""
    for character in str:
        if character is 'b':
            result = result + '0'
        else: result = result + character
    while len(result) != len(str):
        result = '0' + result

    return result

# Next thing to do is to get the value of instruction component and check to see if it is > than 255, if it is then
# We have to use a rotational value and we will set another boolean value to check if this rotation is needed and how to set


if __name__ == '__main__':
    assembler("program.txt", "output.txt")
