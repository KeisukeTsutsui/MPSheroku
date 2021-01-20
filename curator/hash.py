
import string
import secrets
import hashlib

dat = 'python' 

# SHA256のハッシュ値
hs1 = hashlib.sha256(dat.encode()).hexdigest()
print(hs1) 

#[結果] 11a4a60b518bf24989d481468076e5d5982884626aed9faeb35b8576fcd223e1

val = input()

hs2 = hashlib.sha256(val.encode()).hexdigest()

if(hs1 == hs2):
    print('true')

num = [2,3,4,5,6,7,8,9] #1,9は抜く
small = ['a','b','c','d','e','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z'] #l,oは抜く
#big = ['A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z'] #O,Iは抜く
pass = null


