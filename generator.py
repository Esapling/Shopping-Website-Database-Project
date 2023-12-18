import json, random

with open(file="instances/products.json", mode="r") as products:
    product_list = json.load(products)

list_insert = []
for i in range(20):
    total_price = 0
    products = []
    random.seed()
    random.shuffle(product_list)
    x = random.randint(1, 10)
    selected_products = random.choices(product_list, k=x)
    amounts = []
    # print(selected_products)
    for product in selected_products:
        while True:
            random.seed()
            amount = random.randint(1, 100)
            if amount <= product['inventory']:
                break
        total_price += float(product['price'].replace('$', '')) * amount
        total_price = round(total_price, 2)
        products.append(product['product_id'])
        amounts.append(amount)
    msg = f"insert into receipt (product_id, amount, total_price) values ({products}, {amounts}, {total_price});"
    list_insert.append(msg)

for command in list_insert:
    print(command)
