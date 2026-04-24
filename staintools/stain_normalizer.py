import numpy as np

from staintools.stain_extraction.macenko_stain_extractor import MacenkoStainExtractor
from staintools.stain_extraction.vahadane_stain_extractor import VahadaneStainExtractor
from staintools.utils.optical_density_conversion import convert_OD_to_RGB
from staintools.utils.get_concentrations import get_concentrations


class StainNormalizer(object):

    def __init__(self, method):
        raise NotImplementedError

    def fit(self, target):
        """
        Fit to a target image.

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
