# -*- coding: utf-8 -*-
"""
Tools for kernel identification.

Functions
---------
assert_enough_data_samples :
    Assert that there is enough data samples for the identification.
cplx_to_real :
    Cast a complex numpy.ndarray to a specific type using a given mode.

Notes
-----
Developed for Python 3.6.1
@author: Damien Bouvier (Damien.Bouvier@ircam.fr)
"""

#==============================================================================
# Importations
#==============================================================================

import warnings
import numpy as np


#==============================================================================
# Functions
#==============================================================================

def assert_enough_data_samples(nb_data, max_nb_est, M, N, name):
    """
    Assert that there is enough data samples for the identification.

    Parameters
    ----------
    nb_data : int
        Number of data samples in the input signal used for identification.
    max_nb_est : int
        Maximum size of linear problem to solve.
    M : int or list(int)
        Memory length for each kernels (in samples).
    N : int
        Truncation order.
    name : str
        Name of the identification method.

    Raises
    ------
    ValueError
        If L is inferior to the number of Volterra coefficients.
    """

    if nb_data < max_nb_est:
        raise ValueError('Input signal has {} data samples'.format(nb_data) +
                         ', it should have at least {} '.format(max_nb_est) +
                         'for a truncation to order {} '.format(N) +
                         'and a {}-samples memory length'.format(M) +
                         'using {} method.'.format(name))


def complex2real(sig_cplx, cast_mode='real-imag'):
    """
    Cast a numpy.ndarray of complex type to real type with a specified mode.

    Parameters
    ----------
    sig_cplx : numpy.ndarray
        Array to cast to real numbers.
    cast_mode : {'real', 'imag', 'real-imag'}, optional (default='real-imag')
        Choose how complex number are casted to real numbers.

    Returns
    -------
    sig_casted : numpy.ndarray
        Array ``sig_cplx`` casted to real numbers following ``cast_mode``.
    """

    if cast_mode not in {'real', 'imag', 'real-imag', 'cplx'}:
        warnings.warn("Unknown cast_mode, mode 'real-imag' used.", UserWarning)
        cast_mode = 'real-imag'

    if cast_mode == 'real':
        return np.real(sig_cplx)
    elif cast_mode == 'imag':
        return np.imag(sig_cplx)
    elif cast_mode == 'real-imag':
        return np.concatenate((np.real(sig_cplx), np.imag(sig_cplx)), axis=0)
    elif cast_mode == 'cplx':
        return sig_cplx
