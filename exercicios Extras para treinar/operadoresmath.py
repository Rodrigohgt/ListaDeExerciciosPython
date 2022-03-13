a = float(input("Digite um valor para calculo"))
b = float(input("Digite outro valor para calculo"))

x = a + b

print("{:.0f} + {:.0f} = {:.0f}".format(a, b, x))
print("{:.2f} * {:.2f} = {:.2f}".format(a, b, a * b))
print("{:.2f} / {:.2f} = {:.2f}".format(a, b, a / b))
print("{:.2f} - {:.2f} = {:.2f}".format(a, b, a - b))
print("{:.2f} + {:.2f} = {:.2f} /// {:.2f} * {:.2f} = {:.2f}".format(a, b, a + b, a, b, a * b))