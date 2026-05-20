# ============================================
# Week 1 Practice — Solar Data Basics
# Olufemi Akintunde | Africa Energy Analytics
# ============================================

# Exercise 1 — Lists and loops
cities = ["Lagos", "Nairobi", "Accra", "Cairo", "Johannesburg"]
for city in cities:
    print(f"Analysing solar data for {city}...")

print("\n" + "="*45 + "\n")

# Exercise 2 — Dictionaries
solar_ghi = {
    "Lagos": 4.5,
    "Nairobi": 5.8,
    "Accra": 5.2,
    "Cairo": 6.4,
    "Johannesburg": 5.6
}
for city, ghi in solar_ghi.items():
    print(f"{city}: {ghi} kWh/m²/day")

print("\n" + "="*45 + "\n")

# Exercise 3 — Functions
def classify_solar_potential(ghi):
    if ghi >= 6.0:
        return "Excellent"
    elif ghi >= 5.0:
        return "Good"
    else:
        return "Moderate"

for city, ghi in solar_ghi.items():
    rating = classify_solar_potential(ghi)
    print(f"{city}: {ghi} kWh/m²/day — {rating} potential")