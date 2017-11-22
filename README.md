# Neural Network Kinematics

This project seeks to train a neural network to perform inverse kinematics for rigid body link chains.  This
is by no means a new idea, and it is a discipline where there are in many cases both iterative and
closed-form solutions.  More generally, this is a study of minimizing error using neural networks 
on arbitrary nonlinear mappings.  The general goal is to better understand training the inverse mapping
using only the forward mapping, which entails understanding the best network model for approximating
functions that may have singularities in the mapping.  



### Existing Work

There are a number of works focusing on neural networks for robotic kinematics and inverse kinematics:

  * [A study of neural network based inverse kinematics solution for a three-joint robot](https://pdfs.semanticscholar.org/9062/8e6b996060cebfa2f1d3c02326e538aa913f.pdf)

  * [A New Artificial Neural Network Approach in Solving Inverse Kinematics of Robotic Arm](http://downloads.hindawi.com/journals/cin/2016/5720163.pdf)

  * [Approximation of the Inverse Kinematics of a Robotic Manipulator Using a Neural Network](http://www.ros.hw.ac.uk/bitstream/handle/10399/2265/DinhBH_0709_eps.pdf?sequence=1)

  * [Artificial Neural Network Based Forward Kinematics Solution for Planar Parallel Manipulators Passing through Singular Configuration](https://www.omicsonline.org/open-access/artificial-neural-network-based-forward-kinematics-solution-for-planar-parallel-manipulators-passing-through-singular-configuration-2168-9695.1000106.pdf)

  * [Direct kinematics solution of 3-RRR robot by using two different artificial neural networks](http://ieeexplore.ieee.org/document/7367852/)


In this study I am using a 3R robot.  The rigid body mechanics are well studied, but there
are focus articles relating to space division on the basis of the 3R singularity set that 
are relevant to understanding the style of manifold we intend to learn:

  * [A classification of 3R regional manipulator singularities and geometries](http://ieeexplore.ieee.org/document/132033/)

  * [Guaranteed detection of the singularities of 3R robotic manipulators](http://perso-laris.univ-angers.fr/~delanoue/article/ms-7-31-2016.pdf)

  * [Classification of one family of 3R positioning Manipulators](https://arxiv.org/pdf/0705.1344.pdf)


Another interesting and relevant investigation is the work of Rolnick and Tegmark on natural 
function expression, and augmented by Lin on why deep learning works as well as it does:

  * [The power of deeper networks for expressing natural functions](https://arxiv.org/pdf/1705.05502.pdf)

  * [Why does deep and cheap learning work so well?](https://arxiv.org/pdf/1608.08225.pdf)



### Methodology

The robot kinematics studied here is a 3R robot.  Why 3R?  Mainly because I have an industial 6R 
and believe the waist-shoulder-elbow aspect is a good exercise for inverse kinematics.  It is also 
handy given the abundance of inexpensive servo-driven 3R robotics models that are available, lending 
itself simple for anyone to independently verify the results on physical hardware.  Additionally, 3R 
robots admit a slightly more rich set of singularities than robots like the Stanford arm and Cartesian 
(gantry) robots, and the forward and inverse kinematics have well known analytic solutions.

In this work I am using the Denavit-Hartenberg convention for computing the composite homogeneous
transformation.  For training, I am strictly using the forward kinematics to produce a set of 
features (Cartesian position of the end effector) and labels (joint angles).  Why using the forward
kinematic mapping rather than the inverse kinematics that would result in more consistent sampling from
the desired Cartesian end effector space?  Because the ultimate goal is to be able to actuate a 
robot without knowledge of how to find a closed form inverse mapping and understand how to create and train
a model that provides acceptable accuracy.



### Code

First, make sure all your libs are up to date:

```
pip -r requirements.txt
```



### Software Results



### Physical Robot Results

