class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        b.f: create a seen dict where we have a key for each row and col, and the value to each key would be a set 
        of the elements in that row or column. This way we can traverse the board visiting every cell 3*3 and keeping the elems of each box
        also in a set, so for each addition we check 3 sets, row, col, and the box and if no collision we proceed to adding the
        values of each cell to their respective row and col. At any point if the value being added to the row or col already
        exists for that col we return False as we have found a duplicate, if not we continue and move onto the next 3*3.

        Time this will take is going to be the time to check every cell which in this case since we know we have a 9*9 board
        it will be O(81) which is consant and in big O notation can be simplified to O(1).

        Space needed will be a dict with 9 rows and 9 cols, where each set can have a size as large as a row or a col which would be 9.
        So the largest the dict will ever grow to would be 81 keys and up to 9 values per key. That being said, this would also be (81*9) which again
        can be simplified to O(1)
        """
        rows_cols_seen = defaultdict(set)
        box_counter = 0
        row_offset = 0
        col_offset = 0
        while box_counter < 9:
            this_box = set()
            for i in range(row_offset, row_offset+3):
                for j in range(col_offset, col_offset+3):
                    if board[i][j] != ".":
                        cell = int(board[i][j])
                        if not cell in rows_cols_seen[f"r{i}"] and not cell in rows_cols_seen[f"c{j}"] and not cell in this_box:
                            rows_cols_seen[f"r{i}"].add(cell)
                            rows_cols_seen[f"c{j}"].add(cell)
                            this_box.add(cell)
                        else:
                            return False
            box_counter += 1
            col_offset += 3
            if box_counter%3 == 0:
                row_offset += 3
                col_offset = 0
        return True
            
