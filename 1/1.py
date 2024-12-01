import heapq
minHeapLeft = []
minHeapRight = []
leftList = []
right_dct = {}
with open(file="1/input.txt", mode='r') as file:
    for i,line in enumerate(file):
        splitLine = line.strip().split(' ')
        left = splitLine[0]
        right = splitLine[3]
        heapq.heappush(minHeapLeft, int(left))
        heapq.heappush(minHeapRight, int(right))
        # left_dct[left] = 1 + left_dct.get(left, 0)
        leftList.append(int(left))
        right_dct[int(right)] = 1 + right_dct.get(int(right), 0)
distance = 0
while minHeapLeft and minHeapRight:
    distance += abs(heapq.heappop(minHeapLeft) - heapq.heappop(minHeapRight))
sim_score = 0
for item in leftList:
    sim_score += (item * right_dct.get(item, 0))
print(distance)
print(sim_score)

