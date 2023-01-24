class Fundament:
    pass


class Wall:
    pass


class Roof:
    pass


class Inner_Wall:
    pass


class House:
    def __init__(self, fundament, wall, roof, inner_wall):
        self.fundament = fundament
        self.wall = wall
        self.roof = roof
        self.inner_wall = inner_wall
        self.electricy = False

    def on(self):
        self.electricy = True

    def off(self):
        self.electricy = False


class Builder:
    def build_fundament(self):
        raise NotImplementedError

    def build_wall(self):
        raise NotImplementedError

    def build_roof(self):
        raise NotImplementedError

    def build_inner_wall(self):
        raise NotImplementedError


class HouseBuilder:
    def build_fundament(self):
        return Fundament()

    def build_wall(self):
        return Wall()

    def build_roof(self):
        return Roof()

    def build_inner_wall(self):
        return Inner_Wall()

    def build_house(self):
        fundament = self.build_fundament()
        wall = self.build_wall()
        roof = self.build_roof()
        inner_wall = self.build_inner_wall()
        return House(fundament, wall, roof, inner_wall)


ivan_builder = HouseBuilder()
own_house = ivan_builder.build_house()

print(own_house)
print(own_house.fundament)
print(own_house.wall)
print(own_house.roof)
print(own_house.inner_wall)
