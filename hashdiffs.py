# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 15:23:07 2017

@author: prasad.varma
"""

import hashtest
import pprint

images, image_hashes = hashtest.scan_and_hash('code\images')
#plotmat = hashtest.find_hash_diffs(image_hashes)
pprint.pprint(hashtest.find_rel_images(images, image_hashes,diff_max = 12))
