#MAEC -> OVAL Translator
#v0.94 BETA
#Generates valid OVAL 5.7 XML output from MAEC v4.1 XML
#Supports Windows files and registry keys
import maec_to_oval_processor as maec2oval
import sys
    
#Print the usage text    
def usage():
    print USAGE_TEXT
    sys.exit(1)
    
USAGE_TEXT = """
MAEC --> OVAL XML Converter Utility
v0.94 BETA // Compatible with MAEC v4.1/CybOX v2.1 and OVAL 5.7

Usage: python maec_to_oval.py <flags> -i <maec xml file> -o <oval xml file>

Available Flags:
    -s: Statistics output mode. List out the Actions that were converted and skipped during the conversion
    -v: Verbose output mode. Lists any skipped observable items and also prints traceback for errors.
"""

def main():
    infilename = ''
    outfilename = ''
    verbose_mode = False
    stat_mode = False
    #Get the command-line arguments
    args = sys.argv[1:]
    
    if len(args) < 4:
        usage()
        sys.exit(1)
        
    for i in range(0,len(args)):
        if args[i] == '-i':
            infilename = args[i+1]
        elif args[i] == '-o':
            outfilename = args[i+1]
        elif args[i] == '-v':
            verbose_mode = True
        elif args[i] == '-s':
            stat_mode = True

    processor = maec2oval.maec_to_oval_processor(infilename, outfilename, verbose_mode, stat_mode)
    #Parse the input MAEC and generate the output OVAL
    processor.generate_oval()
        
if __name__ == "__main__":
    main()    