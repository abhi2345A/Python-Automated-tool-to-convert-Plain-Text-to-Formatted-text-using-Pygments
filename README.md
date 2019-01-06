# Python Automated tool to convert Plain Text-to Formatted text using Pygments

Tool written in python to convert the plain python code text to the formatted text in many styles like -
autumn','borland','bw','colorful','default','emacs','friendly','fruity','manni','monokai','murphy','native','pastie','perldoc','rrt',
'tango','trac','vim'

### Working

* Open a terminal window and paste this now:
```
git clone https://github.com/apoorvpatne10/Python-Automated-tool-to-convert-Plain-Text-to-Formatted-text-using-Pygments
```


* Once done, cd into the repository
```
cd Python-Automated-tool-to-convert-Plain-Text-to-Formatted-text-using-Pygments/
```

* Run the __ main __ .py file with '-h or --help' argument

```
apoorv@apoorv:~ python __main__.py -h

usage: __main__.py [-h] [--demo DEMO] [--line_numbers LINE_NUMBERS]
                   [--style_name STYLE_NAME]
                   file_name

positional arguments:
  file_name             Provide the output(html) file name.

optional arguments:
  -h, --help            show this help message and exit
  --demo DEMO           Enter input file name to be formatted. Else default
                        file will be used.
  --line_numbers LINE_NUMBERS
                        Enter 1 to provide line numbers. Enter anything
                        otherwise. Default : True (1)
  --style_name STYLE_NAME
                        Default style : colorful. Other options: ['autumn',
                        'borland', 'bw', 'colorful', 'default', 'emacs',
                        'fruity', 'manni', 'monokai', 'murphy', 'native',
                        'pastie', 'rrt', 'tango', 'trac', 'vim', 'friendly',
                        'perldoc']

```

* Output file name is mandatory hence, you must provide a name for output formatted html file.

```
apoorv@apoorv:~ python __main__.py my_file5

Formatted File is generated as- my_file5.html
Conversion done successfully. Opening it now!

```

This will take the name and assign it to output file name parameter. All the optional arguments will go with default values. The result might look something like this :

![output](https://i.imgur.com/ss0z9gq.png)


* Try other options

```
apoorv@apoorv:~ python __main__.py my_file5 --line_numbers false --style_name vim

Formatted File is generated as- my_file5.html
Conversion done successfully. Opening it now!

```

The result will look like this:

![output2](https://i.imgur.com/YaPImoG.png)

