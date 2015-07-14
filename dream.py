from batcountry import BatCountry
import numpy as np
import urllib
import cStringIO
from PIL import *

class Dream:

  def __init__(args):
    guide_image = img_url_to_file(args['guide_image'])
    main_image = img_url_to_file(args['main_image'])

  def img_url_to_file(img_url):
    f = cStringIO.StringIO(urllib.urlopen(img_url).read())
    return Image.open(f)