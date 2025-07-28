import random

count_7 = 0
count_2 = 0
count_gt_10 = 0

trials = 10000

for _ in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    if total == 7:
        count_7 += 1
    elif total == 2:
        count_2 += 1
    elif total > 10:
        count_gt_10 += 1

p_sum_7 = count_7 / trials
p_sum_2 = count_2 / trials
p_sum_gt_10 = count_gt_10 / trials

print(f"P(Sum = 7): {p_sum_7:.4f}")
print(f"P(Sum = 2): {p_sum_2:.4f}")
print(f"P(Sum > 10): {p_sum_gt_10:.4f}")
