
from tabulate import *
import os, sys, pdfrw, pdfminer
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfrw import *

def pdf_title(fname):
    name = PdfReader(fname).Info.Title

    r =  name if not name is None and len(name) else None
    if not r: return r
    return r

def f2(fname):
    fp = open(fname, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument(parser)
    fp.close()
    metadata = doc.info  # The "Info" metadata
    print (metadata)
    metadata = metadata[0]
    for x in metadata:
        if x == "Title":
            #new_name = metadata[x].decode('utf-8') + ".pdf"
            try:
                #print(metadata[x].decode('utf-8'))
                return metadata[x].decode('utf-8')
            except:
                
                #print(metadata[x])
                return metadata[x]
                pass
            #os.rename(file_name,new_name)
            pass
        pass
    pass
def f2x(fx):
    for i in fx:
        yield i, f2(i), pdf_title(i)
        pass
    pass
if __name__ == '__main__':
    
    for i in sys.argv[1:]:
        #        print(i, pdf_title(i))
        #f2(i)
        pass
    ax = list(f2x(sys.argv[1:]))
    
    print(tabulate(ax,tablefmt='github'))
