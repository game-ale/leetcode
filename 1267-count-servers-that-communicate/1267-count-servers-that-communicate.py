class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0]) if num_rows > 0 else 0
        communicable_servers_count = 0

        # Traverse through the grid
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    can_communicate = False

                    # Check for communication in the same row
                    for other_col in range(num_cols):
                        if other_col != col and grid[row][other_col] == 1:
                            can_communicate = True
                            break

                    # If a server was found in the same row, increment
                    # communicable_servers_count
                    if can_communicate:
                        communicable_servers_count += 1
                    else:
                        # Check for communication in the same column
                        for other_row in range(num_rows):
                            if other_row != row and grid[other_row][col] == 1:
                                can_communicate = True
                                break

                        # If a server was found in the same column, increment
                        # communicable_servers_count
                        if can_communicate:
                            communicable_servers_count += 1

        return communicable_servers_count