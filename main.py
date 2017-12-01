#!/usr/bin/python

import argparse


p = argparse.ArgumentParser()

p.add_argument('--test',  action='store_true', help='Verify Denavit-Hartenberg for two link case')
p.add_argument('--train', action='store_true', help='Train network to learn IK')
p.add_argument('--infer', action='store_true', help='Run inference test on existing network model')
p.add_argument('--table', action='store_true', help='Produce table of determinant values')
p.add_argument('--ik',    action='store_true', help='Run inverse kinematic test using sympy solver')

args = p.parse_args()

if args.test:
    import tests.test as Test
    Test.Test().test()

if args.train:
    import src.train as Train
    Train.Train().train()

if args.infer:
    import src.infer as Infer
    Infer.Infer().infer()

if args.table:
    import tests.table as Table
    Table.Table().table()

if args.ik:
    import tests.ik as IK
    IK.IK().ik()
