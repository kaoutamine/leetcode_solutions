class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        f_pos = n  # Default to all negative

        for i, num in enumerate(nums):
            if num >= 0:
                f_pos = i
                break

        # Square the list
        squares = [x**2 for x in nums]

        # If all numbers are positive
        if f_pos == 0:
            return squares

        # If all numbers are negative
        if f_pos == n:
            squares.reverse()
            return squares

        # If mixed
        squares1 = squares[:f_pos]
        squares1.reverse()  # In-place reversal
        squares2 = squares[f_pos:]

        # Merge
        result = []
        i, j = 0, 0
        while i < len(squares1) and j < len(squares2):
            if squares1[i] < squares2[j]:
                result.append(squares1[i])
                i += 1
            else:
                result.append(squares2[j])
                j += 1

        result.extend(squares1[i:])
        result.extend(squares2[j:])

        return result