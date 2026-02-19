from pwn import *

enc_flag = '551257106e1a52095f654f510a6b4954026c1e0304394100043a1c5654505b6b'
key_Len = 50000

hostname = 'mercury.picoctf.net'
port = 36449
ctn = remote(hostname, port)
ctn.recvuntil('This is the encrypted flag!\n')
