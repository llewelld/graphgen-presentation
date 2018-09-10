# Automatically Generating Visualisations

A presentation given as part of teh Molecular Laboratory Training Workshop 2018.

You can download the pre-built presentation slides, and the example paper that demonstrates embedding the automatically generated graph into a document, from here:
1. Slides: http://www.flypig.co.uk/presentations/graphgen-presentation.pdf
2. Example document: http://www.flypig.co.uk/presentations/graphgen-example.pdf

In order to build the files you'll need (at least) the following:
1. LaTeX
2. pdflatex
3. beamer
4. dot
5. python
6. matplotlib

On Ubuntu, the `texlive-math-extra` is needed to provide the yhmath and eqnarray packages. 

To build the document:
```
make
```

This will generate all graphs, the presentation and example paper. The main output files are

1. presentation.pdf
2. example.pdf

You can use `make clean` to remove temporary build files.






