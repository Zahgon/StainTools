import cv2 as cv

from staintools.tissue_masks.abc_tissue_locator import ABCTissueLocator
from staintools.utils.exceptions import TissueMaskException
from staintools.preprocessing.input_validation import is_uint8_image


class LuminosityThresholdTissueLocator(ABCTissueLocator):

    @staticmethod
    def get_tissue_mask(I, luminosity_threshold=0.8):
        """
        Get a binary mask where true denotes pixels with a luminosity less than the specified threshold.
        Typically we use to identify tissue in the image and exclude the bright white background.

        :param I: RGB uint 8 image.
        :param luminosity_threshold: Luminosity threshold.
        :return: Binary mask.
        """
        pass
