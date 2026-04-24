import numpy as np
import os
import matplotlib.pyplot as plt


def plot_row_colors(C, fig_size=6, title=None):
    """
    Plot rows of C as colors (RGB)

    :param C: An array N x 3 where the rows are considered as RGB colors.
    :return:
    """
    pass


def plot_image(image, show=True, fig_size=10, title=None):
    """
    Plot an image (np.array).
    Caution: Rescales image to be in range [0,1].

    :param image: RGB uint8
    :param show: plt.show() now?
    :param fig_size: Size of largest dimension
    :param title: Image title
    :return:
    """
    pass


def plot_image_list(images, width=5, sub_sample=False, rand=False, save_name=None, title_list=None, show=True):
    """
    Display a grid of images.

    :param images: List of RGB uint8
    :param width: Number of images per row.
    :param sub_sample: Number of images to subsample or false.
    :param rand: Should the subsample be randomized?
    :param save_name: File name to save to.
    :param title_list: A list of titles. Should only be used when sub_sample is false.
    :param show: plt.show() now?
    :return:
    """
    pass
