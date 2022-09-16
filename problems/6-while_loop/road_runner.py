current_distance, target_distance = int(input()), int(input())
days_count = 1

while current_distance < target_distance:
    current_distance *= 1.1
    days_count += 1

print(days_count)
