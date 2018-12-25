from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
import sys

class plain_text_to_formatted_text:
    def __init__(self,inpfil,outfil):
        self.__inpfil=inpfil    #inpfil is a private data member ( __ before name specifies private)
        self.__outfil=outfil    #outfil is a private data member ( __ before name specifies private)

    def file_(self):
        
        try:
            rf = open(self.__inpfil,'r')
        except IOError:
            print(f"Couldn't read file {self.__inpfil}")
            sys.exit()

        with rf:
            code = rf.read()
        rf.close()
        return code

    def line_numbers(self):
        flag = input('\nPress\n->1 to insert line Numbers\n->Any other key for not : ')
        if flag == '1':
            return True
        else:
            return False


    def select_style(self):

        style_list= ['autumn', 'borland', 'bw', 'colorful', 'default', 'emacs',
                    'fruity', 'manni', 'monokai', 'murphy', 'native', 'pastie',
                     'rrt', 'tango', 'trac', 'vim' ,'friendly', 'perldoc']
        
        while True:
            styl = input(f"\nSpecify a style from this list :\n{style_list}\n")
            if styl in style_list:
                return styl
            else:
                print('Please specify style from the given list only')


    def __conversion(self,code,var,styl):       # This is a Private Method ( __ before method name)
        lexer = get_lexer_by_name("python", stripall=True)
        formatter = HtmlFormatter(linenos = var, cssclass = 'source', style=styl)
        formatter.noclasses = True
        with open("demo/"+self.__outfil, "w") as f:
            result = highlight(code, lexer, formatter, f)
        print(f"\nFormatted File is generated as- {self.__outfil}")


def main():
    ch = int(input('1.Demo(with default file)\n2.Convert\n3.Exit\n:'))
    if ch==1:
        inpfil='temp.py' #default input file
        print('default file temp.py with content:')
        rf = open(inpfil, 'r')
        with rf:
            demo_code=rf.read()
        print(demo_code)
        outfil = input('\nEnter the Output file name(!! Previous Data will be overwritten !!):')
        obj = plain_text_to_formatted_text(inpfil, outfil+'.html')
        Code = obj.file_()
        Var = obj.line_numbers()
        Styl = obj.select_style()
        obj._plain_text_to_formatted_text__conversion(Code, Var, Styl) #Private method call will require class name

    elif ch==2:
        inpfil = input('Enter the Input file name:')
        outfil = input('Enter the Output file name(!! Previous Data will be overwritten !!):')
        obj = plain_text_to_formatted_text(inpfil,outfil+'.html')
        Code = obj.file_()
        Var = obj.line_numbers()
        Styl = obj.select_style()
        obj._plain_text_to_formatted_text__conversion(Code,Var,Styl) #Private method call will require class name

    else:
        exit(0)
