#!/usr/bin/env python3


def main():
	import warnings
	warnings.filterwarnings("ignore")

	import os
	os.environ['CUDA_VISIBLE_DEVICES'] = '0'
	import json

	import torch
	import torch.nn as nn
	import torch.nn.functional as F
	import PIL.Image
	import numpy as np
	import matplotlib.pyplot as plt
	from scipy.io import loadmat
	from scipy.misc import imresize

	### Access PRM through [Nest](https://github.com/ZhouYanzhao/Nest)

	from nest import modules, run_tasks

	### Train a PRM-augmented classification network using image-level labels

	run_tasks('/home/ubuntu/ebs/ruizhe/CountSeg/train/config_counting_coco14.yml')

if __name__ == "__main__":
    main()


