from tools.laptop_tools import search_by_budget, filter_by_ram, best_value_laptops


print("\n🔍 Testing Budget Search...\n")

laptops = search_by_budget(70000)

print("Total Found:", len(laptops))

for lap in laptops[:5]:
    print(f"{lap['brand']} | ₹{lap['price']} | {lap['ram']}GB RAM")


print("\n💻 Testing RAM Filter...\n")

ram_laptops = filter_by_ram(16)

print("Total Found:", len(ram_laptops))

for lap in ram_laptops[:5]:
    print(f"{lap['brand']} | {lap['ram']}GB | ₹{lap['price']}")


print("\n🏆 Testing Best Value...\n")

best = best_value_laptops(80000)

for lap in best[:5]:
    print(f"{lap['brand']} | Score Laptop | ₹{lap['price']} | {lap['ram']}GB")
