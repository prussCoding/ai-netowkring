from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.log import setLogLevel

def create_sdn_network():
    # Create a Mininet network
    net = Mininet(controller=Controller, switch=OVSKernelSwitch)

    # Create SDN controllers
    c0 = net.addController("c0")

    # Create network switches
    s1 = net.addSwitch("s1")
    s2 = net.addSwitch("s2")

    # Create host nodes
    h1 = net.addHost("h1", ip="10.0.0.1/24")
    h2 = net.addHost("h2", ip="10.0.0.2/24")

    # Link switches and hosts
    net.addLink(s1, s2)
    net.addLink(s1, h1)
    net.addLink(s2, h2)

    # Start the network
    net.start()

    # Add switches to the controller
    c0.start()
    c0.addSwitch(s1)
    c0.addSwitch(s2)

    # Open an xterm for each host
    h1.cmd("xterm -hold -e 'ping 10.0.0.2'")
    h2.cmd("xterm -hold -e 'ping 10.0.0.1'")

    # Run the Mininet command line interface
    CLI(net)

    # Stop the network
    net.stop()

if __name__ == "__main__":
    setLogLevel("info")
    create_sdn_network()
