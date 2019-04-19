"""Model store which handles pretrained models """
from .fcn import *
from .fcnv2 import *
from .pspnet import *
from .deeplabv3 import *
from .danet import *
from .denseaspp import *
from .bisenet import *
from .encnet import *
from .dunet import *
from .icnet import *

__all__ = ['get_model', 'get_model_list', 'get_segmentation_model']

_models = {
    'fcn32s_vgg16_voc': get_fcn32s_vgg16_voc,
    'fcn16s_vgg16_voc': get_fcn16s_vgg16_voc,
    'fcn8s_vgg16_voc': get_fcn8s_vgg16_voc,
    'fcn_resnet50_voc': get_fcn_resnet50_voc,
    'fcn_resnet101_voc': get_fcn_resnet101_voc,
    'fcn_resnet152_voc': get_fcn_resnet152_voc,
    'psp_resnet50_voc': get_psp_resnet50_voc,
    'psp_resnet50_ade': get_psp_resnet50_ade,
    'psp_resnet101_voc': get_psp_resnet101_voc,
    'psp_resnet101_ade': get_psp_resnet101_ade,
    'psp_resnet101_citys': get_psp_resnet101_citys,
    'psp_resnet101_coco': get_psp_resnet101_coco,
    'deeplabv3_resnet50_voc': get_deeplabv3_resnet50_voc,
    'deeplabv3_resnet101_voc': get_deeplabv3_resnet101_voc,
    'deeplabv3_resnet152_voc': get_deeplabv3_resnet152_voc,
    'deeplabv3_resnet50_ade': get_deeplabv3_resnet50_ade,
    'deeplabv3_resnet101_ade': get_deeplabv3_resnet101_ade,
    'deeplabv3_resnet152_ade': get_deeplabv3_resnet152_ade,
    'danet_resnet50_ciyts': get_danet_resnet50_citys,
    'danet_resnet101_citys': get_danet_resnet101_citys,
    'danet_resnet152_citys': get_danet_resnet152_citys,
    'denseaspp_densenet121_citys': get_denseaspp_densenet121_citys,
    'denseaspp_densenet161_citys': get_denseaspp_densenet161_citys,
    'denseaspp_densenet169_citys': get_denseaspp_densenet169_citys,
    'denseaspp_densenet201_citys': get_denseaspp_densenet201_citys,
    'bisenet_resnet18_citys': get_bisenet_resnet18_citys,
    'encnet_resnet50_ade': get_encnet_resnet50_ade,
    'encnet_resnet101_ade': get_encnet_resnet101_ade,
    'encnet_resnet152_ade': get_encnet_resnet152_ade,
    'dunet_resnet50_pascal_voc': get_dunet_resnet50_pascal_voc,
    'dunet_resnet101_pascal_voc': get_dunet_resnet101_pascal_voc,
    'dunet_resnet152_pascal_voc': get_dunet_resnet152_pascal_voc,
    'icnet_resnet50_citys': get_icnet_resnet50_citys,
    'icnet_resnet101_citys': get_icnet_resnet101_citys,
    'icnet_resnet152_citys': get_icnet_resnet152_citys,
}


def get_model(name, **kwargs):
    name = name.lower()
    if name not in _models:
        err_str = '"%s" is not among the following model list:\n\t' % (name)
        err_str += '%s' % ('\n\t'.join(sorted(_models.keys())))
        raise ValueError(err_str)
    net = _models[name](**kwargs)
    return net


def get_model_list():
    return _models.keys()


def get_segmentation_model(model, **kwargs):
    models = {
        'fcn32s': get_fcn32s,
        'fcn16s': get_fcn16s,
        'fcn8s': get_fcn8s,
        'fcn': get_fcn,
        'psp': get_psp,
        'deeplabv3': get_deeplabv3,
        'danet': get_danet,
        'denseaspp': get_denseaspp,
        'bisenet': get_bisenet,
        'encnet': get_encnet,
        'dunet': get_dunet,
        'icnet': get_icnet,
    }
    return models[model](**kwargs)
