
Hoy!

This is my code texxer. That is to say, it turns your code into a nice .tex document.

Right now it only supports java code, And it only works on linux. I like other languages better than java, but java is the only one I make stupid doc's for teachers in. As for other os's, I wouldn't mind people extending this for them, but it would prolly be easier to write from scratch.

You need a few things: pyglist and verbments and pdflatex. Python. Ummm, I think thats everything, but if you run into trouble, do let me know, because something could have slipped my mind.

To use:

Just switch out the variables at the begining of CodeTexxer.py to match your name and project. Then run:

    python CodeTexxer.py

This will create a .tex file, and search for any .class files. Then add the contents of .java files of the same name to the file. And run all the .class files, add the output to the file.

Then you can run:

    pdflatex -shell-escape

This will create your nice shiny .pdf file.

Fin.


