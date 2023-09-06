Prerequisites:

You'll need Python installed on your system.
Install Mininet, a network emulation tool, using the following command:

```sudo apt-get install mininet```


Explanation:

1. In this code example, we import the necessary modules from Mininet to set up an SDN network.
2. We create a Mininet network object net and add an SDN controller (c0) along with two switches (s1 and s2) and two host nodes (h1 and h2).
3. We establish links between switches and hosts to create the network topology.
4. The start method is used to start the network, and we add the switches to the controller.
5. We open an xterm terminal for each host node to demonstrate network communication.
6. The Mininet command line interface (CLI(net)) is run, allowing you to interact with the network.
7. Finally, we stop the network using net.stop().