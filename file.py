# Made with https://machinelearningmastery.com/how-to-train-an-object-detection-model-with-keras/ as a reference

import Mask_RCNN.mrcnn.config as Config
from Mask_RCNN.mrcnn.model import MaskRCNN
class LightConfig(Config):

    NAME = "light_cfg"

    NUM_CLASSES = 3

    STEPS_PER_EPOCH = 603


config = LightConfig()

model = MaskRCNN(mode='training', model_dir='./', config=config)

model.load_weights('mask_rcnn_coco.h5', by_name=True, exclude=["mrcnn_class_logits", "mrcnn_bbox_fc",  "mrcnn_bbox", "mrcnn_mask"])

model.train(train_set, test_set, learning_rate=config.LEARNING_RATE, epochs=5, layers='heads')