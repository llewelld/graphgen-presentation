all: presentation.pdf example.pdf

main.aux: main.tex main.bib
#main.aux: main.tex
	pdflatex main.tex

main.bbl: main.aux
	bibtex main.aux

figures/strange.txt figures/automark.txt:
	@$(MAKE) -C figures

main.pdf: main.tex figures/strange.txt figures/automark.txt
	@$(MAKE) -C figures
	pdflatex main.tex
	pdflatex main.tex

example.pdf: sub.pdf
	cp sub.pdf example.pdf

sub.pdf: sub.tex sub.bbl figures/strange.txt figures/automark.txt
	@$(MAKE) -C figures
	pdflatex sub.tex
	pdflatex sub.tex

sub.bbl: sub.aux
	bibtex sub.aux

sub.aux: sub.tex main.bib
	pdflatex sub.tex

presentation.pdf: main.pdf
	cp main.pdf presentation.pdf

clean:
	@$(MAKE) -C figures clean
	rm -f *.blg *.log *.pdf *.bbl *.aux *.out *.wiki *.snm *.nav *.toc *.vrb

