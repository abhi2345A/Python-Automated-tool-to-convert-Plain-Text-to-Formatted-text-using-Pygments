from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
import sys

class plain_text_to_formatted_text:
    def __init__(self ,inpfil ,outfil):
        self.__inpfil = inpfil  # inpfil is a private data member ( __ before name specifies private)
        self.__outfil = outfil  # outfil is a private data member ( __ before name specifies private)

    def file_(self):

        try:
            rf = open(self.__inpfil ,'r')
        except IOError:
            print(f"Couldn't read file {self.__inpfil}")
            sys.exit()

        with rf:
            code = rf.read()

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

    def __conversion(self, code, var, styl):  # This is a Private Method ( __ before method name)
        lexer = get_lexer_by_name("python", stripall=True)
        formatter = HtmlFormatter(linenos=var, cssclass='source', style=styl)
        formatter.noclasses = True
        with open("demo/" + self.__outfil, "w") as f:
            f.write("<i> ------- Formatted the code successfully! ------- </i><br>")
            result = highlight(code, lexer, formatter, f)
        print(f"\nFormatted File is generated as- {self.__outfil}")

