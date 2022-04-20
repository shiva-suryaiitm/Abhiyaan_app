1) I have written two two turtlesim python prgms to describe onebody revolving stationary planet and two bodies.

2) Concept used :
        F = alpha / d^2.
        All bodies have mass 1kg.
        F has two components fx and fy by that Vx and Vy are calculated.
        Fx and Fy are calculated using basic elemntary level trig.
        V is calculated using the formula V = a*t ; assuuming body didn't moved that much during the time period , so the force is almost const.
        Then Vavg during the whole time period is ( 1/2 * a * t ) and it is given as the velocity of the turtle.
        By this way almost gravity can be animated.(approxmation techniques xD)
        
        cons :
          During high speed like when the objects are closer this fails because F is not almost constant during the time.
          So I added a atatement:
                      if d<0.9 :
                        Vx = Fx * 0.0055 (Which increases the speed by 10%)
          I tried to increasing the rospy.Rate() by it resulted in queueing ig , so the results are worse
          I find out the optimal Rate is 100 hz.
          So when they are close to eachother their orbits kind of changes and goes outside.
          
 3) Optimal values of alpha , intial_Vx , intila_Vy For two body system : ( PLS see this sec to give better initial conditions to see a ellipse or circle )
          
          * alpha give around 2 - 4.
          * Intial_Vy give zero(0).
          * give Intial Vx as 0.1 to 0.4 for turtle 1.
          * give Intial Vx as -0.1 to -0.4 for turtle 2. ( Give as 0.1 & -0.1 or 0.2 & -0.2 like that positive  value for one turtle and same value neg for other turtle)
          
