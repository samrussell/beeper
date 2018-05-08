class Route:
    def __init__(self, prefix, next_hop, as_path, origin):
        self.prefix = prefix
        self.next_hop = next_hop
        self.as_path = as_path
        self.origin = origin

    def __str__(self):
        return "%s via %s (%s) %s" % (self.prefix, self.next_hop, self.as_path, self.origin)

    def __eq__(self, other):
        return self.prefix == other.prefix and \
            self.next_hop == other.next_hop and \
            self.as_path == other.as_path and \
            self.origin == other.origin \