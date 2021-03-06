# pyvi - Python Toolbox for Volterra System Identification
This project proposes a python toolbox for Volterra Series Identification using nonlinear homogeneous order separation.

License
=======
[Pyvi](https://github.com/d-bouvier/pyvi) is distributed under the BSD 3-Clause "New" or "Revised" License.

Python prerequisites
====================
The [Pyvi](https://github.com/d-bouvier/pyvi) package is developped for Python 3 and needs the following packages installed:

- [numpy](http://www.numpy.org)
- [scipy](http://www.scipy.org)

The package has been fully tested with the following versions:

- python 3.6.4
- numpy 1.14.0
- scipy 0.19.1

Package structure
=================

The package is divided into the following submodules:

* [separation](https://github.com/d-bouvier/pyvi/tree/master/pyvi/separation)

Module for nonlinear homogeneous order separation of Volterra series.

* [identification](https://github.com/d-bouvier/pyvi/tree/master/pyvi/identification)

Module for Volterra kernels identification.

* [volterra](https://github.com/d-bouvier/pyvi/tree/master/pyvi/volterra)

Module creating various tools for Volterra series.

* [utilities](https://github.com/d-bouvier/pyvi/tree/master/pyvi/utilities)

Module containing various useful class and functions.

Authors
=======
Damien, Bouvier (Équipe S3AM, IRCAM, CNRS UMR 9912, UPMC, Paris, France) - damien.bouvier@ircam.fr

Hélie, Thomas (Équipe S3AM, IRCAM, CNRS UMR 9912, UPMC, Paris, France)

Roze, David Tristan (Équipe S3AM, IRCAM, CNRS UMR 9912, UPMC, Paris, France)
