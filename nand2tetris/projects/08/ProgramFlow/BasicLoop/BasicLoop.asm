
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
                
@0
D=A
@LCL
D=M+D
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
        
($LOOP_START) 
        
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
        
@0
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
        
@SP
AM=M-1
D=M
@SP
AM=M-1
M=D+M
@SP
M=M+1
            
@0
D=A
@LCL
D=M+D
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
        
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
        
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
                
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
M=M+1
                
@0
D=A
@ARG
D=M+D
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
        
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
        
@SP
AM=M-1
D=M
@$LOOP_START                                                        //This might work but if it doesn't it's because a different label was requested meaning I need to store labels and reuse them instead of just going off of what was shown in the parts breakdown
D;JNE
            
@0
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
        