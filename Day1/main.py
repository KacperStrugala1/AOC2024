def split_number():
    with open ("data.txt", 'r') as f:
        all_data = [x for x in f.read().split()]
        length = len(all_data)//2
        left_values = sorted([all_data[x] for x in length if x % 2 == 0])
        right_values = sorted([all_data[x] for x in length if x % 2 != 0])
        result = sum(left_values-right_values)
        return (result)

print(split_number())