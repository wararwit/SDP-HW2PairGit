print("Random number is")
import random

random_number=random.randrange(0, 100000, 1)


z=random_number

bit1=z%10;
bit2=z%10/5;
bit3=z%100/10;
bit4=z%1000/100;
bit5=z%10000/1000;
bit6=z%100000/10000;
bit7=9;



print bit6,bit5,bit4,bit3,bit2,bit1,bit7

print("fix bit1 = 9")

