"""
Integrating python with RumbleDB
RumbleDB:  https://rumble.readthedocs.io/en/latest/Getting%20started/
Prerequisites: py4j and rumble-standalone JARs.
"""

# Steps
# Compile the entry point Java class: ./compile.bash
# Launch py4j gateway server: ./launch_gateway_server.sh
# Run test: python3 ./rumble_test.py

from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
rumble = gateway.entry_point.getRumble()

# REPL
while(True):
    query_input = input("Enter a query (ex: 1+1) or q to quit: ")
    if(query_input == "q"):
        break
    # Run Rumble query: results are stored in a Rumble sequence java object
    sequence = rumble.runQuery(query_input);

    # Iterate through the sequence java object and collect the results into a list
    # we need a java list because the populateList() method requires a java list as input
    results_list = gateway.jvm.java.util.ArrayList()
    if(not sequence.availableAsRDD()):
        sequence.populateList(results_list)

        # Print the results in python
        for result in results_list:
            print(result.getStringValue())
