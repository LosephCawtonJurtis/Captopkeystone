
(SimpleFunction.test)
                  
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
                      
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
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
        
@1
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
            
@SP
A=M-1
M=!M
                
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
@SP
AM=M-1
M=D+M
@SP
M=M+1
            
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
        
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
M=M+1
                 //checking
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
                