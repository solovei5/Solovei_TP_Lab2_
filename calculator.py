# calculator.py
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
# ... (попередні функції add, subtract) ...
def multiply(x, y):
    return x * y
if __name__ == "__main__":
    num1 = 15
    num2 = 7
    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
# Додаємо виклик нової функції
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
# Змінюємо повідомлення
print("Калькулятор оновлено: додано множення.") # Змінений рядок!
