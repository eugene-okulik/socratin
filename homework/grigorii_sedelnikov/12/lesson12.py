class Flower:
    def __init__(self, name, color, stem_length, price, lifespan):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.lifespan = lifespan


class Rose(Flower):
    def __init__(self, color, stem_length, price, lifespan):
        super().__init__("Rose", color, stem_length, price, lifespan)


class Lily(Flower):
    def __init__(self, color, stem_length, price, lifespan):
        super().__init__("Lily", color, stem_length, price, lifespan)


class Tulip(Flower):
    def __init__(self, color, stem_length, price, lifespan):
        super().__init__("Tulip", color, stem_length, price, lifespan)


class Booqet:
    def __init__(self):
        self.flowers = []

    def price_bouqeet(self):
        total_price = 0
        for flower in self.flowers:
            total_price += flower.price
        return total_price

    def dead_time(self):
        total_time = 0
        for flower in self.flowers:
            total_time += flower.lifespan
        return total_time / len(self.flowers)

    def add_flower(self, flower):
        self.flowers.append(flower)

    def sorted(self, key):
        if key == "price":
            self.flowers.sort(key=lambda x: x.price, reverse=True)
        if key == "lifespan":
            self.flowers.sort(key=lambda x: x.lifespan, reverse=True)
        if key == "color":
            self.flowers.sort(key=lambda x: x.color)
        if key == "stem_length":
            self.flowers.sort(key=lambda x: x.stem_length, reverse=True)

    def search_flower_lifespan(self, lifespan):
        for flower in self.flowers:
            if flower.lifespan == lifespan:
                return True
        return False


rose1 = Rose("white", 25, 8, 4)
lily1 = Lily("white", 40, 12, 7)
tulip1 = Tulip("yellow", 20, 6, 3)

booqet = Booqet()
booqet.add_flower(rose1)
booqet.add_flower(lily1)
booqet.add_flower(tulip1)
