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

## Feature ideas
- [ ] implementation of https://ctan.org/pkg/cooking-units?lang=de
- [ ] easier handling of folder management for categories, setting folders for whole categories
- [ ] individual pictures for recipes
- [ ] source for recipes including web link
- [ ] some sort of marked box for tips and hints
- [ ] Template for informational pages (cooking tables, portion size, etc.)
- [ ] MAKEFILE for corect compilattion
- [ ] nicer Header/Footer with colours
- [ ] make \index{A>B} work better (no duplicates)
- [ ] interactive recipe insertion (python)
- [ ] automatic alphabetic sorting for pre makefile (python)
- [ ] implement language for template
- [ ] multiple dietary restrictions possible

## implemented features

- [x] setup of a nice part layout e.g. for menus, general information 
- [x] implementing portions and time variable
- [x] intorduction of cooking symbols for baking, time, portions
