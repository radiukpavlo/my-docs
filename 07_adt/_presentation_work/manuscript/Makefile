MAIN=main

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex references.bib ceurart.cls
	pdflatex $(MAIN)
	bibtex $(MAIN) || bibtex8 $(MAIN)
	pdflatex $(MAIN)
	pdflatex $(MAIN)

clean:
	rm -f $(MAIN).aux $(MAIN).bbl $(MAIN).blg $(MAIN).log $(MAIN).out $(MAIN).toc $(MAIN).xmpdata $(MAIN).abs pdfa.xmpi
