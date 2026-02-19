f = open('message .txt','r')
nums =[]
for line in f.readlines():
  for num in line.split():
    nums.append(num)
  
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
      
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

      
msg =""

for num in nums:
  num = int(num)%41
  num= modinv(num, 41)
  if( num < 27):
    msg += (chr(num+64))
  elif(num < 37):
    msg += (chr(num+21))
  else:
    msg += (chr(num+58))

print("picoCTF{"+msg+"}")
