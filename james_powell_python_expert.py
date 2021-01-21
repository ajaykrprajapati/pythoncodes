class polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{})'.format(self.coeffs)

p1 = polynomial(1,2,3)
p2 = polynomial(4,5,6)

print(p1)
print(p2)