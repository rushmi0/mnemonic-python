import hashlib

#-------------------------------------------------------------------------#
# https://github.com/SleekPanther/binary-hexadecimal-conversion/blob/master/binary-hexadecimal-conversion.py

hexEquivalentsOfBinary = {
    '0000':'0',
    '0001':'1',
    '0010':'2',
    '0011':'3',
    '0100':'4',
    '0101':'5',
    '0110':'6',
    '0111':'7',
    '1000':'8',
    '1001':'9',
    '1010':'a',
    '1011':'b',
    '1100':'c',
    '1101':'d',
    '1110':'e',
    '1111':'f' }

binaryEquivalentsOfHex = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111' }

MAX_BITS_ALLOWED = 256       #used to limit user input
NIBBLE_SIZE = 4             #half a byte. (4 digits long of 1's and 0's)


def showWelcomeScreen():
    print('---'*35)
    userChoice=input('\tHex & Binary Converter \nEnter 1 to convert unsigned binary to hexadecimal \nEnter 2 to convert hexadecimal to unsigned binary \nYour choice: ')
    userChoice=userChoice.lstrip(' ')   #remove leading spaces
    if(userChoice[0]=='1'):     #check 1st character in string
        binaryToHex()
    elif(userChoice[0]=='2'):
        hexToBinary()
    else:
        print('\nProgram Done')


def binaryToHex():
    binaryValue=''
    hexEquivalent=''

    goodInput = False
    while not(goodInput):
        binaryValue=input('Enter binary number (max 256 bits): \n> ').strip(' ')
        binaryValueLength = len(binaryValue)
        goodInput = True    #assume it's good for now until proven otherwise

        if binaryValueLength > MAX_BITS_ALLOWED:
            print('Error. Too many digits.')
            goodInput=False
            continue    #go back to beginning of loop to try again
        if not(isValidBinary(binaryValue)):     #make sure they only entered 1's & 0's
            print("Error! Only enter 1's & 0's, no spaces or letters")
            goodInput=False
            continue    #go back to beginning of loop to try again
        if binaryValue == '':   #the conversion loop is skipped since the condition is never true
            binaryValue='0000'     #avoid key errors if enter nothing
            hexEquivalent='0'

    if binaryValueLength%NIBBLE_SIZE !=0:     #if NOT divisible by 4,  add padding 0's to the left
        paddingZeros= NIBBLE_SIZE - binaryValueLength%NIBBLE_SIZE    #find if length is divisible by NIBBLE_SIZE of 4 (remainder). Subtract from 4 to find how many MORE digits need to be added to length IS divisible by 4
        binaryValue = '0'*paddingZeros + binaryValue    #add padding 0's to the left
        binaryValueLength = len(binaryValue)    #recalculate length since we added to it

    #now to the actual conversion looping over string 4 characters at a time right to left
    rightIndex=binaryValueLength-1      #end index is 1 less than size (0 based)
    leftIndex=rightIndex -(NIBBLE_SIZE-1)    #NIBBLE_SIZE-1 since we need the 4 consecutive numbers. 0+3=3 but we include 0 and get values 0,1,2,3 (4 values)
    iterations = int(binaryValueLength/NIBBLE_SIZE)   #loop iterates over 4 character at a time until it runs out of the string
    for i in range(iterations):                 #loop is skipped altogether if they enter an empty string
        nibble = binaryValue[leftIndex:(rightIndex+1)]      #get 4 characters from the string
        hexEquivalent = hexEquivalentsOfBinary[nibble] +hexEquivalent
        rightIndex -=NIBBLE_SIZE      #decrement indexes by 4
        leftIndex -=NIBBLE_SIZE

    print()
    print('---'*35)
    print('[Binary -> Hexadecimal] \n> {}'.format(hexEquivalent))

    #print(type(hex_value))

    print()
    item = Hash_SHA256(hexEquivalent)
    print("[Hexadecimal -> Sha256] \n> {}".format(item))


    #print(binaryValue+' binary = '+hexEquivalent+' hex')
    #showWelcomeScreen()     #go back to main program


def hexToBinary():
    hexValue=input('Enter a hexadecimal number: \n> ').strip(' ').upper()    #remove leading/trailing spaces & force UPPERCASE
    if hexValue=='':
        hexValue = '0'      #avoid key errors on empty string
    binaryEquivalent=''
    for char in reversed(hexValue):     #loop skipped for empty strings
        try:
            binaryEquivalent= binaryEquivalentsOfHex[char] +binaryEquivalent
        except KeyError:        #if key is not in my list of valid conversions
            print('Error, you entered an invalid hex value. Try again')
            hexToBinary()     #exit loop & try again

    print()
    print('[Hexadecimal -> Binary] \n> {}'.format(binaryEquivalent))
    #print(hexValue+' hex = '+binaryEquivalent+' binary')
    #showWelcomeScreen()     #go back to main program


def isValidBinary(string):
    for char in string:         #loop through string. Return false if finds any character other than 1 or 0
        if(char !='0' and char!='1'):
            return False
    return True


def run_converter():
    showWelcomeScreen()

#-------------------------------------------------------------------------#
# https://teachbitcoin.io/presentations/bitcoinedge_keio_hd.html#/

def binary_to_decimal(num):
    b = list(num)
    n = len(list(num))
    decimal = 0
    hold = 0
    i = 0
    exp = n-1
    while (i < n):
        x = int(b[i])
        quot= 2**exp
        hold = x*quot
        i += 1
        exp -= 1
        decimal = decimal + hold
    return(decimal)

#-------------------------------------------------------------------------#

def Hash_SHA256(Item):
    Result = str(Item)
    hash = hashlib.sha256(Result.encode('utf-8')).hexdigest()
    return hash

#-------------------------------------------------------------------------#

# 0000000101010101001011000000000100000000001100000001111000000001010000000010000000000111000000100110000000100100000000110000000010111101111101100000001101000000011101000010110000000010000000000100010000001001000000000000010110000000000001010100000010110111

if __name__ == "__main__":
    stack_binary = []
    for i in range(1):
        binary = input("Enter binary number N0.{} \n|> ".format(i+1))

        if binary == "E" or binary == "e":
            print("Exit loop.")
            break

        stack_binary.append(binary)
        #print("Current Stack Input: {}".format(stack_binary))

    print()
    entropy = "".join(stack_binary)
    print("[Entropy Binary] \n> {}".format(entropy))

    run_converter()
    print()
    run_converter()
