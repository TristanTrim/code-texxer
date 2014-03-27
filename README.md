
Hoy!

This is my code texxer. That is to say, it turns your code into a nice .tex document.

Right now it only supports java code, And it only works on linux. I like other languages better than java, but java is the only one I make stupid doc's for teachers in. As for other os's, I wouldn't mind people extending this for them, but it would prolly be easier to write from scratch.

You need a few things: pyglist and verbments and pdflatex. And Python. Ummm, I think thats everything, but if you run into trouble, do let me know, because something could have slipped my mind.


Generating a PDF:

Just switch out the variables at the begining of CodeTexxer.py to match your name and project. Then run:

    python CodeTexxer.py

This will create a .tex file, and search for any .class files. Then add the contents of .java files of the same name to the .tex file. And run all the .class files, add the output to the .tex file.

It expects to be run on a filesystem with a file.java for every file.class in the same folder.

Then you can run:

    pdflatex -shell-escape

This will create your nice shiny .pdf file.


Make gets and sets:

I use this for generating particularly booring java classes which have a lot of accessors and mutators. I thought I'd include it here, but do intend to write something better in vimscript if I keep using java long enough... unlikely.


...

PS: goo.txt is there for no reason. It serves no perpose. I generated it while experimenting with output to files. I've grown strangely attatched to it.


