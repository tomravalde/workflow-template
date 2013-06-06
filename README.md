LaTeX_template
==============

## Project structure
- `main.tex` is the base file for the project.
	- Defines the `\documentclass`
	- Loads the version control
	- Specifies the start and end of the document with `\begin{document ]` and `\end{document}`
	- Load all other `*.tex` files, contents, bibliography etc.
- `foo.sty` loads all necessary packages, and defines new commands. Comment out anything you don't want to use.

- `main.tex` is the main document which calls all the other `*.tex` and `*.bib` files.

- `main.tex.latexmain` tells vim-LaTeX that `main.tex` is the main  document file, such that the document can be compiled from any file opened within Vim.

- `*.tex`, images, tables and source-code are all kept in separate sub-directories.

## Version control
- `vc` and `vc-git.awk` are used with Stephan Hennig's version control bundle (http://www.ctan.org/tex-archive/support/vc/). 
- a `vc.tex` file will be generated which contains macros which allows you to insert revision information in the document---see the `\fancyfoot` definitions in the `*.sty` style file.
- (Comment out these commands if not using version control).

## Bibliography style
- `kbib.bst` is used to such that references are printed 'Surname, Firstname' in the Reference list.
- This is used in conjuction with the `natbib` package, for Author-Year citations.
