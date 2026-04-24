from staintools.stain_extraction.abc_stain_extractor import ABCStainExtractor
from staintools.utils.miscellaneous_functions import normalize_matrix_rows
from staintools.utils.optical_density_conversion import convert_RGB_to_OD
from staintools.tissue_masks.luminosity_threshold_tissue_locator import (
    LuminosityThresholdTissueLocator,
)
from staintools.preprocessing.input_validation import is_uint8_image


class VahadaneStainExtractor(ABCStainExtractor):
    @staticmethod
    def get_stain_matrix(I, luminosity_threshold=0.8, regularizer=0.1):
        """
        Stain matrix estimation via method of:
        A. Vahadane et al. 'Structure-Preserving Color Normalization and Sparse Stain Separation for Histological Images'

        :param I: Image RGB uint8.
        :param luminosity_threshold:
        :param regularizer:
        :return:
        """
        pass
