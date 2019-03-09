#######################
Python Standard Library
#######################

Python standard library package containing data structures and algorithms.

Installing stdlib package
-----------------------------

The stdlib is packaged so it's easy to install via pip::

    pip3 install stdlib

Getting Started
---------------

Standard Library contains a variety of different tools to allow you to build whatever you need
using simple to complex data structures and algorithms

Once you've installed the package, you can import modules like normal

Example::

    from stdlib.ds.linear.bag import Bag
    from stdlib.sort.quickx import QuickX

    bag = Bag()
    bag.add(0)
    bag.add(10)
    bag.add(3)
    bag.add(6)

    print("Before quick sort on our bag")
    for item in bag:
        print(item)

    print("After quick sort")
    QuickX.sort(bag)

    for item in bag:
        print(item)

Development
-----------

See CONTRIBUTING for instructions on how to begin contributing and setup a development environment
