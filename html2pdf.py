#! /usr/bin/env python3

import pdfkit
import sys
import os
from optparse import OptionParser

class html2pdf(object):
    def __init__(self):
        super(html2pdf).__init__()

    def make_pdf_by_url(self, url, out, options):
        if out==None:
            base_name = url
            replaced = {':': '-',
                        '/': '_'}
            for key, value in replaced.items():
                base_name = base_name.replace(key, value)
            out = base_name+'.pdf'
        pdfkit.from_url(url, out, options=options)

    def make_pdf_by_file(self, html_file, out, options):
        if out==None:
            base_name = os.path.splitext(html_file)[0]
            out = base_name+'.pdf'
        pdfkit.from_file(html_file, out, options=options)


if __name__=='__main__':
    parser = OptionParser(usage="%prog [-f FILE] [-u URL|-o PDF]",
                          version="%prog 1.0")
    parser.add_option("-f", "--file", dest="html_file",
                      help="use html file", metavar="FILE")
    parser.add_option("-u", "--url", dest="url",
                      help="get html file from URL and convert it",
                      metavar="URL")
    parser.add_option("-o", "--out", dest="out",
                      help="output file name",
                      metavar="PDF")
    (options, args) = parser.parse_args()

    # Option -f and -u cannot be specified simultaneously
    if options.html_file and options.url:
        parser.error("options -f and -u are exclusive")

    # wkhtmltopdf options
    # These options should be set by command line options
    wkhtmltopdf_options = {
        'page-size': 'A4',
        'orientation': 'portrait',
        'encoding': "UTF-8",
        'no-outline': None,
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'javascript-delay': '5000',
    }

    h = html2pdf()
    # following codes violate the DRY manner.
    if options.html_file != None:
        h.make_pdf_by_file(html_file = options.html_file,
                           out = options.out,
                           options = wkhtmltopdf_options)
    if options.url != None:
        h.make_pdf_by_url(url = options.url,
                          out = options.out,
                          options = wkhtmltopdf_options)
