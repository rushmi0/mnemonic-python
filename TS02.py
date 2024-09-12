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
    '1010':'A',
    '1011':'B',
    '1100':'C',
    '1101':'D',
    '1110':'E',
    '1111':'F' }

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

#-------------------------------------------------------------------------#


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


#-------------------------------------------------------------------------#


def binaryToHex(binary):
    hexEquivalent=''

    goodInput = False
    while not(goodInput):
        #binary_Value=input('Enter binary number (max 256 bits): \n> ').strip(' ')

        binaryValueLength = len(binary)
        goodInput = True    #assume it's good for now until proven otherwise

        if binaryValueLength > MAX_BITS_ALLOWED:
            print('Error. Too many digits.')
            #goodInput=False(int(entropy)).rstrip("L").lstrip("0x") or "0"
            continue    #go back to beginning of loop to try again
        if not(isValidBinary(binary)):     #make sure they only entered 1's & 0's
            print("Error! Only enter 1's & 0's, no spaces or letters")
            goodInput=False
            continue    #go back to beginning of loop to try again
        if binary == '':   #the conversion loop is skipped since the condition is never true
            binary='0000'     #avoid key errors if enter nothing
            hexEquivalent='0'

    if binaryValueLength%NIBBLE_SIZE !=0:     #if NOT divisible by 4,  add padding 0's to the left
        paddingZeros= NIBBLE_SIZE - binaryValueLength%NIBBLE_SIZE    #find if length is divisible by NIBBLE_SIZE of 4 (remainder). Subtract from 4 to find how many MORE digits need to be added to length IS divisible by 4
        binary = '0'*paddingZeros + binary    #add padding 0's to the left
        binaryValueLength = len(binary)    #recalculate length since we added to it


    #now to the actual conversion looping over string 4 characters at a time right to left
    rightIndex = binaryValueLength-1      #end index is 1 less than size (0 based)
    leftIndex = rightIndex -(NIBBLE_SIZE-1)    #NIBBLE_SIZE-1 since we need the 4 consecutive numbers. 0+3=3 but we include 0 and get values 0,1,2,3 (4 values)
    iterations = int(binaryValueLength/NIBBLE_SIZE)   #loop iterates over 4 character at a time until it runs out of the string
    for i in range(iterations):                 #loop is skipped altogether if they enter an empty string
        nibble = binary[leftIndex:(rightIndex+1)]      #get 4 characters from the string
        hexEquivalent = hexEquivalentsOfBinary[nibble] + hexEquivalent
        rightIndex -=NIBBLE_SIZE      #decrement indexes by 4
        leftIndex -=NIBBLE_SIZE

    return hexEquivalent


#-------------------------------------------------------------------------#


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


#-------------------------------------------------------------------------#


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




if __name__ == "__main__":
    stack_binary = []
    for i in range(1):
        binary = input("Enter binary number N0.{} \n|> ".format(i+1))
        stack_binary.append(binary)
        #print("Current Stack Input: {}".format(stack_binary))

    print()
    entropy = "".join(stack_binary)
    print("[Entropy Binary] \n> {}".format(entropy))

    print() # 111111111110000000000010000010000 | 1FFC00410
    hexadecimal = binaryToHex(entropy)
    print("[Binary -> Hexadecimal] \n> {}".format(hexadecimal))

    print()
    item = Hash_SHA256(hexadecimal)
    print("[Hexadecimal -> Sha256] \n> {}".format(item))


    print()
    hash = int(item, base=16)
    bin_value = bin(hash).rstrip("L").lstrip("0b") or "0"
    print("[Sha256 -> Binary] \n> {}".format(bin_value))



    #decimal = binary_to_decimal(entropy)
    #print("[Binary -> Decimal] \n> {}".format(decimal))
    print('---'*20)
    print()


    #print("List: {}".format(decimal))

    # +1 เลขฐาน10 ทั้งหมดใน
    #new_list = [x+1 for x in decimal]
    #print("List: {} +1".format(new_list))


#-------------------------------------------------------------------------#

'''
    list_binary = []
    while len(stack_binary) > 0:
        #binary = stack_binary.pop()
        #print("Current Stack: {}".format(stack_binary))

        decimal = binary_to_decimal(entropy)
        list_binary.append(decimal)
        #print("Current Decimal No.{} \n|> {}".format(x, list_binary))
'''

#-------------------------------------------------------------------------#

'''
    print()
    print("List: {}".format(list_binary))

    # +1 เลขฐาน10 ทั้งหมดใน
    new_list = [x+1 for x in list_binary]
    print("List: {} +1".format(new_list))
    
        message = "Hello ".join("World")
    print(message) #prints 'Hello World'
    
    vowels = ["a", "e", "i", "o", "u"]
    vowelsCSV = ",".join(vowels)
'''
