import random
import json

companies = json.loads(open("company_names.json").read())
products = json.loads(open("products.json").read())

rand_company = random.choice(list(companies))
rand_product = random.choice(list(products))


print("Why don't we develop the next " + rand_company + " for " + rand_product + "?")