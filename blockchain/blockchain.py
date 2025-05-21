from block import Block

class Blockchain:

    def __init__(self):
        self.chain = [self._create_genesis_block()]

    @staticmethod
    def _create_genesis_block() -> Block:
        """
        Create the genesis block (the first block in the blockchain).
        """
        return Block("Genesis Block", "0" * 64)

    async def add_block(self, data) -> None:
        """
        Add a new block to the blockchain.
        """
        previous_block = self.chain[-1]
        new_block = Block(data, previous_block.hash)
        await new_block.mine_block(4)  # Example difficulty
        self.chain.append(new_block)
