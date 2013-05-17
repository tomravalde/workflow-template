LaTeX_template
==============

## Project structure

### Root directory
- ESA_style.sty loads all necessary packages, and stores user-defined commands. Comment out anything you don't want to use.

- main.tex is the main document class.

- main.tex.latexmain tells vim-LaTeX that 'main' is the main docuement, such that the document can be compiled from any LaTeX document.

- vc and vc-git.awk are used with version control. If version control isn't being used, then comment out \input{vc} in main.tex.

### img
- Stores images for use in the document.

### notes
- I use outline.md to make notes about the content of my document.

### tex
- Contains the \*.tex files which contain the document content.
