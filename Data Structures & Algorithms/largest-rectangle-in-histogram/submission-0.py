class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        '''
Utilizes a monotonically increasing stack to track the potential start indices of rectangles.
Each stack element is a pair: (start_index, height).

When we encounter a height shorter than the top of the stack, it means the taller 
stack element cannot extend any further to the right. We process it by:
1. Popping the taller element to calculate its max area (width = current index - start_index).
2. Inheriting the popped element's start_index for the new, shorter bar. This is crucial 
   because the new shorter height remains valid all the way back to where the taller bar began.
'''
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea