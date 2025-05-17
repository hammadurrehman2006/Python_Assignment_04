# ------------------Mars Weight Program

# Gravitational constant for Mars (relative to Earth's gravity)
MARS_GRAVITY = 0.378

def main():
# Prompt the user for their weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))  # Convert to float for calculation
    
# Calculate Mars weight (37.8% of Earth's weight)
    mars_weight = earth_weight * MARS_GRAVITY
    rounded_mars_weight = round(mars_weight, 2)  # Round to 2 decimal places
    
# Output the result
    print(f"The equivalent weight on Mars: {rounded_mars_weight}")

if __name__ == "__main__":
    main()
