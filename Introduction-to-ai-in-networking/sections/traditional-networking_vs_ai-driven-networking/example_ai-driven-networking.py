# Advanced AI-Driven Network Configuration (SDN with Mininet)

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import Controller, OVSKernelSwitch
from mininet.log import setLogLevel

# Create a custom topology
class SDNTopo(Topo):
    def build(self):
        # Create switches
        switch1 = self.addSwitch("s1")
        switch2 = self.addSwitch("s2")

        # Create hosts
        host1 = self.addHost("h1", ip="192.168.1.2/24")
        host2 = self.addHost("h2", ip="10.0.0.2/24")

        # Add links
        self.addLink(host1, switch1)
        self.addLink(host2, switch2)
        self.addLink(switch1, switch2)

# Create Mininet network
def create_network():
    topo = SDNTopo()
    net = Mininet(topo=topo, controller=Controller, switch=OVSKernelSwitch)
    net.start()
    net.pingAll()
    net.stop()

if __name__ == "__main__":
    setLogLevel("info")
    create_network()
