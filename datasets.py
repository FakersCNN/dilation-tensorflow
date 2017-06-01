import numpy as np

# configuration for different datasets
CONFIG = {
    'cityscapes': {
        'classes': 19,
        'weights_file': 'dilation_cityscapes.h5',
        'weights_url': 'http://imagelab.ing.unimore.it/files/dilation_keras/cityscapes.h5',
        'input_shape': (1396, 1396, 3),
        'test_image': 'data/cityscapes.png',
        'mean_pixel': (72.39, 82.91, 73.16),
        'palette': np.array([[128, 64, 128],
                            [244, 35, 232],
                            [70, 70, 70],
                            [102, 102, 156],
                            [190, 153, 153],
                            [153, 153, 153],
                            [250, 170, 30],
                            [220, 220, 0],
                            [107, 142, 35],
                            [152, 251, 152],
                            [70, 130, 180],
                            [220, 20, 60],
                            [255, 0, 0],
                            [0, 0, 142],
                            [0, 0, 70],
                            [0, 60, 100],
                            [0, 80, 100],
                            [0, 0, 230],
                            [119, 11, 32]], dtype='uint8'),
        'zoom': 1,
        'conv_margin': 186
    },
    'voc12': {
        'classes': 21,
        'weights_file': 'dilation_voc12.h5',
        'weights_url': 'http://imagelab.ing.unimore.it/files/dilation_keras/voc12.h5',
        'input_shape': (3, 900, 900),
        'test_image': 'data/voc.jpg',
        'mean_pixel': (102.93, 111.36, 116.52),
        'palette': np.array([[0, 0, 0],
                            [128, 0, 0],
                            [0, 128, 0],
                            [128, 128, 0],
                            [0, 0, 128],
                            [128, 0, 128],
                            [0, 128, 128],
                            [128, 128, 128],
                            [64, 0, 0],
                            [192, 0, 0],
                            [64, 128, 0],
                            [192, 128, 0],
                            [64, 0, 128],
                            [192, 0, 128],
                            [64, 128, 128],
                            [192, 128, 128],
                            [0, 64, 0],
                            [128, 64, 0],
                            [0, 192, 0],
                            [128, 192, 0],
                            [0, 64, 128]], dtype='uint8'),
        'zoom': 8,
        'conv_margin': 186
    },
    'kitti': {
        'classes': 11,
        'weights_file': 'dilation_kitti.h5',
        'weights_url': 'http://imagelab.ing.unimore.it/files/dilation_keras/kitti.h5',
        'input_shape': (3, 852, 1640),
        'test_image': 'data/kitti.png',
        'mean_pixel': (96.19, 95.55, 91.34),
        'palette': np.array([[128, 0, 0],
                             [128, 128, 0],
                             [128, 128, 128],
                             [64, 0, 128],
                             [192, 128, 128],
                             [128, 64, 128],
                             [64, 64, 0],
                             [64, 64, 128],
                             [192, 192, 128],
                             [0, 0, 192],
                             [0, 128, 192]], dtype='uint8'),
        'zoom': 8,
        'conv_margin': 186
    },
    'camvid': {
        'classes': 11,
        'weights_file': 'dilation_camvid.h5',
        'weights_url': 'http://imagelab.ing.unimore.it/files/dilation_keras/camvid.h5',
        'input_shape': (3, 900, 1100),
        'test_image': 'data/camvid.png',
        'mean_pixel': (110.70, 108.77, 105.41),
        'palette': np.array([[128, 0, 0],
                             [128, 128, 0],
                             [128, 128, 128],
                             [64, 0, 128],
                             [192, 128, 128],
                             [128, 64, 128],
                             [64, 64, 0],
                             [64, 64, 128],
                             [192, 192, 128],
                             [0, 0, 192],
                             [0, 128, 192]], dtype='uint8'),
        'zoom': 8,
        'conv_margin': 186
    }
}
