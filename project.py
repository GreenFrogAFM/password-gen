from random import randint, choice, sample
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
            collectData(p)
            writeToFile(p, numberOfPasswords())
            break
        except KeyboardInterrupt:
            if exitClause() == True:
                sysExit()
    createPass(p)
    return 0


def collectData(pa: password):
    getLength(pa)
    haveNumbers(pa)
    haveChars(pa)
    passCheck(pa)


def createPass(pa: password) -> str:
    result = ""
    for _ in range(pa.passNum):
        result += "".join(str(randint(0, 9)))
    for _ in range(pa.passChar):
        result += "".join(choice(string.punctuation))
    for _ in range(pa.passLen - (pa.passChar + pa.passNum)):
        result += "".join(choice(string.ascii_letters))
    return ''.join(sample(result, len(result)))


def numberOfPasswords() -> int:
    while True:
        try:
            inp = int(input("how many of the specified password do you want to print to file?\n"))
            
            if inp <= 0:
                print("please enter at least 1 or more!")
                return numberOfPasswords()
            
            return inp
        except ValueError:
            return numberOfPasswords()


def writeToFile(pa:password, num: int):
    with open("passwords.txt", 'w+') as file:
        for _ in range(num):
            file.write(f"{createPass(pa)}\n")
        file.close()
        print("Process Finished!")


def exitClause() -> bool:
    MSG = "Would you like to exit the program? [Y]es / [N]o\n"
    return yORn(input(MSG), MSG)


def getLength(pa: password, looped: bool = False):
        while (pa.passLen <= pa.passNum ) or (pa.passLen <= pa.passChar):
            if not looped:
                MSG = "How long is your desired password?\n"
            else:
                MSG = f"What's the new password length? (must be larger than {pa.passChar or pa.passNum})\n"
            pa.passLen = tryInt(input(MSG), MSG)
            break


def haveNumbers(pa: password):
    MSG = "Would you like your password to contain numbers? [Y]es / [N]o\n"
    if yORn(input(MSG), MSG):
        getNumbers(pa)
    else:
        pa.passNum = 0


def getNumbers(pa: password, looped: bool = False):
    while True:
        if not looped:
            MSG = "How many numbers would you like?\n"
            numberCount = tryInt(input(MSG), MSG)
        else:
            MSG = (f"How many special character would you like?\n"
            f"must be equal or less than {pa.passLen - pa.passChar}\n")
            numberCount = tryInt(input(MSG), MSG)
        
        if numberCount > pa.passLen:
            LARGER_MSG = ("The number count is larger than the password length\n"
                "would you like to change the password length to match the number count? [Y]es / [N]o\n")
            pa.passNum = numberCount
            modifyLength(pa, numberCount, LARGER_MSG, getNumbers)
            break
        else:
            pa.passNum = numberCount
            break


def haveChars(pa: password):
    MSG = "Would you like your password to contain special characters? [Y]es / [N]o\n"
    if yORn(input(MSG), MSG):
        getChars(pa)
    else:
        pa.passChar = 0


def getChars(pa: password, looped: bool = False):
    while True:

        if not looped:
            MSG = "How many special characters would you like?\n"
            charCount = tryInt(input(MSG), MSG)
        else:
            MSG = (f"How many special character would you like?\n"
            f"must be equal or less than {pa.passLen - pa.passNum}\n")
            charCount = tryInt(input(MSG), MSG)

        if charCount > pa.passLen:
            LARGER_MSG = ("The number of special characters is larger than the password length\n"
                "would you like to change the password length to match the number count? [Y]es / [N]o\n")
            pa.passChar = charCount
            modifyLength(pa, charCount, LARGER_MSG, getNumbers)
            break
        else:
            pa.passChar = charCount
            break


def modifyLength(pa: password, largerValue: int, msg: str, sender):
    while pa.passLen <= largerValue:
        if yORn(input(msg), msg):
            return getLength(pa, True) 
        else:
            sender(pa)
            break
            

def passCheck(pa: password):
    while (pa.passChar > pa.passLen - pa.passNum) or (pa.passNum > pa.passLen - pa.passChar):
        print(f"The password length will not fit all {pa.passNum} numbers\n"
              f"and {pa.passChar} special characters!\n")
        MSG = (f"Please Choose whether to [R]estart, change the [N]umber count or the [C]haracter count.\n")
        passFix(pa, input(MSG), MSG)
        break


def passFix(pa: password, inp: str, msg: str):
    inp = inp.strip().lower()
    while True:
        match inp:
            case 'r':
                collectData(pa)
                break
            case 'n':
                getNumbers(pa, True)
                break
            case 'c':
                getChars(pa, True)
                break
            case _:
                passFix(input(msg), msg)
                break


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
                

def tryInt(inp: str, msg: str) -> int:
    while True:
        try:
            inp = int(inp)
            return inp
        except ValueError:
            return tryInt(input(msg), msg)


if __name__=="__main__":
    main()
    