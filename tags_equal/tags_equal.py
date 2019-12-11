def tags_equal(*tags):
    tag1, tag2 = [Tag(tag) for tag in tags]
    return tag1 == tag2


class Tag:
    def __init__(self, tag):
        # get rid of open/closing brackets
        tag = tag[1:-1]

        # split into name, attributes
        name, *attrs = tag.split(" ")
        self.name = name.lower()
        self.attrs = {}

        for attr in attrs:
            key, value = attr.split("=")
            if key.lower() not in self.attrs.keys():
                self.attrs[key.lower()] = value.lower()

    def __eq__(self, other):
        if self.name != other.name:
            return False

        for key, val in self.attrs.items():
            if key in other.attrs.keys():
                if val != other.attrs[key]:
                    return False
            else:
                return False

        return True
