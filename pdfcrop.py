#!/usr/bin/env python3

from optparse import OptionParser

def parse_input():
    usage = "Usage: %prog [options]"
    parser = OptionParser(usage=usage)

    parser.add_option("-f","--file",dest="filename", help = "Input pdf filename and path",
    metavar = "FILE")

    parser.add_option("-k","--keep",dest="keep", help = "Input list of pages to keep, in format [1,3,42]",
    type= "string")

    parser.add_option("-o","--output",dest="output",help="Output pdf filename including path",
    default = "cropped.pdf")

    (options, args) = parser.parse_args()
    return (options, args)
    

def main():
    (options, args) = parse_input()
    print(options, args)

if __name__ == '__main__':
    main()