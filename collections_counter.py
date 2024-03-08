# Enter your code here. Read input from STDIN. Print output to STDOUT
total_shoes = int(input())
shoes_sizes = list(map(int, input().split()))
n_of_customers = int(input())

factured = 0
for i in range(n_of_customers):
    j, k = map(int, input().split())
    if j in shoes_sizes:
        shoes_sizes.remove(j)
        factured = factured + k
print(factured)