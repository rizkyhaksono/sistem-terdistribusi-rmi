# Remote Method Invocation (RMI)

This is a simple implementation of RMI in python. This repository made for homework of Distributed System course in University of Muhammadiyah Malang.

## What is RMI?
The RMI (Remote Method Invocation) is an API that provides a mechanism to create distributed application in java. The RMI allows an object to invoke methods on an object running in another JVM. [source](https://www.javatpoint.com/RMI)

## How to Run?
1. Clone this repository
2. Install the requirements
```bash
pip install Pyro4
```
3. Run the server
```bash
python .\server\server.py
```
4. Run the client
```bash
python .\client\client.py
```
5. Run the Pyro4 nameserver
```bash
python -m Pyro4.naming
```