# Neural Network Kinematics

This project seeks to train a neural network to perform inverse kinematics for rigid body link chains.  This
is by no means a new idea, and it is a discipline where there are in many cases both iterative and
closed-form solutions.  More generally, this is a study of minimizing error using neural networks 
on arbitrary nonlinear mappings.  



### Existing Work

There are a number of works focusing on neural networks for robotic kinematics and inverse kinematics:

  * [A study of neural network based inverse kinematics solution for a three-joint robot](https://pdfs.semanticscholar.org/9062/8e6b996060cebfa2f1d3c02326e538aa913f.pdf)

  * [A New Artificial Neural Network Approach in Solving Inverse Kinematics of Robotic Arm](http://downloads.hindawi.com/journals/cin/2016/5720163.pdf)

  * [Approximation of the Inverse Kinematics of a Robotic Manipulator Using a Neural Network](http://www.ros.hw.ac.uk/bitstream/handle/10399/2265/DinhBH_0709_eps.pdf?sequence=1)

  * [Artificial Neural Network Based Forward Kinematics Solution for Planar Parallel Manipulators Passing through Singular Configuration](https://www.omicsonline.org/open-access/artificial-neural-network-based-forward-kinematics-solution-for-planar-parallel-manipulators-passing-through-singular-configuration-2168-9695.1000106.pdf)

  * [Direct kinematics solution of 3-RRR robot by using two different artificial neural networks](http://ieeexplore.ieee.org/document/7367852/)

Another interesting and relevant investigation is the work of Rolnick and Tegmark on natural 
function expression, and augmented by Lin on why deep learning works as well as it does:

  * [The power of deeper networks for expressing natural functions](The power of deeper networks for expressing natural functions.pdf)

  * [Why does deep and cheap learning work so well?](https://arxiv.org/pdf/1608.08225.pdf)



### Methodology

The robot kinematics studied here is an RRR robot.  The homogeneous transformations, based on
Denavit-Hartenberg parameterization, is used to determine the Cartesian position of the end 
effector based on the joint angles.  



### Software Results



### Physical Robot Results

