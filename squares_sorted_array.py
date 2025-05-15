def sortedSquares(self, nums):
        squares = []
        ans = []
        for num in nums:
            num = num*num
            squares.append(num)
        
        left = 0
        right= len(squares)-1
        
        while left <= right:
            if squares[left] < squares[right]:
                ans.append(squares[left])
                left+=1
            
            else:
                ans.append(squares[right])
                right -=1
        return sorted(ans)