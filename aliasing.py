# function to multiply each element by x and print the list
def scale_and_print(nums_, scaling_factor_):
    for i in range(len(nums)):
        nums_[i] *= scaling_factor_
    print(f"nums * {scaling_factor_}: {nums_}")


# example vector
nums = [2, 5, 10]
print(f"nums: {nums}")

# print 1, 2, 3 multiples of vector
for i in range(1, 4):
    scale_and_print(nums, i)
