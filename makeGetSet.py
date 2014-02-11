
clss = "Lallet"
atts = [['int', 'totalValue']]





fl = open("carrots.py",'w')

fl.write("\n\npublic class "+clss+"\n{")

fl.write("\n\n\t//Attributes!\n")
##Make atts
for var in atts:
  fl.write("\tprivate "+var[0]+" "+var[1])
  fl.write(";\n")

##Constructors
fl.write("\n\n\tpublic "+clss+"()"
    +"\n\t{}")
fl.write("\n\n\tpublic "+clss+"(")
for var in atts:
  fl.write(var[0]+" "+var[1]+", ")
fl.write(")\n\t{")
for var in atts:
  fl.write("\n\t\tthis."+var[1])
  fl.write(" = "+var[1]+";")
fl.write("\n\t}\n\n")



for var in atts:

 # Title
  fl.write("//"+var[1]+"'s Get and Set Methods:")
  """ Get """
  fl.write("\n\tpublic "+var[0]+" get"+var[1]+" ()\n\t{")
  fl.write("\n\t\treturn this."+var[1]+";\n\t}")
  """ Set """
  fl.write("\n\tpublic void set"+var[1]+" ("+var[0])
  fl.write(" "+var[1]+")\n\t{\n\t\tthis."+var[1])
  fl.write(" = "+var[1]+";\n\t}")
  fl.write("\n\n")


fl.write("\n\n}\n\n")

fl.close()


