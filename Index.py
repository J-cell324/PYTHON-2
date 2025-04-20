
my_list = []


my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)

my_list.extend([50, 60, 70])


my_list.pop()


my_list.sort()

index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)


print("Final my_list:", my_list)
 
 #week 3


def calculate_discount(price, discount_percent):
       if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price


try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if final_price < price:
        print(f"Discount applied! Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Final price: ${final_price:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount.")
