from main import main
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--demo", help="Enter input file name to be formatted. Else default file will be used.")
parser.add_argument("file_name", help="Provide the output(html) file name.")
parser.add_argument("--line_numbers", help="Enter 1 to provide line numbers. Enter anything otherwise. Default : True (1)")
parser.add_argument("--style_name", help="Default style : colorful.\nOther options: ['autumn', 'borland', 'bw', 'colorful', 'default', 'emacs', 'fruity', 'manni', 'monokai', 'murphy', 'native', 'pastie', 'rrt', 'tango', 'trac', 'vim', 'friendly', 'perldoc']")

args = parser.parse_args()

if __name__ == "__main__":
    main(args)
else:
    pass
