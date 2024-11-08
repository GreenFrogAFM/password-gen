import random
import string
from sys import exit as sysExit

class password:
    def __init__(self, length: int, numbers: int , characters: int):
        self.length = length
        self.numbers = numbers
        self.characters = characters
    
    @property
    def passLen(self):
        return self.length

    @passLen.setter
    def passLen(self, length):
        self.length = length

    @property
    def passNum(self):
        return self.numbers
    
    @passNum.setter
    def passNum(self, numbers):
        self.numbers = numbers

    @property
    def passChar(self):
        return self.characters
    
    @passChar.setter
    def passChar(self, characters):
        self.characters = characters
        

def main():
    p = password(0, 0, 0)
    while True:
        try:
            getLength(p)
            haveNumbers(p)
            break
        except KeyboardInterrupt:
            if exitClause() == True:
                sysExit()
    total(p)

def total(pa: password):
    print(f"pass len: {pa.passLen}")
    print(f"pass num: {pa.passNum}")
    print(f"pass char: {pa.passChar}")


def exitClause() -> bool:
    MSG = "Would you like to exit the program? (y/n)\n"
    return yORn(input(MSG), MSG)


def getLength(pa: password):
        MSG = "How long is your desired password?\n"
        pa.passLen = tryInt(input(MSG), MSG)


def haveNumbers(pa: password):
    MSG = "Would you like your password to contain numbers? (y/n)\n"
    if yORn(input(MSG), MSG):
        pa.passNum = getNumbers(pa)
    else:
        pa.passNum = 0


def getNumbers(pa: password) -> int:
    while True:
        MSG = "How many numbers would you like?\n"
        numberCount = tryInt(input(MSG), MSG)
        if numberCount > pa.passLen:
            LARGER_MSG = ("The number count is larger than the password length\n"
                "would you like to change the password length to match the number count? (y/n)\n")
            modifyLength(pa, numberCount, LARGER_MSG)
            return numberCount
        else:
            return numberCount


def modifyLength(pa: password, largerValue: int, msg: str):
    while pa.passLen <= largerValue:
        if yORn(input(msg), msg):
            return getLength(pa) 
        else:
            #problem Here
            #if no to modifying passLen, passNum > passLen
            return pa.passLen


def yORn(inp: str, msg: str) -> bool:
    inp = inp.strip().lower()
    while True:
        match inp:
            case 'y':
                return True
            case 'n':
                return False
            case _:
                return yORn(input(msg), msg)
                

def tryInt(inp: str, msg: str):
    while True:
        try:
            inp = int(inp)
            return inp
        except ValueError:
            return tryInt(input(msg), msg)


if __name__=="__main__":
    main()
    