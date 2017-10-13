# -*- coding: utf-8 -*-
import re

#概　要：１行の文字数が６００字以上で、その４割以上に数字が含まれていれば難読化コードと判定する
def check_num_in_line(text):
    line_len = len(line)
    if line_len > 600:
        num_in_line = len(filter(lambda x: x.isdigit(), line))
        if num_in_line > (line_len*0.4):
            return True
    return False


#概　要：上の関数を呼び出し、文字列中に難読化コードが存在するかを判別する
def find_obfuscation(text):
    if text is None:
        return -1
    text_list = text.split("\n")
    return len(filter(lambda x : check_num_in_line(x), text_list))
