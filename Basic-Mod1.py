"""mod1: Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore."""

nums = '128 63 242 87 151 147 50 369 239 248 205 346 299 73 335 189 105 293 37 214 333 137'.split()


msg =""

newNums = []
for num in nums:
  num = int(num)%37
  if( num <26):
    msg += (chr(num+65))
  elif(num<36):
    msg += (chr(num+22))
  else:
    msg += (chr(num+59))

print("picoCTF{"+msg+"}")
