Hi reviewer, thank you for your time.
In the early stage of the project I´ve considered going for a multiprocessing structure, but since the data needs to be aggregated
we would have a lot of overhead due to the needed sharing of data between the processes to make calculations. 
I've then decided to go for multithreading to make use of a secondary thread to query the db. Since the data can only change every 
5s querying the db every 250ms seems to be accurate enough instead querying on each line of data parsed. 
I've profiled my project with scalene (https://github.com/plasma-umass/scalene), which I've also used to monitor a second implementation 
done with numpy (left commented in the code), that did not yeld yet major time savings on my machine. 
Instead of implementing tests I decided to use the time to create a larger dataset on which smaller changes could reflect better, 
but the results where inconsistent from run to run so I could not draw any conclusions from that.
Also numpy would be great to subdivide the input data in blocks and target the sweetspot by using as much memory as possibile at once.
I'm not aware of what the standard of speed is for executing a task like this, but I'm sure more can be achieved by delving in libraries 
that take full advantage of the underling C speed. For the DB I've used postgresql, but having performance in mind, in a future iteration
Redis would also be a solid choice to access the price modifier faster.

