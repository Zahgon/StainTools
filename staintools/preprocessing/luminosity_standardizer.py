import numpy as np
import cv2 as cv

from staintools.preprocessing.input_validation import is_uint8_image


class LuminosityStandardizer(object):

    @staticmethod
    def standardize(I, percentile=95):
        """
        Transform image I to standard brightness.
        Modifies the luminosity channel such that a fixed percentile is saturated.

        :param I: Image uint8 RGB.
        :param percentile: Percentile for luminosity saturation. At least (100 - percentile)% of pixels should be fully luminous (white).
        :return: Image uint8 RGB with standardized brightness.
        """
        pass
