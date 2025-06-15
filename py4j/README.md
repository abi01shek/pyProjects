# Integrating python with RumbleDB

RumbleDB is in Java and we want to be able to write python programs that interact with RumbleDB classes. For this we can use py4j library.


## Setup
### RumbleDB
https://rumble.readthedocs.io/en/latest/Getting%20started/

Download the rumbleDB standalone jar. The jar file will be used in compilation step later

### Py4j
Installing Py4j: https://www.py4j.org/install.html#install-instructions

The py4j jar file will also be used in compilation step later



## General methodology
You have a java class with its set of methods. You want to be able to access an instance of this class (and its methods) in python. This is made possible my py4j.

To achieve this, we have to create another Java class called the entry-point where we create an instance of the java class you want to access. The entry-point class has methods to return this instance as well as a main method which starts a py4j gateway server. Once the gateway server is running, your python script can access the java instance.


## Getting started
A simple example of a Stack java class, whose instance is accessed in python. The python script gets an instance of the stack class and pushes and pops items into it.

This is adapted from standard examples provided in py4j.

1. Stack class: py4j.examples/Stack.java
2. Entry-point class: py4j.examples/StackEntryPoint.java
3. Python script accessing java instance: test.py

### Steps to run
1. Compile both stack and entry-point classes
```bash
javac -classpath ".:<path/to/py4j.jar>" -d . ./py4j.examples/*.java
```
alternatively modify the file `compile.bash` and run

2. Launch the entry-point gateway server
```bash
java -classpath ".:<path/to/py4j.jar>" py4j.examples.StackEntryPoint
```
alternatively modify the file `launch_gateway_server.sh` and run

3. Run python test
```bash
python3 ./test.py
```


## Rumble integration
This is a simple example of accessing a Rumble class instance in python and running queries.
Note: Both py4j and rumble standalone JARs are needed.

1. Rumble class: This is part of the rumbleDB jar
2. RumbleEntryPoint class: This is the entry-point class which creates a Rumble instance and provides python access to it.
3. rumble_test.py: The python code that passes queries to Rumble instance for it to evaluate and collects its results

### Steps to run
1. Compile the entry-point gateway server
```bash
javac -classpath ".:<path/to/py4j.jar>:<path/to/rumbledb-1.23.0-standalone.jar>" -d . ./RumbleEntryPoint.java

```
Alternatively modify and run `compile.bash`

2. Launch the entry-point gateway server
```bash
java -classpath ".:<path/to/py4j.jar>:<path/to/rumbledb-1.23.0-standalone.jar>" RumbleEntryPoint

```

3. Run python test
```bash
./rumble_test.py
```
