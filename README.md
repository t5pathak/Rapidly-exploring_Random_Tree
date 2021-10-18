# RRT - Rapidly-exploring Random Tree

A Rapidly-exploring Random Tree (RRT) is a data structure and algorithm that is designed for efficiently searching (or navigating) high-dimensional spaces. RRTs are constructed incrementally in a way that quickly reduces the expected distance of a randomly-chosen point to the tree. RRTs are particularly suited for path planning problems that involve obstacles and differential constraints (non-holonomic). The obstacle map is shown below: 

<img width="702" alt="Map" src="https://user-images.githubusercontent.com/44245211/137796938-85075a3d-15bb-4bc2-9f41-fce2d35f9868.png">

# RRT Holonomic: Outline of the Code
1. Start with the robot’s initial point as the node present in the RRT.
2. Do till all the available free spaces are added in the RRT:
- - 2.1 Find a random location in the configuration space. Here the configuration space is the (x, y) point on the image. Let's name this np_q_rand.
- - 2.2 Find the nearest node in the RRT based on Euclidean distance. Let's name this np_q_near.
- - 2.3 Let’s move along the direction given by (np_q_rand - np_q_near) by 10 steps starting from np_q_near. The
function compute_motion_primitive does this for us. And this function returns the path moved by the
mid-platform, left wheel and right wheel.
 - - 2.4 Check the validity of this path i.e. check whether this path has collided or not.
 - - 2.5 If a collision has occurred, go back to step 2. Else proceed to the next step.  
 - - 2.6 Add the final location of this path to the RRT.
 - - 2.7 Show the frame where this path is added to the image.
 - - 2.8 If this added node is in the locality of the robot’s final point, then break out of this loop.
3. Path Tracing: Path is traced from destination back to source using the parent pointer of the node.

# RRT Holonomic: Results
![h1](https://user-images.githubusercontent.com/44245211/137796960-f14f0819-2ead-46f8-ba0c-b61b415ce0a5.gif)
![h2](https://user-images.githubusercontent.com/44245211/137796964-5d089beb-08ba-4e8b-9bb3-7ff039e9d357.gif)
![h3](https://user-images.githubusercontent.com/44245211/137796966-a7d949ee-15c3-4ea4-b4f2-996c3ca6a469.gif)

# RRT Non-Holonomic: Outline of the Code

1. Start with the robot’s initial point as the node present in the RRT.
2. Do till all the available free spaces are added in the RRT:
 - - 2.1 Find a random location in the configuration space. Here the configuration space is the (x, y, theta) point on the image. Let's name this np_q_rand.
 - - 2.2 Find the nearest node in the RRT based on Euclidean distance and the achievable orientation (maximum steering angle is 30o). Let's name this np_q_near.
 - - 2.3 Let’s move along the direction given by (np_q_rand - np_q_near) by 10 steps starting from np_q_near. The function compute_motion_primitive does this for us. And this function returns the path moved by the mid-platform, left wheel and right wheel. While doing so, it ensures that the kinematic equations are followed.
 - - 2.4 Check the validity of this path i.e. check whether this path has collided or not.
 - - 2.5 If a collision has occurred, go back to step 2. Else proceed to the next step.
 - - 2.6 Add the final location of this path to the RRT.
 - - 2.7 Show the frame where this path is added to the image.
 - - 2.8 If this added node is in the locality of the robot’s final point, then break out of this loop.
3. Path Tracing: Path is traced from destination back to source using the parent pointer of the node.

# RRT Non-Holonomic: Results
![nh1](https://user-images.githubusercontent.com/44245211/137797006-31bd350b-5244-485c-9f73-99fa3125c89c.gif)
![nh2](https://user-images.githubusercontent.com/44245211/137797013-bcab0d48-c2bc-4d09-9f62-0f3ce0655e61.gif)
![nh3](https://user-images.githubusercontent.com/44245211/137797019-b1c7d713-a0ba-4a62-8998-0fbf0b797ca7.gif)

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

##### Big Thanks to Pratikkumar Bulani
