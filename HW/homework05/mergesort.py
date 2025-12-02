import sys


def merge(left, right):
    new_list = []
    while left and right:
        print(f"left: {left}, right: {right}")
        if left[0] <= right[0]:
            new_list.append(left.pop(0))
        elif left[0] > right[0]:
            new_list.append(right.pop(0))
    if left:
        new_list.extend(left)
    elif right:
        new_list.extend(right)
    return new_list

def sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = sort(data[:mid])
    right = sort(data[mid:])
    return merge(left, right)



if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 2:
        print("Usage: mergesort.py input_file output_file")
        sys.exit(1)
    input_file_path, output_file_path = args
    data = []
    with open(input_file_path, "r") as input_file:
        for line in input_file:
            data.append(int(line))
    print(data)
    sorted = sort(data)
    print(sorted)
    with open(output_file_path, "w") as output_file:
        for number in sorted:
            output_file.write(f"{number:03}\n")