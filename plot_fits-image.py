# -*- coding: utf-8 -*-
"""
=======================================
Read and plot an image from a FITS file
=======================================

This example opens an image stored in a FITS file and displays it to the screen.

This example uses `astropy.utils.data` to download the file, `astropy.io.fits` to open
the file, and `matplotlib.pyplot` to display the image.

-------------------

*By: Lia R. Corrales, Adrian Price-Whelan, Kelle Cruz*

*License: BSD*

-------------------

"""

##############################################################################
# Set up matplotlib and use a nicer set of plot parameters

import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)

##############################################################################
# Download the example FITS files used by this example:

from astropy.utils.data import download_file
from astropy.io import fits

#image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits',
            #               cache=True)
#image_file = fits.open('C111221.0077.fits')
##############################################################################
# Use `astropy.io.fits.info()` to display the structure of the file:

fits.info('C111221.0077.fits')

##############################################################################
# Generally the image information is located in the Primary HDU, also known
# as extension 0. Here, we use `astropy.io.fits.getdata()` to read the image
# data from this first extension using the keyword argument ``ext=0``:

image_data = fits.getdata('C111221.0077.fits', ext=0)

##############################################################################
# The data is now stored as a 2D numpy array. Print the dimensions using the
# shape attribute:

print(image_data.shape)

##############################################################################
# Display the image data:

plt.figure()
plt.imshow(image_data, cmap='gray',vmin=0,vmax=1)
plt.colorbar()
plt.show()
