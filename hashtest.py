# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 14:08:30 2017

@author: prasad.varma
"""

from PIL import Image
import imagehash
import betterwalk
import os
#import pprint

def scan_and_hash(path, algo=0, resize=(64,64)):

    image_hashes = []
    images = []
    
    for root, dirs, files in betterwalk.walk(path):
        for name in files:
            if not name.endswith('jpg'):
                continue
            path = os.path.join(root, name)
            images.append(name)
            im = Image.open(path)
            im = im.resize(resize)

            image_hash = [imagehash.phash(im.rotate(90, expand=True)),imagehash.dhash(im.rotate(90, expand=True)), imagehash.phash(im)]
            '''            
            if algo == 0:        
                #image_hash = [imagehash.phash(im.rotate(90, expand=True)),imagehash.dhash(im.rotate(90, expand=True))]
                image_hash = [imagehash.phash(im), imagehash.phash(im), imagehash.phash(im)]
            elif algo ==1:
                image_hash = [imagehash.phash(im),imagehash.phash(im.rotate(90, expand=True)), imagehash.phash(im)]
            elif algo ==2:
                image_hash = [imagehash.phash(im, highfreq_factor=6),imagehash.phash(im.rotate(90, expand=True), highfreq_factor=6), imagehash.phash(im)]
            else:
                image_hash = [imagehash.phash(im.rotate(90, expand=True)),imagehash.dhash(im.rotate(90, expand=True)), imagehash.phash(im)]
            '''
            image_hashes.append(image_hash)
            
            #print len(image_hash.hash),
    return images, image_hashes

def find_rel_images(images, image_hashes, diff_max = 12):
    
    indx, indy = 0, 0
    
    img_dups = {}
    
    for hashv1 in image_hashes:
        #print images[indx]
        indy = 0
        for hashv2 in image_hashes:
            hash_diff = (hashv1[0] - hashv2[0]) + (hashv1[1] - hashv2[1]) + (hashv1[2] - hashv2[2])
            avg_diff = float(hash_diff)/3.0
            if 0 < avg_diff <= diff_max:
                img_dups.setdefault(images[indx], []).append(images[indy])
        #        print "\t {:35s} {:02d} {:02d} {:2.2f}".format(images[indy], hashv1[0] - hashv2[0], hashv1[1] - hashv2[1], avg_diff)
            indy = indy+1
            #print '{0:2d}'.format(avg_diff),
        indx += 1

    return img_dups

def find_hash_diffs(image_hashes):
    
    diff_matrix = []
    
    for img_hash1 in image_hashes:
        diff_row = []
        for img_hash2 in image_hashes:
            hash_diff = (img_hash1[0] - img_hash2[0]) + (img_hash1[1] - img_hash2[1]) + (img_hash1[2] - img_hash2[2])
            avg_diff = float(hash_diff)/3.0
            diff_row.append(avg_diff)
        diff_matrix.append(diff_row)
        
    return diff_matrix

#images, image_hashes = scan_and_hash('code\images')
#print find_hash_diffs(image_hashes)

#pprint.pprint(find_rel_images(images, image_hashes))