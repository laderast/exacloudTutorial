---
title: "Exacloud Workshop"
author: "Ted Laderas (laderast@ohsu.edu) and Ryan Swan"
date: "November 5, 2015"
output: pdf_document
---

##What is exacloud?

[Exacloud](http://exainfo.ohsu.edu) is OHSU's cluster computing environment. It currently has over 6000 CPUs of varying capabilities and memory that can be utilized by users who want to run parallel computing jobs.

However, to run jobs effectively on exacloud, you must understand some basic techniques and how exacloud works.

##Architecture of exacloud

Essentially, you can think of exacloud as divided into two different node types: the first is the *head* node, which is the node that you sign into initially into exacloud. The head node handles all of the scheduling and file transfer to the other nodes in the system. The other nodes are subservient cluster nodes.

You might wonder if you need to load all of your data onto each node that you run your jobs on. The short answer is no, because exacloud has a distributed filesystem called Lustre. Essentially when you copy a file onto Lustre, the file gets copied in such a way across nodes that it is easily accessible by each node. The drawback to Lustre is that it is currently difficult to maintain and is prone to data loss.

For this reason, do *not* use Lustre for long term storage of your data! It's better to transfer your files off of Lustre when you're done.

##Task 0: Getting onto exacloud and understanding the lustre filesystem

Before you can even start with exacloud, you need an exacloud login and password. You will need to talk with ACC for an account and password.

1. To connect with exacloud, use the ssh command and input your password when prompted:

```
ssh USERNAME@exacloud.ohsu.edu
```

2. Your entry point is the ACC filesystem, which is shared across all ACC machines (not just exacloud). You can run jobs from here, but you will run into space limitations (10 Gb limit). If you have larger data, it's much easier to use the lustre filesystem. So let's go to the lustre folder:

```
cd /home/exacloud/lustre1/[our folder name]
```

3. Make your own folder in the lustre folder. Copy the scripts, and example data into your folder.

```
mkdir [your user name]
cp 
```

##Task 1: Testing your code in an interactive session

We will be reproducing the following analysis using data pulled from the twitter feed: [On Geek Versus Nerd](https://slackprop.wordpress.com/2013/06/03/on-geek-versus-nerd/). We want to discover the words that co-occur with "nerd" and "geek" with high frequency.

**IMPORTANT:** Do not run jobs on the head node! You will be yelled at, and for good reason. The head node is a very busy node, handling job scheduling and file transfer for the entire cluster. If you run jobs on it, you essentially are slowing everyone else down.

Instead, you can test your jobs by opening up an interactive session on exacloud. Essentially, opening up an interactive session guarantees the use of a particular node on exacloud. You can run jobs in an interactive session on the command line, which is what we're are going to do.

1. Open an interactive session using condor_submit:
```
condor_submit -interactive
```
2. Take a look at the n-gram script ([]). What are the functions?
2. We will be testing out the n-gram counting script on the test data ('test.txt').
4. To leave your interactive session, use exit. Don't leave it just yet, as we'll use the interactive session to split up your file (Task 2)

##Task 2: Splitting up your problem

We'll be using the unix command split to split our 1 and 2-gram task up into 50 smaller tasks using the -n option. Using the -d option, the output of split will be x01,  

```
split --numeric-suffixes --lines=100000 training.1600000.processed.noemoticon.csv
```

###Extension: Using multiple directories to divide your jobs

If you have multiple files to process at a time, another alternative is to set up numbered directories where each file has the identical name.

##Task 3: Setting up your submit script to HTCondor

Look at "wcount.submit" using a text editor such as nano.

Exit the interactive session using `exit`. We need to be in the head node to now submit our script.

###Extension: Asking for machines with specific requirements

HTCondor has a 'classified' system that allows you to request specific processing and memory requirements for your job.

###Extension: Writing a script that writes a submit script

There are other ways to write submit scripts. For example, if your job requires cycling through a list of non-standard files that are not sequentially numbered, this is the best way to process them.

##Task 4: Running your Job on Exacloud

There are two commands that will be necessary to understand running jobs on exacloud: the first is `condor_submit`, which submits the job, and `condor_q`, which shows you current jobs running on exacloud.

##Task 5: Putting your results back together

##Task 6: Debugging

If you want to stop a job, you can use [condor_rm]

If your job seems slow, check the excaloud usage display at [http://exacloud.ohsu.edu/ganglia/](http://exacloud.ohsu.edu/ganglia/)
