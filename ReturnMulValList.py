import statistics

def mean_median_mode(list1):
  return [statistics.mean(list1),statistics.median(list1),statistics.mode(list1)]

mean_median_mode([3,4,5,6,7,8,9,10])
a,b,c = mean_median_mode([3,4,5,6,7,8,9,10])

print(f"Mean = {a}\nMedian = {b}\nMode = {c}")