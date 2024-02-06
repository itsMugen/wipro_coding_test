Hi reviewer thank you for your time.
I've decided to go for multithreading early in the project since it seems that the data needs to be aggregate with
previous data and with multiprocessing we would have a lot of overhead due to the sharing of data to make calculations. 
As of now a secondary thread is used to query the db, since the data can only change every 5s querying the db every 250ms seems 
to be accurate enough instead querying on each line of data parsed. 
I've profiled my project with scalene but due to time constraints an implementation
which takes advantage of numpy did not yeld yet major time savings. Instead of implementing tests I decided to use the time to
create a larger dataset on which smaller changes could reflect better but the results where inconsistent from run to run so I could
not draw any conclusions from that.
Also numpy would be great to suddivide in blocks the input data and target the sweetspot by using as much memory as possibile at once.
I'm not sure of what the standard of speed is but I'm sure more can be achieved by delving in libraries that take full advantage
of the underling C speed. For the DB I've used postgresql but having speed in mind in a future iteration, Redis would also be a
solid choice to access faster the price modifier.

