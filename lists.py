servers = ["web01", "app01", "db01"]

print("Server List: ")
print(servers)

print("First Server: ", servers[0])
print("Second Server: ", servers[1])
print("Third Server: ", servers[2])


# ---------- using a loop ------

servers = ["web01", "app01", "db01"]

for server in servers:
    print("Checking Server: ", server)