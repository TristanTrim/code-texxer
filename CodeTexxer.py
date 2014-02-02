

import re
import getProgramIO
import os
import shutil
import subprocess

initialEnvi = os.getcwd()

## make regular expressions or whatever
getClassName = re.compile('(.+?)(?=\.class)')

########################################
#  Path is where you keep you projects #

#  Folder is the folder to convert to  #
#     pretty .tex document.            #

#  Name should be self explanitory.    #
path = "/home/trist/studies/javaShiz/"
folder = "ASS1"
name = "TristanTrim"

########################################

"""Make the file, naming it after the author and folder"""
f = open(name+"_"+folder+'.tex','w')

"""Put the intro into the tex file"""
intro = open('texintroPt1.tex', 'r')
f.write(intro.read())
intro.close()

f.write(name+"}\n\\title{")
f.write(folder)

intro = open('texintroPt2.tex', 'r')
f.write(intro.read())
intro.close()


"""go through the folder searching for .class files"""
for root, dirs, files in os.walk(path+folder):

    files.sort()### I put the files in aphibetical order, otherwise they're in ??? order.

    os.chdir(root)
    for fl in files:
  #  If it is .class, we add the .java to the tex doc
        if getClassName.match(fl):
            flClass = (getClassName.match(fl).group())

            f.write('\n\n\n\\section*{'+flClass+' }\n\n')

            f.write('\\textbf{Program:}\n\\begin{pyglist}[ language=java]\n')


            CodeContents = open(flClass+'.java','r') 

            f.write(CodeContents.read())

            CodeContents.close()

            f.write('\\end{pyglist}\n')


            """ Getting output if applicable, from .class file, and copy the output to the tex doc """
            """  \/    \/    \/    \/     \/    \/    \/    \/   \/   \/    """

            more_examples = 'y'
            any_examples=True


        ## ask if this file needs output.
  ## lator I may add auto no for classes with no main method.

            print("\n\nFile:\t"+flClass+"\nAdd code output? (y or n): ")

            ## get user input
            while(True):
                try:
                    more_examples = input()
                    break
                except:
                    'meh'


            if(more_examples == 'y'):
              ##  Code output title (output is currently whatever is shown in the terminal
                      ##    while running the program. I'd like to add support for screenshots)
                f.write('\n\\fvset{frame=none}\n\\textbf{Output:}\n\\begin{verbatim}')#tex code..
                any_examples=True


    ##  Code output:

            codeTestNum=1
            while(more_examples == 'y'):

                f.write("\n\n\n\tExample "+str(codeTestNum)+":\n\n")
                f.write(getProgramIO.getProgramIO(flClass))

                codeTestNum+=1

                print("\nAdd more code output? (y or n): ")
                ## get user input
                while(True):
                    try:
                        more_examples = input()
                        break
                    except:
                        'meh'

            if(any_examples):
              ##  End verbatim of code output
                f.write('\\end{verbatim}') 


            print(flClass+" Added to Tex Doc!\n")
    print('#########################################')

f.write('\n\n\n\\end{document}\n\n')

f.close()## and we are done writing our .tex!

## make .tex file into .pdf
subprocess.Popen(["pdflatex","-shell-escape",'Report.tex'],bufsize = 0, universal_newlines = True, stdout = subprocess.PIPE, stdin = subprocess.PIPE )

os.environ = root

