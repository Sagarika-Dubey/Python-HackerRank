from collections import OrderedDict
no_of_items = int(input())
orders_dict = OrderedDict()

for i in range(no_of_items):
    tmp_input = input().rsplit(" ",1)
    if tmp_input[0] in orders_dict:
        orders_dict[tmp_input[0]] += int(tmp_input[1])
    else:
        orders_dict[tmp_input[0]] = int(tmp_input[1])

for k,v  in orders_dict.items():
    print(k + " " + str(v))