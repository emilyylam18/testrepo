# Functions do three things:
# they name pieces of code the way variables name 
# strings and numbers
# they take arguments the way the script takes argv
# using 1 and 2, they let you make your own mini-script
# or tiny command

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok that *args was pointless, just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument  
def print_one(arg1):
    print "arg1: %r" % arg1

#this one taks no arguments
def print_none():
    print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

#this defines a printing command so you can type print() without
# the usual print command
# function = mini script