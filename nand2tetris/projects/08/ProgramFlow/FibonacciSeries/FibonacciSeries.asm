
@1
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
        
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
                
@0
D=A
@THAT
D=M+D
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
        
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
                
@1
D=A
@THAT
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
        
@2
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
        
($MAIN_LOOP_START) 
        
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
@$COMPUTE_ELEMENT                                                        //This might work but if it doesn't it's because a different label was requested meaning I need to store labels and reuse them instead of just going off of what was shown in the parts breakdown
D;JNE
            
@$END_PROGRAM
0;JMP 
            
($COMPUTE_ELEMENT) 
        
@0
D=A
@THAT
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
        
@1
D=A
@THAT
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
            
@2
D=A
@THAT
D=M+D
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
        
@1
D=A
@3
A=A+D
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
M=D+M
@SP
M=M+1
            
@1
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
        
@$MAIN_LOOP_START
0;JMP 
            
($END_PROGRAM) 
        