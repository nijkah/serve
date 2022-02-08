from torchvision.models.detection.mask_rcnn import MaskRCNN
from torchvision.models.detection.backbone_utils import resnet_fpn_backbone


class MASKRCNNObjectDetector(MaskRCNN):
    def __init__(self, num_classes: int=91, **kwargs) -> None:
        backbone = resnet_fpn_backbone('resnet50', False)
        super(MASKRCNNObjectDetector, self).__init__(backbone, num_classes, **kwargs)

