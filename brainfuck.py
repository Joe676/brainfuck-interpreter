class BFArray:
    def __init__(self, n):
        self.arr = [0 for _ in range(n)]
        self.pointer = 0
        self.cell_width = 256
    
    def right(self):
        self.pointer += 1
        self.pointer %= len(self.arr)
    
    def left(self):
        self.pointer -= 1
        self.pointer %= len(self.arr)
    
    def inc(self):
        self.arr[self.pointer] += 1
        self.arr[self.pointer] %= self.cell_width

    def dec(self):
        self.arr[self.pointer] -= 1
        self.arr[self.pointer] %= self.cell_width
    
    def get(self):
        return self.arr[self.pointer]
    
    def put(self, x):
        self.arr[self.pointer] = x


class BFInterpreter:
    def __init__(self, n):
        self.arr = BFArray(n)
        self.lines = []
        self.program_counter = (0, 0)

        self.loops = []
        self.open_brackets = 0
        self.looped = False

        self.input_buffer = []
        
        self.op_codes = {
            '+':self.arr.inc,
            '-':self.arr.dec,
            '<':self.arr.left,
            '>':self.arr.right,
            '.':self.output,
            ',':self.input,
            '[':self.start_loop,
            ']':self.loop,
            '#':self.debug
        }
    
    def debug(self):
        print('Program counter:', self.program_counter)
        print('Array pointer:', self.arr.pointer)
        print('Value at {}:'.format(self.arr.pointer), self.arr.get())
        print('Top of the stack:', self.loops[-1] if len(self.loops)>0 else '-')

    def open_file(self, file_name):
        with open(file_name, 'r') as file:
            self.lines.extend(file.readlines())
    
    def read_line(self):
        l = input("BF > ")
        self.lines.append(l)
        if l[0] == '0':
            return False
        else:
            return True
    
    def step(self):
        #extract program counter
        i = self.program_counter[0]
        j = self.program_counter[1]

        #if looping forward
        if self.open_brackets > 0:
            #'[' goes deeper
            if self.lines[i][j] == '[':
                self.open_brackets += 1
            #']' goes up 
            elif self.lines[i][j] == ']':
                self.open_brackets -= 1
        if self.open_brackets == 0:
            if self.lines[i][j] in self.op_codes.keys():
                self.op_codes[self.lines[i][j]]()
        if not self.looped:
            j += 1
            if j == len(self.lines[i]):
                j = 0
                i += 1
            self.program_counter = (i, j)
        else:
            self.looped = False
        return (self.program_counter[0] < len(self.lines))
        
    def output(self):
        print(chr(self.arr.get()), end = '')
    
    def input(self):
        if len(self.input_buffer) == 0:
            self.input_buffer = list(str(input()))
        c = self.input_buffer.pop(0)
        self.arr.put(ord(c))

    def start_loop(self):
        self.loops.append(self.program_counter)
        if self.arr.get() == 0:
            self.open_brackets = 1
    
    def loop(self):
        pc = self.loops.pop()
        if self.arr.get() != 0:
            self.program_counter = pc
            self.looped = True


def main():
    bf = BFInterpreter(1000)
    menu = str(input("Choose mode [live|file]: ")).casefold()
    while menu != 'live' and menu != 'file':
        menu = str(input("Choose mode [live|file]: "))
    if menu == 'file':
        file_name = input('File name: ')
        bf.open_file(file_name)
        while(bf.step()):
            pass
    else:
        print("--- Live mode ---")
        print("Type a line of code, enter to run, # for debug, 0 to end")
        while True:
            print()
            if not bf.read_line():
                return
            while bf.step():
                pass

if __name__ == '__main__':
    main()

