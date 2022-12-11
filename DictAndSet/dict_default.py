from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")

bean_quantity = pantry.setdefault("beans", 0)
print(f"beans: {bean_quantity}")

ketchup_quantity = pantry.get("ketchup", 0)
print(f"ketchup: {ketchup_quantity}")

print()

print("`pantry` now contains")

for key,value in sorted(pantry.items()):
    print(key,value)
