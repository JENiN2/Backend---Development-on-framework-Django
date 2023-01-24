class Mug:
    def __init__(self, size_h, size_d):
        self.size_h = size_h
        self.size_d = size_d

    def volume_enc(self):
        return 3.14 * ((self.size_d / 2) ** 2) * self.size_h

    def volume_without_enc(self, size_d, size_h):
        return 3.14 * ((size_d / 2) ** 2) * size_h

    def volume(self):
        return self.volume_without_enc(self.size_d, self.size_h)


mug_original = Mug(15, 7)
mug_dublicate = Mug(10, 6)

print(mug_original.volume_enc())
print(mug_original.volume_without_enc(mug_original.size_d, mug_original.size_h))
print(mug_dublicate.volume_enc())
print(mug_original.volume_without_enc(mug_dublicate.size_d, mug_dublicate.size_h))
