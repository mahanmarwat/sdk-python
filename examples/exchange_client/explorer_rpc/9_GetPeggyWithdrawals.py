import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    sender = "inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku"
    peggy_deposits = await client.get_peggy_withdrawals(sender=sender)
    print(peggy_deposits)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
