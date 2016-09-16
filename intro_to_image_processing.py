import numpy as np

# Our image processing tools
import skimage.filters
import skimage.io
import skimage.morphology
import skimage.exposure

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

im_phase = skimage.io.imread('data/bsub_100x_phase.tif')
cfp_im=skimage.io.imread('data/bsub_100x_phase.tif')

with sns.axes_style('dark'):
    skimage.io.imshow(im_phase / im_phase.max())

hist_phase, bins_phase = skimage.exposure.histogram(im_phase)
plt.plot(bins_phase, hist_phase)

#apply threshold to image
thresh=250
in_phase_thresh=im_phase < thresh

with sns.axes_style('dark'):
    plt.imshow(in_phase_thresh, cmap=plt.cm.Greys_r)
plt.show()

with sns.axes_style('dark'):
    plt.imshow(cfp_im, cmap=plt.cm.viridis)

selem = skimage.morphology.square(3)
cfp_filt=skimage.filters.median(cfp_im,selem)

with sns.axes_style('dark'):
    plt.imshow(cfp_filt[150:250, 450:550]/cfp_filt.max(), cmap=plt.cm.viridis)
plt.show()

x, y = skimage.exposure.histogram(cfp_filt)
plt.plot(y,x)

plt.show()



cfp_thresh = 250<cfp_filt > 120
with sns.axes_style('dark'):
    plt.imshow(cfp_thresh, cmap=plt.cm.Greys_r)

plt.show(_)
