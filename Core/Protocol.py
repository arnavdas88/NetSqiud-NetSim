import netsquid as ns

from netsquid.protocols import NodeProtocol
from netsquid.qubits import qubitapi as qapi

class PingProtocol(NodeProtocol):
    def __init__(self, node, telnet_client, port):
        super().__init__(node)
        self.port = port
        self.telnet = telnet_client

    def run(self):
        # print(f"Starting ping at t={ns.sim_time()}")
        port = self.node.ports[self.port]
        qubit, = qapi.create_qubits(1)
        port.tx_output(qubit)  # Send qubit to Pong
        # print(f"[i] Sent {qubit}.")
        self.telnet.listener_push(f"[i] Sent {qubit}.")


class ListenProtocol(NodeProtocol):
    def __init__(self, node, telnet_client, port):
        super().__init__(node)
        self.port = port
        self.telnet = telnet_client
    
    def run(self):
        # print("Starting pong at t={}".format(ns.sim_time()))
        port = self.node.ports[self.port]
        while True:
            yield self.await_port_input(port)
            qubit = port.rx_input().items[0]
            m, prob = qapi.measure(qubit, ns.Z)
            # print(f"[i] Received {m} with {prob} probability.")
            self.telnet.listener_push(f"[i] Received {m} with {prob} probability.")

class BlankProtocol:
    def __init__(self, *args, **kwargs):
        pass
    def start(self, ):
        pass
    def run(self, ):
        pass