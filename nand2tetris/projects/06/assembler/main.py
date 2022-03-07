checkAT = '@'
checkEQ = '='
checkSMI = ';'
null = None
rf_name = input('filename: ')
wf_name = rf_name[:-4]+'.hack'

Dest_Dict = {'M': '001', 'D': '010', 'MD': '011', 'A': '100', 'AM': '101',
             'AD': '110', 'AMD': '111'}

Jmp_Dict = {'JGT': '001', 'JEQ': '010', 'JGE': '011', 'JLT': '100', 'JNE': '101',
            'JLE': '110', 'JMP': '111'}

Comp_Dict = {'0': '0101010', '1': '0111111', '-1': '0111010', 'D': '0001100',
             'A': '0110000', '!D': '0001101', '!A': '0110001', '-D': '0001111',
             '-A': '0110011', 'D+1': '0011111', 'A+1': '0110111',
             'D-1': '0001110', 'A-1': '0110010', 'D+A': '0000010',
             'D-A': '0010011', 'A-D': '0000111', 'D&A': '0000000',
             'D|A': '0010101', 'M': '1110000', '!M': '1110001', '-M': '1110011',
             'M+1': '1110111', 'M-1': '1110010', 'D+M': '1000010',
             'D-M': '1010011', 'M-D': '1000111', 'D&M': '1000000',
             'D|M': '1010101'}


def parseline(instruction):
    if instruction == null:
        return null
    addr = null
    dest = null
    comp = null
    jmp = '000'
    if checkAT in instruction:
        checkA = instruction.split('@')
        addr = checkA[1]
        #print(addr)

    if checkEQ in instruction:
        insDest = instruction.split('=')
        dest = insDest[0]
        #print(dest)
        if checkSMI not in instruction:
            comp = insDest[1]
            #print(comp)

    if checkSMI in instruction:
        insJmp = instruction.split(';')
        jmp = insJmp[1]
        #print(jmp)
        if checkEQ in instruction:
            insComp = insJmp[0].split('=')
            comp = insComp[1]
            #print(comp)
        else:
            comp = insJmp[0]
            #print(comp)
    return addr, comp, dest, jmp


def fix_AT(currentATvalue):
    length = len(currentATvalue)
    amount_to_keep = 16-length
    finalAT = '0000000000000000'
    return finalAT[:amount_to_keep]+currentATvalue


def translate_instruction(line):
    parts = parseline(line)
    if parts[0] != null:
        return fix_AT(str(bin(int(parts[0])).replace('0b', '')))
    else:
        finalComp = loop_through_dict(str(parts[1]).strip(), Comp_Dict)
        finalDest = loop_through_dict(str(parts[2]).strip(), Dest_Dict)
        if finalDest == null: finalDest = '000'
        finalJmp =  loop_through_dict(str(parts[3]).strip(), Jmp_Dict)
        if finalJmp == null: finalJmp = '000'

        return '111'+str(finalComp)+str(finalDest)+str(finalJmp)


def loop_through_dict(critter, dict):
    for key in dict:
        if str(key) == critter:
            return dict[key]


with open(rf_name, 'r') as read_file, open(wf_name, 'w') as write_file:
    for line in read_file:
        if line.startswith("/") or line == "\n": line = read_file.__next__()
        line = line.partition('//')[0]  # split line and grab only text before the comment // my good friend Wesley Elmer had comment cleaning code laying
        line = line.rstrip()  # remove whitespace from line                                // laying around that has been revived and introduced here
        #line += "\n"                                                                       //
        write_file.write(translate_instruction(line)+'\n')