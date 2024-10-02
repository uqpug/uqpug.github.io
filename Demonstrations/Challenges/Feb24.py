# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 14:17:27 2024

@author: uqcwest5
"""

CODE = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

#%% Official solution

import string

table = CODE.maketrans(string.ascii_lowercase,
                       string.ascii_lowercase[2:] + string.ascii_lowercase[:2])

decoded = CODE.translate(table)

print(decoded)

#%% string.maketrans() method


table = CODE.maketrans("abcdefghijklmnopqrstuvwxyz", 
                       "cdefghijklmnopqrstuvwxyzab")

decoded = CODE.translate(table)

print(decoded)

#%% Dictionary method

table_a_to_x = {n: n+2 for n in range(ord("a"), ord("y"))}
table_y_to_z = {n: n-24 for n in range(ord("y"), ord("z")+1)}

decoded = CODE.translate(table_a_to_x | table_y_to_z)

print(decoded)


#%% Unicode loop
decoded = ""

for letter in CODE:
    
    new_ord = ord(letter)
    
    if letter > "x" and letter <= "z":
        new_ord -= 24
    
    elif letter >= "a":
        new_ord += 2
    
    new_letter = chr(new_ord)
    
    decoded += new_letter
    
print(decoded)


