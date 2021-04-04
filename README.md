# Introduction

I was asked if I could hack together something for processing the
category pages until `n`th page for their exam preparations.

Having an offline copy of the articles would be useful for reading
material.

# Dependency

The project depends on modules listed in the `requirements.txt`
file. The program uses Python 3.6+. Install dependencies with `pip`:

    pip install -r requirements.txt

# Usage

The `-h` parameter to the executable `main.py` provides you with:

    $ ./main.py -h
    usage: main.py [-h] [--start START] category page_num

    Parse and save as PDF range of pages from gktoday.in for category

    positional arguments:
      category              Provide category for the website such as `environment-current-affairs`
      page_num              Page until which to parse

    optional arguments:
      -h, --help            show this help message and exit
      --start START, -s START
                            Start parsing from this page

which is enough to begin putting together the pages. The generated PDF
files are placed into the directory structure as follows:

    articles/<category>/<month-name>/<article-title>

# Combining all files to a single files

While I could do this in python itself, I thought that having it
create separate pdf for individual articles is better. Using quite
famous `poppler-utils` commandline utility, namely, `pdfunite`; you
can generate the final files.

    cd articles
    for i in *
    do
      cd $i
      for mo in *
      do
        cd mo
    	pdfunite *.pdf ../$mo.pdf
    	cd ..
      done
      pdfunite *.pdf "${i}.pdf"
    done

# Credits

 1. weasyprint
 1. requests-html
 1. poppler-utils
 1. This [stack overflow](https://stackoverflow.com/q/23359083/1190388) post for suggesting weasyprint
 1. Another [SO thread](https://stackoverflow.com/a/11280219/1190388) for pdfunite
 1. GKToday.in for the content
