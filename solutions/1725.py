import sys
input = sys.stdin.readline
print = sys.stdout.write


def Max_Rectangle(heights):
    stack = []
    max_area = 0
    n = len(heights)

    for i in range(n):
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
        print(stack)

    while stack:
        height = heights[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area


graph = []
n = int(input())

for i in range(n):
    graph.append(int(input()))

print(f"{Max_Rectangle(graph)}")
