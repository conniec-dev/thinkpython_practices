class Kangaroo:
    """Represents a bag of items.
    attributes: pouch_contents"""

    def __init__(self, pouch_contents=[]):
        self.pouch_contents = pouch_contents

    def put_in_pouch(self, object):
        self.pouch_contents.append(object)

    def __str__(self):
        return "<" + str(self.pouch_contents)

    def _repr_pretty_(self, p, cycle):
        p.text(str(self) if not cycle else "...")

    def __add__(self, other):
        res = self.pouch_contents + other.pouch_contents
        return Kangaroo(res)


kan = Kangaroo()
roo = Kangaroo()
kan.put_in_pouch("wallet")
kan.put_in_pouch("car keys")
kan.put_in_pouch(roo)

print("kan:", kan)
print("roo:", roo)
