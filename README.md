# Neural Network Kinematics

This project seeks to train a neural network to perform inverse kinematics for rigid body link chains.  This
is by no means a new idea, as a trained solution to relatively complex nonlinear equations has been desired 
for decades.  As well, it is a discipline where there are in many cases both iterative and
closed-form solutions.  More generally, this is a study of minimizing error using neural networks 
on arbitrary nonlinear mappings.  



### Background

There are three fairly common ways to perform inverse kinematics for rigid link robots:

_Closed Form Solutions_ These are explicit solutions solving the inverse kinematics.  These solutions evaluate
very quickly and are very accurate, but can suffer the inability to be computed for suitably complex 
robotic systems.  Moreover, additional logic may be required because there may be more than one solution, whence
choosing the context of the solution is important.  The Jacobian is also closed form in these solutions,
so there is an explicit knowledge of the manipulabity and associated joint angular velocity situations that 
are important for practical robots.  Bottom line is the types of robots that closed form solutions are relevant
to are limited, but the precision and controlability is high.  These solutions are seen in precision industrial
and manufacturing robots.

_Iterative Solutions_ In this case the forward kinematics are well known, but the inverse kinematics are more
challenging to solve for explicitly.  The Jacobian is often still known, so the manipulability and practical concerns
for joint angular velocity are often known.  The problem is that it is often unknown how long the solution will take
to calculate, as it depends on the specific equations being solved, where on the manifold the solution lies, 
what the initial guess is, etc.  While this method offers precisions, it isn't always appropriate since there is
no guarantee of the timeframe for a solution, or if the solver will find a solution (e.g. problem conditioning).  This
type of solution is more commonly seen in unusually complex rigid body robots where there is no constrain on
the time required to solve for the joint angles.

_Neural Network Solutions_ In this case a neural network is used to learn the inverse kinematics based on forward
kinematic training.  The Jacobian can be known, but may not be integral to the concept of a solution.  The 
idea is that this form of solution offers more flexibility (ability to resolve multiple possible solutions by 
using training from forward kinematics) with a consistent evaluation time at the expense of precision.  Since the
Jacobian itself is not part of the training, it can still be used for determining manipulability and angular
joint velocity, though this is not part of the main idea of the technique.  Since this type of solution does not
offer high accuracy, it is not a solution that would be found in industrial and manufacturing robots.  However,
for classes of robots that do not require precision, and for which manipulability may not be of paramount
importance, this type of solution is quite flexible in that only the forward kinematics needs to be known.  Since
this is not of relevance to most industrial problems, it might not be considered a common solution.



### Goals

The general goal of this project is somewhat academic in that it is an avenue for me to learn about practical
implementation challenges involving all of the techniques.  Moreover, there is an aspect of it related to 
creating my own library for kinematics.  In the context of the stated objective regarding the use of neural
networks for inverse kinematics solvers, the goal is to understand network structures that work best for 
inferring the inverse kinematics based on forward kinematic training, particularly in singular areas.



### Existing Work

There are a number of works focusing on neural networks for robotic kinematics and inverse kinematics, both using
generic multiple layer perceptron networks as well as radial basis function networks:

  * [A study of neural network based inverse kinematics solution for a three-joint robot](https://pdfs.semanticscholar.org/9062/8e6b996060cebfa2f1d3c02326e538aa913f.pdf)

  * [A New Artificial Neural Network Approach in Solving Inverse Kinematics of Robotic Arm](http://downloads.hindawi.com/journals/cin/2016/5720163.pdf)

  * [Approximation of the Inverse Kinematics of a Robotic Manipulator Using a Neural Network](http://www.ros.hw.ac.uk/bitstream/handle/10399/2265/DinhBH_0709_eps.pdf?sequence=1)

  * [Comparison of RBF and MLP neural networks to solve inverse kinematic problem for 6R serial robot by a fusion approach](http://www.sciencedirect.com/science/article/pii/S0952197610000692) 
  
  * [Comparison of neural network architectures for the modeling of robot inverse kinematics](http://ieeexplore.ieee.org/document/845423/)
  
  * [RBF networks-based inverse kinematics of 6R manipulator](https://link.springer.com/article/10.1007/s00170-003-1988-0)


There are also some peripherally useful articles having to do with planar and 3-RRR robot configurations:

  * [Artificial Neural Network Based Forward Kinematics Solution for Planar Parallel Manipulators Passing through Singular Configuration](https://www.omicsonline.org/open-access/artificial-neural-network-based-forward-kinematics-solution-for-planar-parallel-manipulators-passing-through-singular-configuration-2168-9695.1000106.pdf)

  * [Direct kinematics solution of 3-RRR robot by using two different artificial neural networks](http://ieeexplore.ieee.org/document/7367852/)
  
  * [Solution to the inverse kinematics problem in robotics by neural networks](http://ieeexplore.ieee.org/document/23979/)
  
  * [Comparison of inverse kinematics solutions using neural network for 6R robot manipulator with offset](http://ieeexplore.ieee.org/document/1662342/)
  
  * [A study of generalization ability of neural network for manipulator inverse kinematics](http://ieeexplore.ieee.org/document/239161/)


There are also several books pertaining to control theory that cover neural network solutions.

In this study I am using a 3R robot.  The rigid body mechanics are well studied, and there
are focus articles relating to space division on the basis of the 3R singularity set that 
are relevant to understanding the style of manifold we intend to learn:

  * [Singularity avoidance of a six degree of freedom three dimensional redundant planar manipulator](http://www.sciencedirect.com/science/article/pii/S0898122111011448)

  * [Singular Configurations of Wrist-Partitioned 6R Serial Robots: a Geometric Perspective for Users](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.88.1735&rep=rep1&type=pdf)

  * [A classification of 3R regional manipulator singularities and geometries](http://ieeexplore.ieee.org/document/132033/)

  * [Guaranteed detection of the singularities of 3R robotic manipulators](http://perso-laris.univ-angers.fr/~delanoue/article/ms-7-31-2016.pdf)

  * [Classification of one family of 3R positioning Manipulators](https://arxiv.org/pdf/0705.1344.pdf)


Another interesting and relevant investigation is the work of Rolnick and Tegmark on natural 
function expression, and augmented by Lin on why deep learning works as well as it does:

  * [The power of deeper networks for expressing natural functions](https://arxiv.org/pdf/1705.05502.pdf)

  * [Why does deep and cheap learning work so well?](https://arxiv.org/pdf/1608.08225.pdf)


The reason for the inclusion of this should be clear -- we are attempting to learn a manifold, hence the 
representations that are learnable for the manifold is of crucial importance.  



### Methodology

The robot kinematics studied here is for a 3R robot.  Simplicity and I have an industrial 6R that I can
use, but moreover it is handy given the abundance of inexpensive servo-driven 3R robotics models that 
are available, lending itself simple for anyone to independently verify the results on physical 
hardware.  3R robots admit a slightly more rich set of singularities than robots like the Stanford arm 
and Cartesian (gantry) robots, and the forward and inverse kinematics have well known analytic solutions.

In this work I am using the Denavit-Hartenberg convention for computing the composite homogeneous
transformation.  For training, I am strictly using the forward kinematics to produce a set of 
features (Cartesian position of the end effector) and labels (joint angles).  Why using the forward
kinematic mapping rather than the inverse kinematics that would result in more consistent sampling from
the desired Cartesian end effector space?  Because the ultimate goal is to be able to actuate a 
robot without knowledge of how to find a closed form inverse mapping and understand how to create and train
a model that provides acceptable accuracy.

The general notion of the Denavit-Hartenberg convention used in this code is expressed in this link
diagram:

![Denavit-Hartenberg Parameters](/img/dh_params.png)

After establishing a link chain based on the Denavit-Hartenberg parameters, a composite homogeneous
transformation is produced.  Summary information about the transformation and the Jacobian
are provided.  The transformation is also evaluated to train the network.




### Code

First, make sure all your libs are up to date:

```
pip -r requirements.txt
```


There are a number of commands that can be invoked through the `main.py` program in the root of 
the project.  These include:

  * `--test` Demonstrates the homogeneous transformation matrix for a two link planar robot (testing for the chain)

  * `--train` Trains the network based on the model and parameters for the generator

  * `--infer` Runs an inference pass using the model previously generated

  * `--table` Produces Jacobian and determinant values

  * `--ik` Computes all symbolic inverse solutions and verifies them through forward transform using `sympy`


The main objective is that the model used for training results in an inference test that is favorable.  The other
commands are mainly for testing and to validate the Denavit-Hartenberg part of the problem.

The model can be found in `src/model.py`, the generator is in `/src/generator.py` and the specifics of training
the network can be found in `src/train.py`.



### Software Results



### Physical Robot Results

