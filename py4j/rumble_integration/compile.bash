#!/usr/bin/bash
# https://www.py4j.org/install.html#install-instructions
# pip install py4j
# Download rumbledb standalone: https://rumble.readthedocs.io/en/latest/Getting%20started/
javac -classpath ".:/usr/local/share/py4j/py4j0.10.9.9.jar:/home/everglade/Downloads/rumbledb-1.23.0-standalone.jar" -d . ./*.java
