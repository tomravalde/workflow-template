LaTeX_template
==============
Look at `main.tex` to see how the LaTeX document works. This should make the project fairly self-explanatory.

## Root directory
- `ESA_style.sty` loads all necessary packages, and stores user-defined commands. Comment out anything you don't want to use.

- `main.tex` is the main document which calls all the other `*.tex` and `*.bib` files.

- `main.tex.latexmain` tells vim-LaTeX that `main.tex` is the main docuement file, such that the document can be compiled from any LaTeX document.

### Version control
- `vc` and `vc-git.awk` are used with Stephan Hennig's version control bundle (http://www.ctan.org/tex-archive/support/vc/). 
- a `vc.tex` file will be generated which contains macros which allows you to insert revision information in the document---in `ESA_style.sty` in this case.
- If version control isn't being used, then comment out `\input{vc}` in `main.tex`; and comment out the `\fancyfoot` commands in `ESA_sytle.sty`.


## img
- Stores images for use in the document.

## notes
- I use `outline.md` to make notes about the content of my document.
- You can also use this to store other notes, references etc. I make sure these are ignored by Git.

## tex
- Stores the `*.tex` files which contain the document content.
