#2014-11-11 by bitpeach
#-*- coding:cp936 -*-
import hashlib
print "[1]request数据包内的value:"
string1 = '\x75\x48\x65\x59\x6e\x32\x41\x63\x06\x07\x23\xc8\x64\x0a\x3b\x23'
for i in string1:
    print "%02x" % ord(i),
tips = '\x02'

print "\r[2]我的上网密码:"
string2 = '204108'
for i in string2:
    print "%s" % i,
    
print "\r[3]原文序列（ASCII序列）:"
#string3 = string1 + string2
string3 = tips + string2 + string1
for i in string3:
    print "%#02x" % ord(i),

print "\r[4]MD5加密后的序列(十六进制内容):"  
md5=hashlib.md5(string3).hexdigest()
#for i in md5:
#    print "%#02x" % ord(i),
#print '\r' 
i = 0
while i <= (len(md5)-2):
    print "%s" %(md5[i:i+2]), 
    i += 2
