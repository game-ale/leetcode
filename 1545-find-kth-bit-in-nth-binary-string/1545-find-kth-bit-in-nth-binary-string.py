class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        sequence = "0"

        # Generate sequence until we have enough elements or reach nth iteration
        for i in range(1, n):
            if k <= len(sequence):
                break
            sequence += "1"

            # Append the inverted and reversed part of the existing sequence
            inverted = "".join(
                "1" if bit == "0" else "0" for bit in sequence[:-1]
            )
            sequence += inverted[::-1]

        # Return the kth bit
        return sequence[k - 1]