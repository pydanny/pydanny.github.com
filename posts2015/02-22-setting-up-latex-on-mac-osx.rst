============================
Setting up LaTeX on Mac OS X
============================

:date: 2015-02-22 14:00
:tags: book, LaTeX, howto, python
:category: book
:slug: setting-up-latex-on-mac-os-x

These are my notes for getting LaTeX running on Mac OS X with the components and fonts I want. Which is handy when you want to generate PDFs from Sphinx_. At some point I want to replace this with a Docker_ container similar https://github.com/blang/latex-docker, albeit with the components in parts 3 and 4 below.

.. _LaTeX: http://en.wikipedia.com/wiki/LateX
.. _Docker: https://www.docker.com/
.. _Sphinx: http://sphinx-doc.org/

1. Get mactex-basic.pkg from http://www.ctan.org/pkg/mactex-basic

2. Click mactex-basic.pkg to install LaTeX.

3. Update ``tlmgr``::

    sudo tlmgr update --self

3. Install the following tools via ``tlmgr``::

    sudo tlmgr install titlesec
    sudo tlmgr install framed
    sudo tlmgr install threeparttable
    sudo tlmgr install wrapfig
    sudo tlmgr install multirow
    sudo tlmgr install enumitem
    sudo tlmgr install bbding
    sudo tlmgr install titling
    sudo tlmgr install tabu
    sudo tlmgr install mdframed
    sudo tlmgr install tcolorbox
    sudo tlmgr install textpos
    sudo tlmgr install import
    sudo tlmgr install varwidth
    sudo tlmgr install needspace
    sudo tlmgr install tocloft
    sudo tlmgr install ntheorem
    sudo tlmgr install environ
    sudo tlmgr install trimspaces

4. Install fonts via ``tlmgr``::

    sudo tlmgr install collection-fontsrecommended

**note:** Yes, I know I can install the basic LaTeX package using Homebrew_, but sometimes I like doing things manually.

.. _Homebrew: http://brew.sh/

.. image:: http://upload.wikimedia.org/wikipedia/commons/9/9c/Latex_example.png
   :name: packages
   :align: center
   :target: http://en.wikipedia.org/wiki/LaTeX#mediaviewer/File:Latex_example.png