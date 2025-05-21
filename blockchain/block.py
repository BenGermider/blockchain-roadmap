from datetime import datetime
from hashlib import sha256

class Block:

    def __init__(self, data, previous_hash):
        self._data = data
        self._previous_hash = previous_hash
        self._timestamp = datetime.now()
        self._hash = self._calculate_hash()

    def _calculate_hash(self):
        """
        Calculate the hash of the block using SHA-256.
        """
        block_string = f"{self._data}{self._previous_hash}{self._timestamp}"
        return sha256(block_string.encode()).hexdigest()

    @property
    def data(self):
        """
        Get the data of the block.
        """
        return self._data

    @property
    def hash(self):
        """
        Get the previous hash of the block.
        """
        return self._hash
