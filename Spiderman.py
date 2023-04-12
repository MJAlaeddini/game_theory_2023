input_num_of_test = int(input())
result = 1
list_of_test = list(map(int, input().split(" " , input_num_of_test-1)))
for i in list_of_test:
    result += i - 1
    answer = result % 2 + 1
    print(answer)