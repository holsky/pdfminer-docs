pdfminer docs for ReadTheDocs_

.. _ReadTheDocs: http://pdfminer-docs.readthedocs.io

- ReStructuredTexts converted by pandoc.

::

    docker pull jagregory/pandoc
    docker run -v `pwd`:/source jagregory/pandoc \
      -f html -t rst index.html -o pdfminer_index.rst
      docker run -v `pwd`:/source jagregory/pandoc \
      -f html -t rst programming.html -o programming.rst
