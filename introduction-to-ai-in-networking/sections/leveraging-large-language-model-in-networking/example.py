# Import necessary modules
import openai
import logging
from dataclasses import dataclass
from mysecrect import API_KEY  # Import the API_KEY from a secret file
from typing import List

# Configure logging for debugging purposes
logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.DEBUG)

# Set the API key for OpenAI
api_key = API_KEY
openai.api_key = api_key

# Define default chat messages
default_messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What's the weather like today?"},
]

# Function to create a Chat Completion request
def set_ChatCompletion(engine: str = 'gpt-3.5-turbo', messages: List[dict] = default_messages):
    return openai.ChatCompletion.create(
        model=engine,  # Use the chat model appropriate for your needs
        messages=messages
    )

# Define a data class 'Port' to represent network switch ports
@dataclass
class Port:
    name: str
    vlan: str
    port_type: str

# Define a data class 'Switch' to represent network switches and their configurations
@dataclass
class Switch:
    name: str
    brand: str
    role: str
    office_size: str
    vlans: list[int]
    ports: list[Port]

    # Method to generate a configuration prompt
    def configuration_prompt(self):
        return 'Please generate the configuration commands.'

    # Method to prompt for configuring switch type
    def prompt_configure_switch_type(self):
        return f'I need to configure a new {self.brand} switch for a {self.office_size} office. '

    # Method to prompt for configuring VLANs
    def prompt_configure_vlans(self):
        default_vlan = self.vlans[0]
        vlans = self.vlans[0: (len(self.vlans) - 1)]
        last_vlan = self.vlans[-1]
        logging.info(f'{vlans}, {last_vlan} and {default_vlan}')
        return f'It should have VLANs {", ".join(map(str, vlans))} and {str(last_vlan)}, with VLAN {str(default_vlan)} as the default VLAN.'

    # Method to prompt for configuring ports
    def prompt_configure_ports(self):
        _ = []
        for port in self.ports[0: (len(self.ports) - 1)]:
            _.append(f'Port {port.name} should be an {port.port_type} port in VLAN {str(port.vlan)}, ')

        _.append(f'and Port {self.ports[len(self.ports) - 1].name} should be a {self.ports[len(self.ports) - 1].port_type} port for VLAN {self.ports[len(self.ports) - 1].vlan}.')
        return f''.join(_)

    # Method to compose the full prompt message
    def prompt_message(self):
        return ''.join([self.prompt_configure_switch_type(),
                        self.prompt_configure_vlans(),
                        self.prompt_configure_ports(),
                        self.configuration_prompt()])

    # Method to render a message in the chat format
    def render(self):
        return {"role": self.role, "content": self.prompt_message()}

    # Method to set the configuration plan
    def set_plan(self, plan):
        self.plan = plan

# Create two switch instances with their configurations
switch1 = Switch(
    name='sw1',
    brand='Cisco',
    role='user',
    office_size='small',
    vlans=[10, 30, 50],
    ports=[
        Port(
            name=1,
            vlan=10,
            port_type='access',
        ),
        Port(
            name=2,
            vlan=30,
            port_type='access',
        ),
        Port(
            name=3,
            vlan=50,
            port_type='trunk',
        ),
    ]
)

switch2 = Switch(
    name='sw2',
    brand='Cisco',
    role='user',
    office_size='small',
    vlans=[20, 40, 60],
    ports=[
        Port(
            name=1,
            vlan=20,
            port_type='access',
        ),
        Port(
            name=2,
            vlan=40,
            port_type='access',
        ),
        Port(
            name=3,
            vlan=60,
            port_type='trunk',
        ),
    ]
)

# Create a list of switch configurations
configurations = [switch1, switch2]

# Iterate through the list and process each switch configuration
for configuration in configurations:
    response = set_ChatCompletion(messages=[configuration.render()])
    configuration.set_plan(response['choices'][0]['message']['content'])
    logging.info(f'Configuration Plan for ({configuration.name}) - {configuration.plan}')
