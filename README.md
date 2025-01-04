# Sweetspot - a Ray-Triangle intersection showcase module
Author: Audun Skau Hansen (audunsh4@gmail.com) 2022

## Overview

This project was rapidly developed as my submission to a coding challenge from a former employer. I'll keep it here to showcase that I can -- in fact -- write clean and well-documented code, as I acknowledge that some of my other open repositories may appear chaotic upon visitation.

## Installation instructions

Run 

```
pip install .
```

from the project root folder.

## Test installation

Run

```
python3 -m pytest tests/*
```

from the project root folder.

## Build documentation

The project is documented (both researchwise and in regards to development) with mkdocs-material. Please let me know if you are unable to view the documentation properly (in which case I can make it available for you over github-pages).

To install mkdocs-material (and mkdocstrings) locally:

```
pip install mkdocs-material mkdocstrings
```

...then build the documentation (from the root folder):

```
mkdocs serve
```

...and open the local served pages in your browser. All written documentation can be found in the Docs-folder.