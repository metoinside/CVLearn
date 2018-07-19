It is a very simple algorithm to detect faces with 20-lines of code.

Opens your webcam to acquire images then loads the haarcascade_frontalface_default.xml which also can be found in opencv/data/haarcascades

In an infinite loop, algorithm searches for the faces in the grayscale of image. It draws the rectangle after it founds.

Program quits if you hit the esc.
