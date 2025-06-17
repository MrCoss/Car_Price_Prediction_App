import pandas as pd
import numpy as np
import random

np.random.seed(42)

brands_models = {
    "Maruti": ["Swift", "Alto", "Baleno"],
    "Hyundai": ["i10", "i20", "Creta"],
    "Toyota": ["Innova", "Fortuner"],
    "Honda": ["City", "Amaze"],
    "Ford": ["EcoSport", "Figo"],
    "BMW": ["X1", "3 Series"]
}

colors = ["White", "Black", "Silver", "Red", "Blue"]
fuel_types = ["Petrol", "Diesel", "CNG", "Electric"]
transmissions = ["Manual", "Automatic"]
owners = ["First", "Second", "Third"]
cities = ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata"]

num_samples = 1000
data = []

for _ in range(num_samples):
    brand = random.choice(list(brands_models.keys()))
    model = random.choice(brands_models[brand])
    year = random.randint(2005, 2022)
    kms = random.randint(5000, 200000)
    fuel = random.choice(fuel_types)
    trans = random.choice(transmissions)
    owner = random.choice(owners)
    city = random.choice(cities)
    color = random.choice(colors)
    engine_size = random.randint(800, 3000)  # in cc
    mileage = round(random.uniform(10, 25), 1)  # km/l
    seats = random.choice([4, 5, 6, 7])
    insurance = random.choice(["Yes", "No"])

    # Simulate price (basic logic + randomness)
    base_price = 100000 + (2025 - year) * -15000 + engine_size * 50 + mileage * 1000
    if brand == "BMW":
        base_price += 800000  # premium brand
    if owner == "Second":
        base_price -= 30000
    elif owner == "Third":
        base_price -= 50000
    base_price -= kms * 0.3
    base_price = max(base_price + np.random.normal(0, 50000), 100000)

    data.append([
        brand, model, year, kms, fuel, trans, owner, city, color,
        engine_size, mileage, seats, insurance, int(base_price)
    ])

df = pd.DataFrame(data, columns=[
    "Brand", "Model", "Year", "Kilometers_Driven", "Fuel_Type",
    "Transmission", "Owner", "City", "Color", "Engine_Size", "Mileage",
    "Seats", "Insurance_Status", "Price"
])

df.to_csv("enhanced_car_data.csv", index=False)
print("✅ enhanced_car_data.csv with 1000 rows created.")
