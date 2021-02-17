import netsquid as ns
from .Node import Node
from .Connection import Connection

class Topology:
    NAME = ""

    NODES = {}
    CONNECTIONS = {}

    network = None

    def __init__(self, ):
        ns.sim_reset()
        ns.set_random_state(seed=42)
        pass

    def __call__(self, ):
        stats = ns.sim_run()
        return stats


    def build(self, ):
        # network = Network(self.NAME)
        [node.build(self) for _, node in self.NODES.items()]
        [conn.build(self) for _, conn in self.CONNECTIONS.items()]

    def load(self, data):
        ''' Loads the configuration from a dictionary object
        data(dict) : A dictionary object from which the configuration is loaded
        '''
        self.NODES = { node['id']: Node.create(node, self) for node in data['nodes']}
        self.CONNECTIONS = { connection['name']: Connection.create(connection, self) for connection in data['connections']}
        self.NAME = data["name"]



