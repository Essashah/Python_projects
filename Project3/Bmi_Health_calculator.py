# Function to calculate BMI
def calculate_bmi(weight_kg, height_cm):
    """
    This function calculates the BMI (Body Mass Index) based on the weight in kilograms and height in centimeters.
    The formula for BMI is: BMI = weight (kg) / height (m)^2
    """
    height_m = height_cm / 100  # Convert height to meters
    bmi = weight_kg / (height_m ** 2)  # BMI formula
    return bmi  # Ensure this line is present to return the calculated BMI

# Function to interpret BMI and provide health advice
def interpret_bmi(bmi):
    """
    This function interprets the BMI result and returns a category based on the BMI value.
    It also provides basic health advice for each category.
    """
    if bmi < 18.5:
        category = "Underweight"
        advice = "You are underweight. It's important to maintain a balanced diet and consult a healthcare provider for advice."
    elif 18.5 <= bmi <= 24.9:
        category = "Normal weight"
        advice = "You have a normal weight. Keep up the good work with a healthy diet and regular exercise."
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
        advice = "You are overweight. Consider adopting a healthier lifestyle with a balanced diet and more physical activity."
    else:
        category = "Obese"
        advice = "You are obese. It is highly recommended to consult a healthcare provider for personalized advice."

    return category, advice

# Main function to gather input and display results
def main():
    """
    This is the main function where we prompt the user to enter their height, weight, and age.
    It calls other functions to perform calculations and provide feedback.
    """
    
    print("Welcome to the BMI and Health Indicator Calculator!")
    print("Please enter your details to calculate your BMI and other health indicators.")
    
    # User input for height, weight, and age
    height_cm = float(input("Enter your height in centimeters: "))
    weight_kg = float(input("Enter your weight in kilograms: "))
    age = int(input("Enter your age: "))
    
    # Call the BMI calculation function
    bmi = calculate_bmi(weight_kg, height_cm)
    
    # Debug: Print the BMI value to check if it's correctly calculated
    print(f"Debug: Calculated BMI is {bmi}")
    
    # Print the calculated BMI
    print(f"Your BMI is: {bmi:.2f}")
    
    # Interpret the BMI and provide feedback
    category, advice = interpret_bmi(bmi)
    
    # Print the BMI category and advice
    print(f"Your BMI category is: {category}")
    print(f"Health advice: {advice}")

# Call the main function to start the program
main()
