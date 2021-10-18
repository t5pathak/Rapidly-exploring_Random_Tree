# RRT - Rapidly-exploring Random Tree

A Rapidly-exploring Random Tree (RRT) is a data structure and algorithm that is designed for efficiently searching (or navigating) high-dimensional spaces. RRTs are constructed incrementally in a way that quickly reduces the expected distance of a randomly-chosen point to the tree. RRTs are particularly suited for path planning problems that involve obstacles and differential constraints (non-holonomic). The obstacle map is shown below:


# RRT Holonomic: Outline of the Code
- Start with the robot’s initial point as the node present in the RRT.
- Do till all the available free spaces are added in the RRT:
- - Find a random location in the configuration space. Here the configuration space is the (x, y) point on the image. Let's name this np_q_rand.
- - Find the nearest node in the RRT based on Euclidean distance. Let's name this np_q_near.
- - Let’s move along the direction given by (np_q_rand - np_q_near) by 10 steps starting from np_q_near. The
function compute_motion_primitive does this for us. And this function returns the path moved by the
mid-platform, left wheel and right wheel.
 - - Check the validity of this path i.e. check whether this path has collided or not.
 - - If a collision has occurred, go back to step 2. Else proceed to the next step.  
 - - Add the final location of this path to the RRT.
 - - Show the frame where this path is added to the image.
 - - If this added node is in the locality of the robot’s final point, then break out of this loop.
- Path Tracing: Path is traced from destination back to source using the parent pointer of the node.

# RRT Holonomic: Results


# RRT Non-Holonomic: Outline of the Code

- Start with the robot’s initial point as the node present in the RRT.
- Do till all the available free spaces are added in the RRT:
 - - Find a random location in the configuration space. Here the configuration space is the (x, y, theta) point on the image. Let's name this np_q_rand.
 - - Find the nearest node in the RRT based on Euclidean distance and the achievable orientation (maximum steering angle is 30o). Let's name this np_q_near.
 - - Let’s move along the direction given by (np_q_rand - np_q_near) by 10 steps starting from np_q_near. The function compute_motion_primitive does this for us. And this function returns the path moved by the mid-platform, left wheel and right wheel. While doing so, it ensures that the kinematic equations are followed.
 - - Check the validity of this path i.e. check whether this path has collided or not.
 - - If a collision has occurred, go back to step 2. Else proceed to the next step.
 - - Add the final location of this path to the RRT.
 - - Show the frame where this path is added to the image.
 - - If this added node is in the locality of the robot’s final point, then break out of this loop.
- Path Tracing: Path is traced from destination back to source using the parent pointer of the node.

# RRT Non-Holonomic: Results


# Directory Structure
- ```src``` folder contains the source code. 
- ```results``` folder contains the outputs obtained for different number of obstacles and different start and goal points
 
# Running the code
Any changes which need to be made, must be made in the code block under the heading "Main" only

1. Open your software of choice (Google Colab, Jupyter Notebook etc.)
2. Navigate to ```src``` folder. (If using Google Colab, upload the file inside ```src``` from your local PC to the colab repository)
3. Load the file
4. Run the file
5. If you want to make any changes to things like number of robots, goal point of robots, where to save the outputs, whether you want to save outputs or not etc., make necessary changes in the cell block under the heading "Main". The cell block is self-explanatory.
6. Install any necessary libraries if needed

# To save the output
- In the cell block under the heading "Main", make changes to the line where ```solver``` function is called. Instructions regarding how the changes required can be understood by reading the function documentation.
- **Note:** Please make sure that an empty directory exists at the path given to the program to save outputs
