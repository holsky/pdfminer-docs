PDFMiner
========

Python PDF parser and analyzer

`Homepage`_   `Recent Changes`_   `PDFMiner API`_

-  `How to Install`_

   -  `CJK languages support`_

-  `Command Line Tools`_

   -  `pdf2txt.py`_
   -  `dumppdf.py`_
   -  `PDFMiner API`_

-  `Changes`_
-  `TODO`_
-  `Related Projects`_
-  `Terms and Conditions`_

What’s It?
-----------------

PDFMiner is a tool for extracting information from PDF documents. Unlike
other PDF-related tools, it focuses entirely on getting and analyzing
text data. PDFMiner allows one to obtain the exact location of text in a
page, as well as other information such as fonts or lines. It includes a
PDF converter that can transform PDF files into other text formats (such
as HTML). It has an extensible PDF parser that can be used for other
purposes than text analysis.

Features
~~~~~~~~

-  Written entirely in Python. (for version 2.6 or newer)
-  Parse, analyze, and convert PDF documents.
-  PDF-1.7 specification support. (well, almost)
-  CJK languages and vertical writing scripts support.
-  Various font types (Type1, TrueType, Type3, and CID) support.
-  Basic encryption (RC4) support.
-  PDF to HTML conversion (with a sample converter web app).
-  Outline (TOC) extraction.
-  Tagged contents extraction.
-  Reconstruct the original layout by grouping text chunks.

PDFMiner is about 20 times slower than other C/C++-based counterparts
such as XPdf.

| **Online Demo:** (pdf -> html conversion webapp)
| http://pdf2html.tabesugi.net:8080/

Download
~~~~~~~~~~~~~~~

| **Source distribution:**
| http://pypi.python.org/pypi/pdfminer/

| **github:**
| https://github.com/euske/pdfminer/

Where to Ask
~~~~~~~~~~~~~~~~~~~

| **Questions and comments:**
|  http://groups.google.com/group/pdfminer-users/

.. _Homepage: http://www.unixuser.org/~euske/python/pdfminer/index.html
.. _Recent Changes: #changes
.. _PDFMiner API: programming.html
.. _What’s It?: #intro
.. _Download: #download
.. _Where to Ask: #wheretoask
.. _How to Install: #install
.. _CJK languages support: #cmap
.. _Command Line Tools: #tools
.. _pdf2txt.py: #pdf2txt
.. _dumppdf.py: #dumppdf
.. _Changes: #changes
.. _TODO: #todo
.. _Related Projects: #related
.. _Terms and Conditions: #license
