#!/usr/bin/python

import argparse


p = argparse.ArgumentParser()

p.add_argument('--test',  action='store_true', help='Verify Denavit-Hartenberg for two link case')
p.add_argument('--train', action='store_true', help='Train network to learn IK')
p.add_argument('--infer', action='store_true', help='Run inference test on existing network model')

args = p.parse_args()

if args.test:
    import test.test as Test
    Test.Test().test()

if args.train:
    import src.train as Train
    Train.Train().train()

if args.infer:
    import src.infer as Infer
    Infer.Infer().infer()


