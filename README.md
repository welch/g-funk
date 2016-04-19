g-funk
====
[![Build Status][travis-image]][travis-url] [![PyPI version][pypi-image]][pypi-url] [![PyPI download][download-image]][pypi-url]

Whole-Genome Functional Classification of Genes using robust PCA

Back in the early aughts, full-genome microarray assays really hit
their stride, and there was a boom in literature for analyzing the
results.  Trees. Clusters. Dimensionality reduction. Or choose two and
go again.

Let's revisit those heady times with a more recent numerical technique
-- L+S decompostion. SVD decomposition as both dimension reduction and
as a way to impose a hierarchic ordering on the genes and experiments
in the observation matrix seemed pretty promising before, except that
microarray data suffers from spotty noise and dropouts.  Back in the
day, the cool kids were "imputing" the missing values through local or
global regression (or just dropping the loser genes from the matrix
altogether), and then applying stock clustering or factorization to
the filled observation matrix. But more modern L+S decomposition
directly addresses this model of a corrupted observation matrix. Will
it do a nice job without all the pre-processing?

Dependencies
-------------
numpy

[travis-image]: https://travis-ci.org/welch/g-funk.svg?branch=master
[travis-url]: https://travis-ci.org/welch/g-funk
[pypi-image]: http://img.shields.io/pypi/v/g-funk.svg
[download-image]: http://img.shields.io/pypi/dm/g-funk.svg
[pypi-url]: https://pypi.python.org/pypi/g-funk
