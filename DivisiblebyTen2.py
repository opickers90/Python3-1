#Write your function here
def divisible_by_ten(nums):
  num_by_ten = 0
  for n in nums:
    if n % 10 == 0:
      num_by_ten += 1
  return num_by_ten    

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))
