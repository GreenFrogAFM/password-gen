# Password-gen

__Password-gen__ once opend will prompt the user for the desired password length, then will ask whether the user would like numbers or special character in said password, after that the user will be prompted to enter how many password to create under the previous specifications, which will then be created in a __passwords.txt__ file located in the program directory (aka. the same folder the __project.py__ was ran in).

This works by concatenating the required characters (using __join__ from string module), we get these character by calling __string.ascii_letters__ for the letters, __string.punctuation__ for the special characters and casting into a str the result from __randint__ to get the numbers (from 0 to 9).
#

## Password Class
The Password class works as a container to for the length of the password, the number of numbers in the password and the number of special characters, all of them are stored as ints.

## Main

The __Main__ function does 4 things:
1. Call __collectData__: which calls all the functions which take user input to construct the password.

2. Call __numberOfPasswords__: prompts the user for how many password they want to create.

3. Call __writeToFile__: which takes the number from __numberOfPasswords__ to write to "passwords.txt".

4. Call __exitClause__ which wraps all the previous functions, to let the user exit in case they enter shift+C.

## collectData
as mentioned before __collectData__ calls functions that collect data from the user required in constructing the password parameters from these functions:

1. __getLength__: prompts the user for the length of the password.

2. __haveNumbers__: asks the user whether they want numbers in the password or not, if prompted with (yes) it will call __getNumbers__ which prompts the user for how many numbers they want in the password, if the number entered is higher than the password length then __modifyLength__ will be called to prompt the user whether to change the password length or the number of numbers (in the password) entered.

3. __haveChars__: same as __haveNumbers__ above including calling __getChars__ instead of __getNumbers__ and calling __modifyLength__ as well.

4. __passCheck__: checks for the int(s) of the password so a for example a length 12 password won't include 11 number and 6 special characters (11 + 6 = 17) 17 is larger than 12 so __passCheck__ will call __passFix__.

## __passFix__
Gets called by __passCheck__ as mentioned above and prompts the user for one of three inputs:
1. R for reset which will call __collectData__ which will overwrite all of the data collected with the new ones.

2. N for changing the number of numbers in the password by calling __getNumbers__.

3. C for changing the number of special character in the password by calling __getChars__


## __yORn__

a simple function called by other function for yes/no input, compiled as a single function instead of having to Implement it everywhere the user is prompted for a yes/no question, returns __True__ for y and __False__ for n.

## __tryInt__

same as yORn, called by other function whenever user is required to enter a number (int) and loops itself until an appropriate answer is given.

## __createPass__

a function exclusively called by __writeToFile__ to create a password (a string) from the given parameters.
Contains three loops:
1. The first adds numbers by joining in empty string with string casted ranfint.

2. The second loop adds the special character by joining an empty string with a random __string.punctuation__ using __random.choice__.

3. Same as above but instead gets all letters from __string.ascii_letters__ (lowercase and uppercase).
