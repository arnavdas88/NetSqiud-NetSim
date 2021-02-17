import json
from Core.Topology import Topology


topology = json.load(open("example.json"))

print(topology)

top = Topology()
top.load(topology)

print()
top.build()

# print()
# [print(top.CONNECTIONS[con].CONNECTION) for con in top.CONNECTIONS]

[top.NODES[node].summary() for node in top.NODES]

node_a = top.NODES["192.168.18.13"]
node_b = top.NODES["192.168.18.14"]

node_a.telnet()
node_b.telnet()
