# Brainfuck interpreter
This is a [brainfuck](https://esolangs.org/wiki/Brainfuck) language interpreter written in python 3.9.

## Features

The interpreter works in two modes:

* File - reads and interprets provided file;

* Live - reads standard input and interprets it line by line.

Sizes of cell array and cells can be edited in code.

Except for the eight basic instructions this version also features `#` for debug info:

  * **Program counter** - number of line and column in the source code.
  
  * **Array pointer** - number of currently active cell
  
  * **Value** - value stored in the active cell
  
  * **Top of the stack** - the line and column to which the `]` operation will go.
  

## Usage

Make sure [python](https://www.python.org/downloads/) is installed.

When running the interpreter first you will have to choose the mode - type in `live` or `file`.

In file mode you will be asked to provide file name of source code.

In live mode you can input bf code line by line. Input 0 to end program.
