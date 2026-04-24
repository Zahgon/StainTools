import numpy as np
import copy

from staintools.stain_extraction.macenko_stain_extractor import MacenkoStainExtractor
from staintools.stain_extraction.vahadane_stain_extractor import VahadaneStainExtractor
from staintools.tissue_masks.luminosity_threshold_tissue_locator import LuminosityThresholdTissueLocator
from staintools.utils.get_concentrations import get_concentrations


class StainAugmentor(object):

    def __init__(self, method, sigma1=0.2, sigma2=0.2, augment_background=True):
        if method.lower() == 'macenko':
            self.extractor = MacenkoStainExtractor
        elif method.lower() == 'vahadane':
            self.extractor = VahadaneStainExtractor
        else:
            raise Exception('Method not recognized.')
        self.sigma1 = sigma1
        self.sigma2 = sigma2
        self.augment_background = augment_background

    def fit(self, I):
        """
        Fit to an image I.

        :param I:
        :return:
        """
        pass

    def pop(self):
        """
        Get an augmented version of the fitted image.

        :return:
        """
        pass
