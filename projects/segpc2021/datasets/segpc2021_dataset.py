from mmseg.datasets import BaseSegDataset
from mmseg.registry import DATASETS

@DATASETS.register_module()
class Segpc2021Dataset(BaseSegDataset):
    """Segpc2021Dataset dataset.
    In segmentation map annotation for Segpc2021Dataset, 0 stands for background,
    which is included in 3 categories. ``reduce_zero_label`` is fixed to
    False. The ``img_suffix`` is fixed to '.png' and ``seg_map_suffix`` is
    fixed to '.png'.
    Args:
        img_suffix (str): Suffix of images. Default: '.png'
        seg_map_suffix (str): Suffix of segmentation maps. Default: '.png'
    """
    METAINFO = dict(
        classes=('background', 'Cytoplasm', 'Nucleus')
        )
    
    def __init__(self,
                 img_suffix='.bmp',
                 seg_map_suffix='.bmp',
                 reduce_zero_label=False,
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix,
            seg_map_suffix=seg_map_suffix,
            reduce_zero_label=reduce_zero_label,
            **kwargs)