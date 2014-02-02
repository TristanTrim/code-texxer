#####################################################################
####   Welcome to SHINYOUTPUT!!!                                 ####
####   This is the program where we take your terminal program   ####
####    and output a nice shiny string!                          ####
####                                                             ####
#####################################################################
#####################################################################
import subprocess
import sys
import select
import fcntl
import os

# the string that we will return filled with tasty program output and user input #
string = ""

# the subprocess running the program #
child = subprocess.Popen(["java","findTheAverage"],bufsize = 0, universal_newlines = True, stdout = subprocess.PIPE, stdin = subprocess.PIPE )

# stuff to stop IO blocks in child.stdout and sys.stdin ## (I stole if from http://stackoverflow.com/a/8980466/2674170)
fcntl.fcntl(child.stdout.fileno(), fcntl.F_SETFL, os.O_NONBLOCK)
fcntl.fcntl(sys.stdin.fileno(), fcntl.F_SETFL, os.O_NONBLOCK)

# this here in the unlikely event that the program has #
# finished by the time the main loop is first running  #
# because if that happened the loop would end without  #
# having added the programs output to the string!      #
progout = ""
typedbuf = "#"

### here we have the main loop, this friendly fellah is 
### going to read from the program and user, and tell
### each other what needs to be known
while True:

## stop when the program finishes and there is no more output
  if child.poll() != None and not progout:
    break

# read from 
  typed = ""

  while typedbuf:
    try:
      typedbuf = sys.stdin.read(1)
    except:
      break
    typed += typedbuf
    stringbuf  = "#"
  string += typed
  child.stdin.write(typed)

  progout = ""
  progoutbuf = "#"
  while progoutbuf:
    try:
      progoutbuf = child.stdout.read(1)
    except:
      typedbuf = "#"
      break 
    progout += progoutbuf
  if progout:
    print(progout)
  string += progout
print( string)
