import glob, os, time

filelist = []
null = None
rf_name = null
dir_or_file = input('are you translating a directory or a file? input: "file" or "dir" ')
if dir_or_file == 'file':
    rf_name = input('filename: ')
    wf_name = rf_name[:-3] + '.asm'
    static_name = rf_name[:-3]
else:
    dir_name = input('directory: ')
    wf_name = dir_name + '.asm'
    # static_name = dir_name.split("\\")[-1]
    os.chdir(dir_name)
    for file in glob.glob("*.vm"):
        filelist.append(file)

line_count = 0
global label_counter
label_counter = 0
global function_name
function_name = ''

initialize_theft = """
// Bootstrap Code
@256
D=A
@SP
M=D

(OS)

@OS$ret.0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(OS$ret.0)
"""


def parseline(instruction):
    if instruction == null:
        return null

    segment = null  # initialize local variables
    value = null

    inst_lst = instruction.split()
    pp = inst_lst[0]                # push/pop or logic
    if 1 < len(inst_lst):           # checking to see if index exists
        segment = inst_lst[1]       # memory segment
    if 2 < len(inst_lst):
        value = int(inst_lst[2])    # value
    if segment == 'local': segment = 'LCL'
    if segment == 'argument': segment = 'ARG'
    if segment == 'this': segment = 'THIS'
    if segment == 'that': segment = 'THAT'
    if segment == null:
        return pp
    else:
        return pp, segment, value


def translate_instruction(line):
    global label_counter
    global function_name
    parts = parseline(line)
    print(parts)
    # print('these are the parts')
    if parts == 'add':
        formatted_out_add = """
@SP
AM=M-1
D=M
@SP
AM=M-1
M=D+M
@SP
M=M+1
            """
        return formatted_out_add
    if parts == 'sub':
        formatted_out_sub = """
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
M=M+1
                """
        return formatted_out_sub
    if parts == 'neg':
        formatted_out_neg = """
@SP
A=M-1
M=-M
                """
        return formatted_out_neg
    if parts == 'not':
        formatted_out_not = """
@SP
A=M-1
M=!M
                """
        return formatted_out_not
    if parts == 'or':
        formatted_out_or = """
@SP
AM=M-1
D=M
@SP
A=M-1
M=D|M
                """
        return formatted_out_or
    if parts == 'and':
        formatted_out_and = """
@SP
AM=M-1
D=M
@SP
A=M-1
M=D&M
                """
        return formatted_out_and
    if parts == 'eq':
        #global label_counter               moving this to the top of the function
        formatted_out_eq = """
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@eqTrue{0}
D;JEQ
@SP
A=M-1
M=0
(eqTrue{0})
                """
        label_counter += 1
        out = formatted_out_eq.format(str(label_counter))

        return out
    if parts == 'lt':
        formatted_out_lt = """
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@ltTrue{0}
D;JLT
@SP
A=M-1
M=0
(ltTrue{0})
                """
        label_counter += 1
        out = formatted_out_lt.format(str(label_counter))

        return out
    if parts == 'gt':
        formatted_out_gt = """
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@gtTrue{0}
D;JGT
@SP
A=M-1
M=0
(gtTrue{0})
                """
        label_counter += 1
        out = formatted_out_gt.format(str(label_counter))

        return out
    if parts[0] != null and parts[0] == 'push' and parts[1] in ('LCL', 'ARG', 'THIS', 'THAT'):
        formatted_out_push = """
@{1}
D=A
@{0}
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
        """
        return formatted_out_push.format(parts[1], parts[2])
    elif parts[0] != null and parts[0] == 'push' and parts[1] == 'constant':
        formatted_out_const = """
@{1}
D=A
@SP
A=M
M=D
@SP
M=M+1
                """
        return formatted_out_const.format(parts[1], parts[2])
    if parts[0] != null and parts[0] == 'pop' and parts[1] in ('LCL', 'ARG', 'THIS', 'THAT'):
        formatted_out_pop = """
@{1}
D=A
@{0}
D=M+D
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
        """
        return formatted_out_pop.format(parts[1], parts[2])
    if parts[0] != null and parts[0] == 'pop' and parts[1] == 'static':
        formatted_out_pop_static = """
@SP
AM=M-1
D=M
@{0}.{1}
M=D
        """
        return formatted_out_pop_static.format(static_name, parts[2])
    if parts[0] != null and parts[0] == 'push' and parts[1] == 'static':
        formatted_out_pop_static = """
@{0}.{1}
D=M
@SP
A=M
M=D
@SP
M=M+1
        """
        return formatted_out_pop_static.format(static_name, parts[2])
    if parts[0] != null and parts[0] == 'push' and parts[1] == 'temp':
        formatted_out_push_temp = """
@{1}
D=A
@5
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
        """
        return formatted_out_push_temp.format(parts[1], parts[2])
    if parts[0] != null and parts[0] == 'pop' and parts[1] == 'temp':
        formatted_out_pop_temp = """
@{1}
D=A
@5
D=A+D
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
        """
        return formatted_out_pop_temp.format(parts[1], parts[2])
    if parts[0] != null and parts[0] == 'pop' and parts[1] == 'pointer':
        formatted_out_pop_pointer = """
@{1}
D=A
@3
D=A+D
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
        """
        return formatted_out_pop_pointer.format(parts[1], parts[2])
    if parts[0] != null and parts[0] == 'push' and parts[1] == 'pointer':
        formatted_out_push_pointer = """
@{1}
D=A
@3
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
        """
        return formatted_out_push_pointer.format(parts[1], parts[2])
    if parts[0] != null and parts[0] == 'function':
        # global function_name
        function_name = parts[1]
        formatted_out_function = """
({0})
        """
        local_segs = 0
        while local_segs < int(parts[2]):   #this probably won't work, if something goes wrong this is probably one of the reasons
            formatted_out_function += """          
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
            """
            local_segs += 1
        return formatted_out_function.format(parts[1])
    if parts[0] != null and parts[0] == 'label':
        formatted_out_label = """
({0}${1}) 
        """
        # global function_name
        return formatted_out_label.format(function_name, parts[1])
    if parts[0] != null and parts[0] == 'goto':
        formatted_out_goto = """
@{0}${1}
0;JMP 
            """
        # global function_name
        return formatted_out_goto.format(function_name, parts[1])
    if parts[0] != null and parts[0] == 'if-goto':
        formatted_out_ifgoto = """
@SP
AM=M-1
D=M
@{0}${1}                                                        //This might work but if it doesn't it's because a different label was requested meaning I need to store labels and reuse them instead of just going off of what was shown in the parts breakdown
D;JNE
            """
        # global function_name
        return formatted_out_ifgoto.format(function_name, parts[1])
    if parts[0] != null and parts[0] == 'call':
        # global function_name
        label_counter += 1
        ret_label = function_name + "$ret." + str(label_counter)

        formatted_out_call = """
@{0}
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL                                    // saving stack state for each of the four big segments LCL, ARG, THIS, THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@{1}
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@{2}
0;JMP
({0})
            """
        return formatted_out_call.format(ret_label, parts[2], parts[1])
    if parts[0] != null and parts == 'return':
        formatted_out_return = """ //checking
@LCL
D=M
@R13
M=D
@5
A=D-A
D=M
@R14
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13                   //restoring stack segments
AM=M-1
D=M
@THAT
M=D
@R13
AM=M-1
D=M
@THIS
M=D
@R13
AM=M-1
D=M
@ARG
M=D
@R13
AM=M-1
D=M
@LCL
M=D
@R14
A=M
0;JMP
                """
        return formatted_out_return


if rf_name:
    print("I'm doing this")
    with open(rf_name, 'r') as read_file, open(wf_name, 'w') as write_file:
        for line in read_file:
            if line.startswith("//") or line == "\n": continue
            else:
                line = line.partition('//')[0]  # split line and grab only text before the comment // my good friend Wesley Elmer had comment cleaning code laying
                line = line.rstrip()  # remove whitespace from line                                // laying around that has been revived and introduced here
                write_file.write(translate_instruction(line))
else:
    print("im doing thissssssss")
    for file in filelist:
        print("should be a few")
        print(file)
        static_name = str(file)[:-3]
        with open(file, 'r') as read_file, open(wf_name, 'a') as write_file:
            for line in read_file:
                if line.startswith("//") or line == "\n":
                    continue
                else:
                    line = line.partition('//')[
                        0]  # split line and grab only text before the comment // my good friend Wesley Elmer had comment cleaning code laying
                    line = line.rstrip()  # remove whitespace from line                                // laying around that has been revived and introduced here
                    write_file.write(translate_instruction(line))


with open(wf_name, 'r+') as fp:
    lines = fp.readlines()     # lines is list of line, each element '...\n'
    lines.insert(0, initialize_theft)  # you can use any index if you know the line index
    fp.seek(0)                 # file pointer locates at the beginning to write the whole file again
    fp.writelines(lines)







