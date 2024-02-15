import sys
import getopt

# remove first commandline arg
argumentList = sys.argv[1:]

options = "hgn"
long_options = ["help", "gpu", "normal"]  # Removed ':' from options that don't require arguments
try:

    # Parse arguments
    arguments, values = getopt.getopt(argumentList, options, long_options)


    # checking each argument
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--help"):  # Corrected case for "--help"
            print("Displaying Help")
             
        elif currentArgument in ("-g", "--gpu"):
            print("GPU Config Selected...")
             
        elif currentArgument in ("-n", "--normal"):
            print("Normal Config Selected...")
             
except getopt.error as err:
    # output error, and return with an error code
    print(str(err))
