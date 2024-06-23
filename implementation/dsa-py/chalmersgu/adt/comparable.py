# Note: by implementing these methods,
# one can use the standard Python comparison operators (==, !=, <, <=, >, >=).
class Comparable:
    def __eq__(self, other): """Test if self == other."""
    def __ne__(self, other): """Test if self != other."""
    def __lt__(self, other): """Test if self < other."""
    def __le__(self, other): """Test if self <= other."""
    def __gt__(self, other): """Test if self > other."""
    def __ge__(self, other): """Test if self >= other."""
