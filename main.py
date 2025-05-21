import asyncio
from blockchain import Blockchain


if __name__ == "__main__":
    bc = Blockchain()
    for test in range(10):
        print(f"Working on block {test} addition.")
        asyncio.run(bc.add_block(f"Block {test}"))
