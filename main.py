import json

from src.message import message
from src.utils import (
    load_clients, load_sender, run
)

with open("Configs/clients.json") as clients_config_file:
    clients_config = json.load(clients_config_file)

with open("Configs/source_config.json") as source_config_file:
    source_config = json.load(source_config_file)

with open("Configs/secret_config.json") as secret_config_file:
    secret_config = json.load(secret_config_file)

clients = load_clients(clients_config)
sender = load_sender(
    source_config=source_config,
    secret_config=secret_config
)


if __name__ == "__main__":
    run(
        sender=sender,
        clients=clients,
        message=message
    )

