#!/usr/bin/env python
# coding: utf-8

# Q1. What is multiprocessing in python? Why is it useful?

# Multiprocessing in Python is a built-in package that allows the system to run multiple processes simultaneously. It will enable the breaking of applications into smaller threads that can run independently. The operating system can then allocate all these threads or processes to the processor to run them parallelly, thus improving the overall performance and efficiency.

# Performing multiple operations for a single processor becomes challenging. As the number of processes keeps increasing, the processor will have to halt the current process and move to the next, to keep them going. Thus, it will have to interrupt each task, thereby hampering the performance.
# 
# You can think of it as an employee in an organization tasked to perform jobs in multiple departments. If the employee has to manage the sales, accounts, and even the backend, he will have to stop sales when he is into accounts and vice versa.
# 
# Suppose there are different employees, each to perform a specific task. It becomes simpler, right? That’s why multiprocessing in Python becomes essential. The smaller task threads act like different employees, making it easier to handle and manage various processes. A multiprocessing system can be represented as:
# 
# A system with more than a single central processor
# A multi-core processor, i.e., a single computing unit with multiple independent core processing units
# In multiprocessing, the system can divide and assign tasks to different processors.

# Q2. What are the differences between multiprocessing and multithreading?

# While multithreading and multiprocessing can both be used to increase the computing power of a system, there are some key differences between these approaches. Here are some of the primary ways these methods differ from one another:
# 
# Multiprocessing uses two or more CPUs to increase computing power, whereas multithreading uses a single process with multiple code segments to increase computing power.
# Multithreading focuses on generating computing threads from a single process, whereas multiprocessing increases computing power by adding CPUs.
# Multiprocessing is used to create a more reliable system, whereas multithreading is used to create threads that run parallel to each other.
# multithreading is quick to create and requires few resources, whereas multiprocessing requires a significant amount of time and specific resources to create.
# Multiprocessing executes many processes simultaneously, whereas multithreading executes many threads simultaneously.
# Multithreading uses a common address space for all the threads, whereas multiprocessing creates a separate address space for each process.
# Related: C# vs. Python: Choosing the Right Programming Language
# Benefits of multithreading
# Here are some of the key benefits of multithreading:
# 
# It requires less memory storage.
# Accessing memory is easier since threads share the same parent process.
# Switching between threads is fast and efficient.
# It's faster to generate new threads within an existing process than to create an entirely new process.
# All threads share one process memory pool and the same address space.
# Threads are more lightweight and have lower overhead.
# The cost of communication between threads is relatively low.
# Creating responsive user interfaces (UIs)

# Q3. Write a python code to create a process using the multiprocessing module.

# In[5]:


from multiprocessing import Process


def print_func(continent='Asia'):
    print('The name of continent is : ', continent)

if __name__ == "__main__":  # confirms that the code is under main function
    names = ['America', 'Europe', 'Africa']
    procs = []
    proc = Process(target=print_func)  # instantiating without any argument
    procs.append(proc)
    proc.start()

    # instantiating process with arguments
    for name in names:
        # print(name)
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()


# Q4. What is a multiprocessing pool in python? Why is it used?

# Python Multiprocessing Pool: The Complete Guide
# AUGUST 26, 2022 by JASON BROWNLEE in POOL
# 
# The Python Multiprocessing Pool class allows you to create and manage process pools in Python.
# 
# Although the Multiprocessing Pool has been available in Python for a long time, it is not widely used, perhaps because of misunderstandings of the capabilities and limitations of Processes and Threads in Python.
# 
# This guide provides a detailed and comprehensive review of the Multiprocessing Pool in Python, including how it works, how to use it, common questions, and best practices.

# Q5. How can we create a pool of worker processes in python using the multiprocessing module?

# Multiprocessing Pool Number of Workers in Python
# JUNE 29, 2022 by JASON BROWNLEE in POOL
# 
# You can configure the number of workers in the multiprocessing.pool.Pool via the “processes” argument.
# 
# In this tutorial you will discover how to configure the number of worker processes in the process pool in Python.
# 
# Let’s get started.
# 
# Skip the tutorial. Master the multiprocessing Pool today. Learn how
# 
# Table of Contents
# Need to Configure the Number of Worker Processes
# How to Configure The Number of Workers
# Check the Default Number of Workers
# Example of Configuring The Number of Workers
# Common Questions
# What is a CPU and What is a CPU Core?
# What are Physical CPUs vs Logical CPUs?
# What is the Default Number of Processes in the Pool?
# How Many CPU Cores Do I Have?
# Should The Number of Processes in the Pool Match the Number of CPUs or Cores?
# How Many Processes Should I Use?
# What is the Maximum Number of Worker Processes in the Pool?
# Further Reading
# Takeaways
# Need to Configure the Number of Worker Processes
# The multiprocessing.pool.Pool in Python provides a pool of reusable processes for executing ad hoc tasks.
# 
# A process pool can be configured when it is created, which will prepare the child workers.
# 
# We can issue one-off tasks to the process pool using functions such as apply() or we can apply the same function to an iterable of items using functions such as map(). Results for issued tasks can then be retrieved synchronously, or we can retrieve the result of tasks later by using asynchronous versions of the functions such as apply_async() and map_async().
# 
# The process pool has a fixed number of worker processes.
# 
# It is important to limit the number of worker processes in the process pools to perhaps the number of logical CPU cores or the number of physical CPU cores in your system, depending on the types of tasks we will be executing.

# In[ ]:





# In[ ]:




