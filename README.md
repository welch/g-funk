g-funk
====
[![Build Status][travis-image]][travis-url] [![PyPI version][pypi-image]][pypi-url] [![PyPI download][download-image]][pypi-url]

Whole-Genome Functional Classification of Genes

`g-funk` is a Python implementation of a variant of the technique described in:

    Ng, et al, "Whole-Genome Functional Classification of Genes
    by Latent Semantic Analysis on Microarray Data"
    http://datam.i2r.a-star.edu.sg/~skng/papers/APBC2004.pdf

It operates on whole-genome microarray gene expression data (N genes x
M experiments). It reduces the dimensionality of this data using
robust PCA (unsupervised), an improvement over the LSA technique of
the paper. It then clusters the unambiguous genes in the reduced space
(partially supervised) to discover functionally-related groups of
genes.

Dependencies
-------------
numpy

[travis-image]: https://travis-ci.org/welch/g-funk.svg?branch=master
[travis-url]: https://travis-ci.org/welch/g-funk
[pypi-image]: http://img.shields.io/pypi/v/g-funk.svg
[download-image]: http://img.shields.io/pypi/dm/g-funk.svg
[pypi-url]: https://pypi.python.org/pypi/g-funk
