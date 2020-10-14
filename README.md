# Zoom Class Manager
Input your schedule and when you run class.py it'll automatically open up the zoom link for your current/upcoming class automatically.

## Setup
For the time being it's a little messy in terms of functionality, but it does work. To set it up there is a little work you have to do.
* Make a file called input.txt, this is where you'll be putting the data to keep track of your classes.
* Each meeting will need it's own two lines, so if your class has a lab and a lecture, then that class will need 4 lines total.
  * On the first line, first you'll need to put the days that that section meets. This will almost certainly be different for your lab and lecture, so for your lab you'd only put the day(s) that it meets on, and for your lecture you'd only put the days that you have the lecture, don't combine them.
    * The way it's set right now is that m=Monday, t=Tuesday, w=Wednesday, r=Thursday, and f=Friday. Put all the days the class meets with no spaces in between.
  * After that, you'll put the times the class meets at, this is in the 24 hr format with no colon, so if your class is 11:30AM-1:20PM you'd put 1130 1320.
  * The final thing to put on the first line is the name of the class, it can be spaced out and capitalized however you want, so long as it is at the end of the first line.
  * The second line is just the zoom link, be warned that you have to make sure you have a link that isn't session based. 
    * If your professors share zoom links as the long announcement, that one works well, however if it's the page that just has the join button, I got it to work by joining outside of class time, then you go to a URL that simplifies and has #success at the end, copy that link but leave out the #success part and it should work.
  * There shouldn't be any empty lines, they should all either hold the class description, or the zoom link.
    * And just to reiterate it, in the line describing the class, there should be a space after the days it meets (mtwrf), a space after the start time, after the end time, and then you're free to use them as many spaces as you'd like in the class name.
* Now you're good to go, the first time you run class.py it'll generate output.json and use it, every time after that it'll use the one that's already been made. W
* Whenever you run class.py it should automatically open the zoom link in your browser for the right class, it'll tell you how long till the class if it hasn't started, or how much longer there is if it has. Simply hit enter/return to dismiss the terminal, as it waits for input to make sure you can read it.
