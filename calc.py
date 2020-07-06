class Calc:
    def add(self, num1, num2):
        return num1 + num2
    def subtract(self,num1,num2):
        return num1 - num2
    def multiply(self,num1,num2):
        return num1 * num2
    def divide(self,num1,num2):
        return num1/num2
    def modulo(self,num1,num2):
        modulus = (int(num1 % num2))
        print(modulus)
        if modulus == 0:
            return "True"
        else:
            return False

simple_calc = Calc()
print(simple_calc.add(2, 2))