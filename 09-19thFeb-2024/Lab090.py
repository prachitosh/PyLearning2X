class cal:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


obj_ref = cal()
result = obj_ref.sum(3,4)
print(result)

obj_ref = cal()
result = obj_ref.sub(5,4)
print(result)

obj_ref = cal()
result = obj_ref.mul(5,4)
print(result)

obj_ref = cal()
result = obj_ref.div(5,4)
print(result)

