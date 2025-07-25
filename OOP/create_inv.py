class Item:
    def __init__(self, name, quantidy, price):
        self.p = price
        self.q = quantidy
        self.n = name
    def dis_item(self):
        return f"name: {self.n}, quantidy: {self.q}, price: {self.p}"
    def update_quantidy(self, new_quantidy):
        self.q = new_quantidy
    
i1 = Item("apple", 23, 30)

print(i1.update_quantidy(3))
print(i1.dis_item())

