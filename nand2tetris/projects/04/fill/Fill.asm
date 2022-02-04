// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

@SCREEN
D=A
@address
M=D
@i
M=0
@8000
D=A
@n
M=D

(UPDATE)
@KBD
D=M
@SETUP
D;JNE
@i
D=M
@n
D=M-D
@RESET
D;JEQ


@address
D=M
@i
A=M+D
M=0
@i
M=M+1


@UPDATE
0;JMP

(BLACKLOOP)
@KBD
D=M
@RESET
D;JEQ
@address
D=M
@i
A=M+D
M=-1
@i
M=M+1
D=M
@n
D=M-D
@BLACKLOOP
D;JGT

(SETUP)
@i
M=0
@BLACKLOOP
0;JMP

(RESET)
@i
M=0
@UPDATE
0;JMP
