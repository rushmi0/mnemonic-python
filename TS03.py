import hashlib

#-------------------------------------------------------------------------#


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

MAX_BITS_ALLOWED = 256
NIBBLE_SIZE = 4


#-------------------------------------------------------------------------#


def isValidBinary(string):
    for char in string:
        if(char !='0' and char!='1'):
            return False
    return True


#-------------------------------------------------------------------------#


def binary_to_hex(binary):
    hexEquivalent=''

    goodInput = False
    while not(goodInput):
        #binary_Value=input('Enter binary number (max 256 bits): \n> ').strip(' ')

        binaryValueLength = len(binary)
        goodInput = True

        if binaryValueLength > MAX_BITS_ALLOWED:
            print('Error. Too many digits.')
            #goodInput=False(int(binary)).rstrip("L").lstrip("0x") or "0"
            continue

        if not(isValidBinary(binary)):
            print("Error! Only enter 1's & 0's, no spaces or letters")
            goodInput = False
            continue

        if binary == '':
            binary='0000'
            hexEquivalent='0'

    if binaryValueLength%NIBBLE_SIZE !=0:
        paddingZeros= NIBBLE_SIZE - binaryValueLength%NIBBLE_SIZE
        binary = '0'*paddingZeros + binary
        binaryValueLength = len(binary)


    rightIndex = binaryValueLength-1
    leftIndex = rightIndex -(NIBBLE_SIZE-1)
    iterations = int(binaryValueLength/NIBBLE_SIZE)
    for i in range(iterations):
        nibble = binary[leftIndex:(rightIndex+1)]
        hexEquivalent = hexEquivalentsOfBinary[nibble] + hexEquivalent
        rightIndex -= NIBBLE_SIZE
        leftIndex -= NIBBLE_SIZE

    return hexEquivalent


#-------------------------------------------------------------------------#


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
    return decimal


#-------------------------------------------------------------------------#


def Hash_SHA256(Item):
    hash = hashlib.sha256(Item.encode('utf-8')).hexdigest()
    return hash


#-------------------------------------------------------------------------#


if __name__ == "__main__":

    stack_binary = []

    for i in range(2): #11111111111 00000000000 10000010000
        binary = input("Enter binary number N0.{} \n> ".format(i+1))
        stack_binary.append(binary)
        #print("Current Stack Input: {}".format(stack_binary))

    print("Stack binary", stack_binary)
    print()
    entropy = "".join(stack_binary)
    print("[Entropy Binary] \n> {}".format(entropy))
    print('--'*35)

    print()
    decimal = binary_to_decimal(stack_binary)
    print("[Binary -> Decimal] \n> {}".format(decimal))


    print() # 111111111110000000000010000010000 | 1FFC00410
    hexadecimal = binary_to_hex(entropy)
    print("[Binary -> Hexadecimal] \n> {}".format(hexadecimal))
    print('--'*35)


    print()
    item = Hash_SHA256(hexadecimal)
    print(type(item))
    print("[Hexadecimal -> Sha256] \n> {}".format(item))
    print('--'*35)


    print()
    hexValue = item.upper()
    if hexValue=='':
        hexValue = '0'
    binaryEquivalent=''
    for char in reversed(hexValue):
        try:
            binaryEquivalent= binaryEquivalentsOfHex[char] +binaryEquivalent
        except KeyError:
            print('Error, you entered an invalid hex value. Try again')

    print("[Sha256 -> Binary] \n> {}".format(binaryEquivalent))
    print('--'*35)


