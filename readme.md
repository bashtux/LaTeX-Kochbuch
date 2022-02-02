# LaTeX Kochbuch
A Template based on https://github.com/lmoppert/LaTeX-Kochbuch work.
Tried to streamline packages and improved a couple things:
- inserted commands for colors of all titles etc. to be changed in one single place
- improved the ingredient list
- added numbers to the cooking instructions

## Getting started
This is a collection of single recipes formated with LaTeX and tight together into a single cookbook by the central *RecipeCollection.tex* file.

### Prerequisites
In order to compile the cookbook you will need a working LaTeX installation, see https://www.latex-project.org/get/ to find a suitable solution for you.

### Compilation
For a basic compilation use pdflatex (twice, to generate table of contents)
If you want to generate the index as well, use the following structure
```
pdflatex kochbuch.tex
makeindex -g -r -s IndexStyle.ist RecipeCollection.idx
pdflatex kochbuch.tex
pdflatex kochbuch.tex
```
This should create a file called *RecipeCollection.pdf*
