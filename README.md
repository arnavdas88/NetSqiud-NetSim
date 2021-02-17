# NetSqiud-NetSim
An abstraction layer over netsquid to build, test and share quantum network components and topologies in a simpler way

## Usage

### Implementaion of the `test.py` file

First loading the project file, which contains all the components and their topology.
```python
import json

topology = json.load(open("example.json"))
print(topology)
```
Next, let's load the project's topology and construct the network.
```python
from Core.Topology import Topology

top = Topology()
# Loads the project topology and create the necessary components
top.load(topology)

# Build the topology against the necessary components
top.build()
```
Once the network has been build, One can start interacting with the simulation and its components.

To print the summary `Nodes`, one can directly invoke the `summary()`  function from the elemental Node.

```python
[top.NODES[node].summary() for node in top.NODES]
```

Similarly, one can invoke the `telnet()` function to start a telnet connection to a `Node`, and run commands.

```python
[top.NODES[node].telnet() for node in top.NODES]
```
## The topology project file
```json
 {
    "name": "Quantum_Connection",
    "description": "A simple quantum link",
    "nodes": [
        {
            "id": "192.168.18.13",
            "name": "node_A",
            "type": "edge",
            "class": "node",
            "memory": 3,
            "delay-config": { "delay": 5 },
            "ports": ["qport"]
        },
        {
            "id": "192.168.18.14",
            "name": "node_B",
            "type": "edge",
            "memory": 3,
            "class": "node",
            "ports": ["qportL"]
        }
    ],
    "connections": [
        {
            "name": "quantum",
            "type": "quantum",
            "connection": ["192.168.18.13", "192.168.18.14"],
            "to": {"id": "192.168.18.13", "port": "qport"},
            "from": {"id": "192.168.18.14", "port": "qportL"},
            "distance": "43",
            "delay-type": "FibreDelayModel",
            "loss-type": "FibreLossModel",
            "loss-config": { "p_loss_init": 0.83, "p_loss_length": 0.2}
        }
    ]
 }

```


# License
```
                Copyright (C) 2007 Free Software Foundation, Inc.

 Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.

 The GNU General Public License is a free, copyleft license for software and other kinds of works.

  The licenses for most software and other practical works are designed to take away your freedom to share and change the works. By contrast, the GNU General Public License is intended to guarantee your freedom to share and change all versions of a program--to make sure it remains free software for all its users.  We, the Free Software Foundation, use the GNU General Public License for most of our software; it applies also to any other work released this way by its authors.  You can apply it to your programs, too.
```