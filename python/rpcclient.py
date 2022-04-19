import xmlrpc.client

with xmlrpc.client.ServerProxy("http://gao:gao123@localhost:8252/") as proxy:
    print(str(proxy.getinfo()))
