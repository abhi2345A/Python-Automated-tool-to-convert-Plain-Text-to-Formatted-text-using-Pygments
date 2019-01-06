from plain_to_formatted_ import plain_text_to_formatted_text
import webbrowser, os

def main(args):

    args = args
    if args.demo:

        inpfil = args.demo
        rf = open(inpfil, 'r')

        with rf:
            demo_code = rf.read()

        outfil = args.file_name
        obj = plain_text_to_formatted_text(inpfil, outfil + '.html')
        code = obj.file_()
        if args.line_numbers:
            line_nums = args.line_numbers.lower()
        else:
            line_nums = 1
        var = obj.line_numbers(flag=line_nums)
        if args.style_name:
            styl = obj.select_style(styl=args.style_name.lower())
        else:
            styl = obj.select_style()
        obj._plain_text_to_formatted_text__conversion(code, var, styl) #Private method call will require class name
        print("Conversion done successfully. Opening it now!")
        webbrowser.get().open('file://' + os.path.realpath('demo/'+ outfil + '.html'))
        exit(0)

    else:
        print('Default file temp.py is being used. ')
        inpfil = 'temp.py' #default input file
        outfil = args.file_name
        obj = plain_text_to_formatted_text(inpfil, outfil + '.html')
        code = obj.file_()
        if args.line_numbers:
            line_nums = args.line_numbers.lower()
        else:
            line_nums = 1
        var = obj.line_numbers(flag=line_nums)
        if args.style_name:
            styl = obj.select_style(styl=args.style_name.lower())
        else:
            styl = obj.select_style()
        obj._plain_text_to_formatted_text__conversion(code, var, styl) #Private method call will require class name
        print("Conversion done successfully. Opening it now!")
        webbrowser.get().open('file://' + os.path.realpath('demo/'+ outfil + '.html'))
        exit(0)

if __name__ == '__main__':
    main()
