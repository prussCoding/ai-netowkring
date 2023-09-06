# Traditional Networking Configuration (Basic Router)

class Router:
    def __init__(self, name):
        self.name = name
        self.interfaces = []

    def add_interface(self, interface_name, ip_address):
        self.interfaces.append((interface_name, ip_address))

    def show_interfaces(self):
        print(f"Interfaces on {self.name}:")
        for interface in self.interfaces:
            print(f"Interface: {interface[0]}, IP Address: {interface[1]}")


# Create a router instance
router1 = Router("Router1")

# Add interfaces to the router
router1.add_interface("eth0", "192.168.1.1")
router1.add_interface("eth1", "10.0.0.1")

# Display router interfaces
router1.show_interfaces()
