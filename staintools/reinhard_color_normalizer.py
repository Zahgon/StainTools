import numpy as np
import cv2 as cv

from staintools.preprocessing.input_validation import is_uint8_image


class ReinhardColorNormalizer(object):
    """
    Normalize a patch color to the target image using the method of:
    E. Reinhard, M. Adhikhmin, B. Gooch, and P. Shirley,
    'Color transfer between images'
    """

    def __init__(self):
        self.target_means = None
        self.target_stds = None

    def fit(self, target):
        """
        Fit to a target image

        :param target: Image RGB uint8.
        :return:
        """
        pass

    def transform(self, I):
        """
        Transform an image.

        :param I: Image RGB uint8.
        :return:
        """
        pass

    @staticmethod
    def lab_split(I):
        """
        Convert from RGB uint8 to LAB and split into channels.

        :param I: Image RGB uint8.
        :return:
        """
        pass

    @staticmethod
    def merge_back(I1, I2, I3):
        """
        Take seperate LAB channels and merge back to give RGB uint8.

        :param I1: L
        :param I2: A
        :param I3: B
        :return: Image RGB uint8.
        """
        pass

    def get_mean_std(self, I):
        """
        Get mean and standard deviation of each channel.

        :param I: Image RGB uint8.
        :return:
        """
        pass
