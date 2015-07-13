from batcountry import BatCountry
import numpy as np
from PIL import *
import pdb

bc = BatCountry("/home/dylan/caffe/models/bvlc_googlenet")
features = bc.prepare_guide(Image.open('./guide.jpg'), end='inception_5b/5x5_reduce')
image = bc.dream(np.float32(Image.open('./image.jpg')), end='inception_5b/5x5_reduce',
    iter_n=20, objective_fn=BatCountry.guided_objective,
    objective_features=features,)
pdb.set_trace()
bc.cleanup()