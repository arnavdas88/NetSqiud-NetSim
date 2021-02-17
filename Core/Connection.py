import netsquid as ns

from netsquid.components import Channel, QuantumChannel
from netsquid.nodes import DirectConnection

from .utils import get_delay_model, get_loss_model

class Connection:
    TYPE = "classical"
    NAME = ""
    CONNECTION = []

    conn = None

    distance = 2.74 / 1000  # default unit of length in channels is km, i.e. distance = 2.74 meters
    delay_config = {}
    delay_type = "FibreDelayModel"
    loss_config = {}
    loss_type = "FibreLossModel"
    network = None

    def __init__(self, network):
        self.network = network
        pass

    def __call__(self, ):
        pass

    def load(self, data):
        ''' Loads the configuration from a dictionary object
        data(dict) : A dictionary object from which the configuration is loaded
        '''
        self.TYPE = data["type"]
        self.NAME = data["name"]
        self.CONNECTION = {
            "connection": data["connection"],
            "to": data["to"],
            "from": data["from"]
        }
        self.delay_config = data.get("delay-config", {})
        self.delay_type = data.get("delay-type", "FibreDelayModel")
        self.loss_config = data.get("loss-config", {})
        self.loss_type = data.get("loss-type", {})
        
        return self
    
    def create(data, network):
        connection = Connection(network)
        return connection.load(data)

    def build(self, network):
        delay_model = get_delay_model(self.delay_type, **self.delay_config)
        loss_model = get_loss_model(self.loss_type, **self.loss_config)
        if self.TYPE == "quantum":
            channel_1 = QuantumChannel(name="AtoB", length=self.distance, models={"delay_model": delay_model,'quantum_loss_model': loss_model})
            channel_2 = QuantumChannel(name="BtoA", length=self.distance, models={"delay_model": delay_model, 'quantum_loss_model': loss_model})

            self.conn = connection = DirectConnection(name=self.NAME, channel_AtoB=channel_1, channel_BtoA=channel_2)

            to_node = network.NODES[self.CONNECTION["to"]["id"]]
            to_port = self.CONNECTION["to"]["port"]

            from_node = network.NODES[self.CONNECTION["from"]["id"]]
            from_port = self.CONNECTION["from"]["port"]

            to_node.node.ports[to_port].connect(self.conn.ports["A"])
            from_node.node.ports[from_port].connect(self.conn.ports["B"])
        pass
