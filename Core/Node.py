import os
import netsquid as ns
import subprocess


from .Telnet import Telnet
from .Kernel import Kernel

class Node:
    TYPE = ""
    ID = ""
    NAME = ""
    node = None
    ports = []

    delay_config = {}
    delay_type = "FixedDelayModel"

    network = None

    telnet_client = None

    kernel = None
    
    
    def __init__(self, network):
        self.network = network
        pass

    def __call__(self, ):
        pass

    def telnet(self, ):
        # subprocess.call(str.split(f"xterm -hold -e")+[f'telnet {self.telnet_client.host} {self.telnet_client.port}'])
        os.system(f"xterm -hold -e telnet {self.telnet_client.host} {self.telnet_client.port} &")
        pass

    def run(self, command):
        self.kernel.run(command)
        self.network() # ns.sim_run()
        pass

    def load(self, data):
        ''' Loads the configuration from a dictionary object.
        data(dict): A dictionary object from which the configuration is loaded.
        '''
        self.TYPE = data["type"]
        self.ID = data["id"]
        self.NAME = data["name"]
        self.delay_config = data.get("delay-config", {})
        self.delay_type = data.get("delay-type", "FixedDelayModel")
        self.ports = data.get("ports", ["port_to_channel"])

        print(f"Starting Telnet for device {self.NAME} in ", end = "")
        self.telnet_client = Telnet(name=self.NAME)
        self.telnet_client(self.run)
        self.kernel = Kernel(self)
        # self.telnet_client(print)

        return self
    
    def create(data, network):
        node = Node(network)
        return node.load(data)
    
    def summary(self, ):
        print("="*7, self.ID, "::", f"[{self.TYPE}]", "="*7)
        print("\t" + "Name : " + self.NAME + "\t")
        print("\t" + "Ports : " + str(self.ports) + "\t")
        print("\t" + "Source.delay : " + str(self.delay_config) + "\t")
        print("\t" + "Source.delay_type : " + self.delay_type + "\t")
        print()

    def build(self, network):
        self.node = ns.nodes.Node(name=self.NAME, port_names=self.ports)
        pass

