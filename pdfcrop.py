#!/usr/bin/env python3

"""
   program name: pdfcrop
   description: Script that allows to crop a PDF removing or keeping pages
   created by: Benigno Calvo
   creation date: 05-08-2016
   Modification History:
   06-08-2016: added ability to specify pages to delete instead of pages to keep.
"""

import sys
# from string import split
from optparse import OptionParser
from PyPDF2 import PdfFileReader, PdfFileWriter

def parse_input():
    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)

    parser.add_option("-f","--file",
                      dest="filename",
                      help="input pdf filename and path",
                      default="CVen Benigno Calvo 2016.pdf",
                      metavar="file")

    parser.add_option("-k", "--keep",
                      dest="keep",
                      help="input list of pages to keep, separated by commas 1,3,42",
                    #   default="1,2",
                      type="string")

    parser.add_option("-d", "--delete",
                      dest="delete",
                      help="input list of pages to delete, separated by commas 1,3,42",
                      default="3,4",
                      type="string")

    parser.add_option("-o", "--output",
                      dest="output",
                      help="output pdf filename including path",
                      default="cropped.pdf")

    (options, args) = parser.parse_args()
    # if options.filename is None:
    #     options.filename = input('enter input pdf filename:')

    # if options.keep is None:
    #     options.keep = input('enter page numbers to keep ie. 2,23,42:')

    return (options, args)

def parse_pages(str_pages):
    """takes a string from the options input and turns
    it into an array for further use"""
    tmp_pages = str_pages.split(",")
    pages = list()
    for i in tmp_pages:
        pages.append(int(i)-1)
    return pages

def main():
    (options, args) = parse_input()
    pages_to_keep = list()
    pages_to_delete = list()
    if options.keep:
        pages_to_keep = parse_pages(options.keep)
    if options.delete:
        pages_to_delete = parse_pages(options.delete)
    output = PdfFileWriter()
    infile = PdfFileReader(options.filename)
    for i in range(infile.getNumPages()):
        added = False
        if i in pages_to_keep:
            page = infile.getPage(i)
            added = True
        if i not in pages_to_delete and not added:
            page = infile.getPage(i)
            added = True
        if added:
            output.addPage(page)
    with open(options.output, 'wb') as pdffile:
        output.write(pdffile)
        print("Created cropped file:", options.output)

if __name__ == '__main__':
    main()
