class Kangaroo:
    """A Kangaroo is a marsupial."""

    def __init__(self, name, contents=None):
        """Initialize the pouch contents.
        name: string
        contents: initial pouch contents.
        """
        # In this version, the default value is None.  When
        # __init__ runs, it checks the value of contents and,
        # if necessary, creates a new empty list.  That way,
        # every Kangaroo that gets the default value gets a
        # reference to a different list.

        # As a general rule, you should avoid using a mutable
        # object as a default value, unless you really know
        # what you are doing.
        self.name = name
        if contents == None:
            contents = []
        self.pouch_contents = contents

    def __str__(self):
        """Return a string representaion of this Kangaroo."""
        t = [self.name + " has pouch contents:"]
        for obj in self.pouch_contents:
            s = "    " + object.__str__(obj)
            t.append(s)
        return "\n".join(t)

    def put_in_pouch(self, item):
        """Adds a new item to the pouch contents.
        item: object to be added
        """
        self.pouch_contents.append(item)


kanga = Kangaroo("Kanga")
roo = Kangaroo("Roo")
kanga.put_in_pouch("wallet")
kanga.put_in_pouch("car keys")
kanga.put_in_pouch(roo)

print(kanga)
print(roo)