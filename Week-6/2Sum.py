with open('HashInt.txt') as f:
    nums = [int(c) for c in f]

a = {}
answers = {}

for i in nums:
  a[i] = True

for i in nums:
  for t in xrange(-10000,10001):
    if t - i in a:
      if i == t - i:
        continue
      if t not in answers:
        answers[t] = set([tuple(sorted([i, t - i]))])
      else:
        answers[t].add(tuple(sorted([i, t - i])))

print len(answers)
