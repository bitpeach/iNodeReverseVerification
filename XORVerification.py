#2014-11-11 by bitpeach
#-*- coding:cp936 -*-
import base64
import string
import binascii

secret_text = 'bGBeTUpXN3cuTEgycQV5foKo5pw='  #抓包iNode后，可以从request中拿到的base64编码
#publickey = 'HuaWei3COM1XHuaWei3C'
#publickey2= 'C3ieWauHX1MOC3ieWauH'
publickey = 'Oly5D62FaE94W7Oly5D6' #Oly5D62FaE94W7 一共14位
publickey2= '6D5ylO7W49EaF26D5ylO'

# encodestring(string) and decodestring(string)  
print "------------------------------------"  
print "[1]Secret Text:\t%s"  % secret_text 
hex_text=base64.decodestring(secret_text)

print "[2]Hex Before secret:\t"
for hex in hex_text:
     print "%#x\t" %ord(hex),
print"\r"
for hex in hex_text:
     print "%s\t" % hex,
print "\r[3]异或计算的每次结果:"  
#result = ''.join([chr(ord(x)^0x88) for x in hex_text])
#for c in result:
#     print "%#x" %ord(c), 
string1 = hex_text
string2 = publickey
#string3存放string1和string2异或结果
string3 = ''
string4 = publickey2
string5 = ''
print "第一次异或:"  
for i in range(len(string1)):
#   print "%s ^ %s = %s" % (bin(ord(string1[i])), bin(ord(string2[i])), bin(ord(string1[i]) ^ ord(string2[i])) )
    print "%#x ^ %#x = %s" % (ord(string1[i]), ord(string2[i]), bin(ord(string1[i]) ^ ord(string2[i])) ),
    string3 += chr(ord(string1[i]) ^ ord(string2[i]))
print "\r第二次异或:"  
for i in range(len(string1)):
#   print "%s ^ %s = %s" % (bin(ord(string1[i])), bin(ord(string2[i])), bin(ord(string1[i]) ^ ord(string2[i])) )
    print "%#x ^ %#x = %s" % (ord(string3[i]), ord(string4[i]), bin(ord(string3[i]) ^ ord(string4[i])) ),
    string5 += chr(ord(string3[i]) ^ ord(string4[i]))
print "\r[4]异或后的整体序列:" 
j = 0
for j,d in enumerate(string5):
    if j == 16: print "||",
    print "%#x" % ord(d),
#string5存放着前16字节和4个字节的随机数
print "\r[5]前16字节与随机数分离:" 
string6 = string5[:-4] #前16个字节
string7 = string5[-4:] #最后4个字节，随机数
print "前16字节:\t",
for i in string6:
     print "%#x" % ord(i),
print "\r随机数:\t\t",
for i in string7:
     print "%#x" % ord(i),  
string8 = ''
for i,temp in enumerate(string7):
    temp = ord(string7[i])>>4
    string8 += chr(temp)
    temp = ord(string7[i]) & ord('\x0F')
    string8 += chr(temp)
print"\r待转字符的随机数:\t",
for i in string8:
     print "%#x" % ord(i),
#-----------------------------------------------------
#print"\r已转字符的随机数:\t",
#operator = {'\x00':"0",'\x01':"1",'\x02':"2",'\x03':"3",'\x04':"4",\
#                '\x05':"5",'\x06':"6",'\x07':"7",'\x08':"8",'\x09':"9",\
#                '\x0a':"a",'\x0b':"b",'\x0c':"c",'\x0d':"d",'\x0e':"e",'\x0f':"f"}
#string9 = ''
#for i in string8: 
#        if operator.has_key(i):
#            temp = operator.get(i)
#            string9 += temp
#             
#for i in string9:
#     print "%#x" % ord(i), 
#-----------------------------------------------------
#string9 = "%02x%02x%02x%02x%02x%02x%02x%02x" %(ord(string8[0]),ord(string8[1]),ord(string8[2]),ord(string8[3]),ord(string8[4]),ord(string8[5]),ord(string8[6]),ord(string8[7])
#string9 = "cee4cee5"
string9 =  "%x%x%x%x%x%x%x%x" %(ord(string8[0]),ord(string8[1]),ord(string8[2]),ord(string8[3]),\
                                                ord(string8[4]),ord(string8[5]),ord(string8[6]),ord(string8[7]) )
#-----------------------------------------------------
print"\r已转字符的随机数:\t",
for i in string9:
     print i, 

print"\r构造异或使用的数1:\t",
string10 = string9 + string9
for i in string10:
     print "%#x" % ord(i),
print"\r构造异或使用的数2:\t",
string11 = string10[::-1]
for i in string11:
     print "%#x" % ord(i),
print "\r[6]最后一次异或还原真正的版本号:" 
string12 = ''
string13 = ''
print "第一次异或:"  
#print "%#x" % (ord('\x15') ^ ord('\x0c')) #这里的\0xc是十进制12，不是ASCII的c
for i in range(16):
#   print "%s ^ %s = %s" % (bin(ord(string1[i])), bin(ord(string2[i])), bin(ord(string1[i]) ^ ord(string2[i])) )
    print "%#x ^ %#x = %s" % (ord(string6[i]), ord(string10[i]), bin(ord(string6[i]) ^ ord(string10[i])) ),
    string12 += chr(ord(string6[i]) ^ ord(string10[i]))
print "\r第二次异或:" 
for i in range(16):
#   print "%s ^ %s = %s" % (bin(ord(string1[i])), bin(ord(string2[i])), bin(ord(string1[i]) ^ ord(string2[i])) )
    print "%#x ^ %#x = %s" % (ord(string12[i]), ord(string11[i]), bin(ord(string12[i]) ^ ord(string11[i])) ),
    string13 += chr(ord(string12[i]) ^ ord(string11[i]))
print "\r还原真正版本号:"
for i in string13:
     print "%#x\t" % ord(i),
print "\r" #CH\x12V5.20-0407
for i in string13:
     print i,"\t",
