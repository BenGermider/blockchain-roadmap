import asyncio
import time

from blockchain import Blockchain


if __name__ == "__main__":
    bc = Blockchain()
    s_time = time.time()
    for test in range(10):
        print(f"Working on block {test} addition.")
        asyncio.run(bc.add_block(f"Block {test}"))
    print(f"It took {time.time() - s_time} seconds to add 10 blocks.")