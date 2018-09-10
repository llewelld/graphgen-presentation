all: automark-process.pdf strange01.pdf strange02.pdf strange03.pdf automark01.pdf

INKSCAPE = inkscape

DOT = dot

DOT_SVG_FLAGS = -Tsvg

DOT_PDF_FLAGS = -Tpdf

%.svg: %.dot
	$(DOT) $(DOT_SVG_FLAGS) $< > $@

automark-process.pdf: automark-process.svg
	$(INKSCAPE) $< --export-pdf=$@

strange.txt:
	python gen-strange-data.py

strange01.pdf: strange.txt
	python gen-strange01.py 

strange02.pdf: strange.txt
	python gen-strange02.py 

strange03.pdf: strange.txt
	python gen-strange03.py 

automark01.pdf: automark.txt
	python gen-automark01.py

clean:
	rm -f automark-process.svg automark-process.pdf strange.txt strange01.pdf strange02.pdf strange03.pdf automark01.pdf


