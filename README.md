# pdfcrop

Python script to crop pages out of pdf documents.

## Usage

pdfcrop.py `[options]

The script uses the following options when called:

- -h --help show this help message and exit.
- -f --file Input pdf filename including path if necessary.
- -k --keep List of pages to keep, separate them with commas, do not put in spaces: ie 1,2,12
- -d --delete List of pages to delete, separate them with commas, do not put in spaces: ie 1,2,12
- -o --output Filename including path of the cropped pdf. Default value: _cropped.pdf_

Normally you will not want to use both methods (delete and keep) at the same time

### Example of usage:

This will keep only the first two pages and delete the rest:
> pdfcrop.py -f NameofInputFile.pdf -k 1,2 -o NameofOutputFile.pdf

This will delete pages 3 and 4 and keep the rest:
> pdfcrop.py -f NameofInputFile.pdf -d 3,4 -o NameofOutputFile.pdf
