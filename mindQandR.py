c = 8533139361076999596208540806559574687666062896040360148742851107661304651861689
n = 769457290801263793712740792519696786147248001937382943813345728685422050738403253
e = 65537
p=  475693130177488446807040098678772442581573
q = 1617549722683965197900599011412144490161

def egcd (a,b):
  if a ==0:
    return(b,0,1)
  else:
    g,y,x = egcd(b%a,a)
    return (g,x - (b //a) *y,y)

def modinv (a, m):
  g,x,y = egcd(a,m)
  if g!=1:
    raise Exception('modular inverse does not exist')
  else:
    return x%m

def dec_to_hex(msg):
  return hex(msg)[2:]
def hex_to_str(msg):
  return bytes.fromhex(msg).decode('ascii')

phi_n = (p-1)*(q-1)
d = modinv(e, phi_n)

encoded_msg = pow(c,d,n)
hex_msg = dec_to_hex(encoded_msg)
msg = hex_to_str(hex_msg)
print(msg)


print()
