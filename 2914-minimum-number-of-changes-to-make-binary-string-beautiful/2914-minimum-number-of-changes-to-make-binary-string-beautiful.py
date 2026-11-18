class Solution:
    def minChanges(self, s: str) -> int:
        # Initialize with first character
        current_char = s[0]

        consecutive_count = 0
        min_changes_required = 0

        # Iterate through each character
        for char in s:
            # If current character matches the previous sequence
            if char == current_char:
                consecutive_count += 1
                continue

            # If we have even count of characters, start new sequence
            if consecutive_count % 2 == 0:
                consecutive_count = 1
            # If odd count, we need to change current character
            else:
                consecutive_count = 0
                min_changes_required += 1

            # Update current character for next iteration
            current_char = char

        return min_changes_required