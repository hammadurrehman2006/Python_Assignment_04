# ----------------Planetary Weight Program

# Gravitational constants for various planets (relative to Earth's gravity)
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
EARTH_GRAVITY = 1.0  # Earth's gravity is considered 100%

def main():
# Prompt for the user's weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))  # Convert to float for calculation
    
# Prompt for the planet name
    planet = input("Enter a planet: ")
    
# Determine the gravitational constant for the selected planet
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    elif planet == "Neptune":
        gravity_constant = NEPTUNE_GRAVITY
    else:
        gravity_constant = EARTH_GRAVITY  # Default to Earth if the planet name is not recognized
    
# Calculate the weight on the selected planet
    planetary_weight = earth_weight * gravity_constant
    rounded_planetary_weight = round(planetary_weight, 2)  # Round to 2 decimal places
    
# Output the result
    print(f"The equivalent weight on {planet}: {rounded_planetary_weight}")

if __name__ == "__main__":
    main()
