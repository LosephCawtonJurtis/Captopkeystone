
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

(Main.fibonacci)
        
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
A=M-1
D=M-D
M=-1
@ltTrue1
D;JLT
@SP
A=M-1
M=0
(ltTrue1)
                
@SP
AM=M-1
D=M
@Main.fibonacci$IF_TRUE                                                        //This might work but if it doesn't it's because a different label was requested meaning I need to store labels and reuse them instead of just going off of what was shown in the parts breakdown
D;JNE
            
@Main.fibonacci$IF_FALSE
0;JMP 
            
(Main.fibonacci$IF_TRUE) 
        
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
                
(Main.fibonacci$IF_FALSE) 
        
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
                
@Main.fibonacci$ret.2
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
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.2)
            
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
                
@Main.fibonacci$ret.3
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
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.3)
            
@SP
AM=M-1
D=M
@SP
AM=M-1
M=D+M
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
                
(Sys.init)
        
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
                
@Sys.init$ret.4
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
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Sys.init$ret.4)
            
(Sys.init$WHILE) 
        
@Sys.init$WHILE
0;JMP 
            