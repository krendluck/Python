# -*- coding: utf-8 -*-
import re

def deal(str):
    reg = r'n\.|adj\.|adv\.|prep\.|v\.|vt\.|vi\.'       
    name = re.findall(reg,str)
    result = re.split(reg,str)
    while '' in result:
        result.remove('')
    output = ''
    for i in range(len(name)):
        output += name[i] + result[i] + '\n'
    return output