class BMI:
    def __init__(self, weight_pounds, height_feet):
        self.weight = weight_pounds
        self.height = height_feet

    def BMI_Value(self):
        # Convert height from feet to meters
        height_meters = self.height * 0.3048

        # Convert weight from pounds to kilograms
        weight_kg = self.weight * 0.453592

        # Calculate BMI
        bmi = weight_kg / (height_meters ** 2)
        return bmi

    def __eq__(self, other):
        if isinstance(other, BMI):
            return self.weight == other.weight and self.height == other.height
        return False

# Contoh penggunaan:
bmi1 = BMI(170, 2)
bmi2 = BMI(140, 5)

print("BMI Value for Person 1:", bmi1.BMI_Value())
print("BMI Value for Person 2:", bmi2.BMI_Value())

# Testing the equality method
print("Are the two BMI objects equal?", bmi1 == bmi2)
