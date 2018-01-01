# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 15:23:07 2017

@author: prasad.varma
"""

import hashtest
import pprint


def culsterize_dict(similar_dict):
    
    cluster_list = []

    for index_img, cur_list  in similar_dict.items():
        
        cur_list.append(index_img)
        
        clust_len = len(cluster_list)
        flag_found = 0
        
        for i in range(clust_len):

            cluster_item = cluster_list[i]

            if any((True for x in cluster_item if x in cur_list)):
                cluster_list[i] = list(set(cluster_item) | set(cur_list))
                flag_found = 1
        
        if not flag_found:
            cluster_list.append(cur_list)
        
    return cluster_list

images, image_hashes = hashtest.scan_and_hash('D:\\SNAPBCK\\Rameswaram')

rel_images_dict = hashtest.find_rel_images(images, image_hashes,diff_max = 15)

clusters = culsterize_dict(rel_images_dict)

pprint.pprint(clusters)

