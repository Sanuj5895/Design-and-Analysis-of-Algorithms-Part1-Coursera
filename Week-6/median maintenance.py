import heapq

with open('median.txt') as f:
    nums = [int(c) for c in f]

heap_low  = []
heap_high = []

sum = 0
for num in nums:
  if len(heap_low) > 0:
    if num > -heap_low[0]:
      heapq.heappush(heap_high, num)
    else:
      heapq.heappush(heap_low, -num)
  else:
    heapq.heappush(heap_low, -num)

  if len(heap_low) > len(heap_high) + 1:
    heapq.heappush(heap_high, -(heapq.heappop(heap_low)))
  elif len(heap_high) > len(heap_low):
    heapq.heappush(heap_low, -(heapq.heappop(heap_high)))

  sum += -heap_low[0]

print sum % 10000