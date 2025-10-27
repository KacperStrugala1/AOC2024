def split_number():
    with open ("data.txt", 'r') as f:
        #open and split data as int
        all_data = [int(x) for x in f.read().split()]
        
        #sort by even and odd index and sort
        a = ([all_data[x] for x in range(0, len(all_data), 2)])
        a = sorted(a)
        
        b= ([all_data[x] for x in range(1, len(all_data), 2)])
        b = sorted(b)
        #get abs value between numbers
        result = sum([abs(a_i - b_i) for a_i, b_i in zip(a, b)])
        return (result)

print(split_number())