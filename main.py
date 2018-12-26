from plain_to_formatted_ import plain_text_to_formatted_text

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
