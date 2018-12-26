from plain_to_formatted_ import plain_text_to_formatted_text
import webbrowser, os

def main():
    ch = int(input('Enter your choice\n1. Demo (work with default file)\n2. Format your own file\n3. Exit\n:'))

    if ch == 1:
        inpfil = 'temp.py' #default input file
        print('Default file temp.py is being used. ')
        rf = open(inpfil, 'r')

        with rf:
            demo_code = rf.read()

        outfil = input('\nEnter the Output file name (Previous Data will be overwritten!) : ')
        obj = plain_text_to_formatted_text(inpfil, outfil + '.html')
        code = obj.file_()
        var = obj.line_numbers()
        styl = obj.select_style()
        obj._plain_text_to_formatted_text__conversion(code, var, styl) #Private method call will require class name
        print("Conversion done successfully. Opening it now!")
        webbrowser.get().open('file://' + os.path.realpath('demo/'+ outfil + '.html'))

    elif ch==2:
        inpfil = input("Enter python file's name to be formatted : ")
        outfil = input('Enter the Output file name (Previous Data will be overwritten!) : ')
        obj = plain_text_to_formatted_text(inpfil, outfil + '.html')
        code = obj.file_()
        var = obj.line_numbers()
        styl = obj.select_style()
        obj._plain_text_to_formatted_text__conversion(code, var, styl) #Private method call will require class name
        print("Conversion done successfully. Opening it now!")
        webbrowser.get().open('file://' + os.path.realpath('demo/'+ outfil + '.html'))

    else:
        exit(0)
