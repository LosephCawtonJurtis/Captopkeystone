# Reads input file and generates list of tokens found within
import glob
import os

null = None
keyword = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void',
           'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']
symbol = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '<', '>', '=', '~']
integer_constant = null
string_constant = ''
identifier = ''
token_types = ['keyword', 'symbol', 'integerConstant', 'stringConstant', 'identifier']

filelist = []
rf_name = null
dir_or_file = input('are you translating a directory or a file? input: "file" or "dir" ')
if dir_or_file == 'file':
    rf_name = input('filename: ')
    wf_name = rf_name[:-4] + 'T.xml'
    static_name = rf_name[:-4]
else:
    dir_name = input('directory: ')
    wf_name = dir_name + 'tk'
    # static_name = dir_name.split("\\")[-1]
    os.chdir(dir_name)
    for file in glob.glob("*.jack"):
        filelist.append(file)


def sort(block):
    """identifies type belonging to found block of text"""
    if block in keyword:
        key_type = 0
    elif block in symbol:
        key_type = 1
    elif block.isdigit():
        key_type = 2
    elif block.startswith('"') and block.endswith('"'):
        block = block[1:-1]
        key_type = 3
    elif type(block) == str:
        key_type = 4
    out = '<{0}> {1} </{0}>' # debug add spaces after fixy
    return out.format(token_types[key_type], block)


is_recording_stringConst = False

with open(rf_name, 'r') as file, open(wf_name, 'a') as write_file:
    for line in file:
        if line.startswith("//") or line == "\n" or line.startswith("/**"):
            continue
        else:
            line = line.partition('//')[0]  # split line and grab only text before the comment // my good friend Wesley Elmer had comment cleaning code laying
            line = line.rstrip()  # remove whitespace from line                                // laying around that has been revived and introduced here
            output = ''
            for char in line:
                if char == '"':  # records data until finding another "
                    string_constant += char
                    # print(char)
                    if is_recording_stringConst:  # checks if already recording string variable when quote was found, if so disable isrecordstringcons and output
                        if string_constant != '':
                            write_file.write(sort(string_constant)+'\n')
                            string_constant = ''
                    is_recording_stringConst = not is_recording_stringConst
                    continue
                if is_recording_stringConst:
                    string_constant += char
                    continue
                if char in symbol:
                    if output != '': write_file.write(sort(output)+'\n')
                    output = char
                    if output != '': write_file.write(sort(output)+'\n')
                    output = ''
                    continue
                if char.isspace():
                    if output != '': write_file.write(sort(output)+'\n')
                    output = ''  # restets outpued
                else:
                    output += char






