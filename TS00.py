
import hashlib
import math

# แปล เลขฐาน2 เป็น เลขฐาน10
def binary_to_decimal(binary):
    b = list(binary)
    n = len(list(binary))
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

#-------------------------------------------------------------------------

# Hash ข้อมูลด้วย SHA256
def Hash_SHA256(Item):
    Result = str(Item)
    hash = hashlib.sha256(Result.encode('utf-8')).hexdigest()
    return hash

#-------------------------------------------------------------------------

'''

   ใส่ค่า เลขฐาน2 ที่เราสุ่มมา "0" หรือ "1"
   เช่น เลขฐาน2 ความยาว 253bits
>> 0000000101010101001011000000000100000000001100000001111000000001010000000010000000000111000000100110000000100100000000110000000010111101111101100000001101000000011101000010110000000010000000000100010000001001000000000000010110000000000001010100000010110

'''
print()
binary = input("Enter binary number : ")

# นำเลขฐาน2 ที่เราสุ่มมา ส่งไปที่ "binary_to_decimal" เพิ่อแปลงเป็น เลขฐาน10
decimal = binary_to_decimal(binary)
print("Decimal : ", decimal)

# นำเลขฐาน2
hexadecimal = hex(int(binary)).rstrip("L").lstrip("0x") or "0"
print("Binary to Hexadecimal : ", hexadecimal)

item = Hash_SHA256(hexadecimal)
print()
print("Hex to Hashed : ", item)

# Convert to Integer
int_value = int(item, base=16)

# Convert integer to a binary value
bin_value = bin(int_value).rstrip("L").lstrip("0b") or "0"
print("SHA256 to Binary : ", bin_value)







