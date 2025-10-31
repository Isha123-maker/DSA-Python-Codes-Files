# ==============================================
# 2D Vector Class with Basic Operations
# ==============================================
class R2Vector:
    # Initialize 2D vector with x and y components
    def __init__(self, *, x, y):
        self.x = x
        self.y = y

    # Compute the Euclidean norm (magnitude) of the vector
    def norm(self):
        return sum(val**2 for val in vars(self).values())**0.5

    # Return a human-readable string representation, e.g. (2, 3)
    def __str__(self):
        return str(tuple(getattr(self, i) for i in vars(self)))

    # Return a more detailed string representation for debugging, e.g. R2Vector(x=2, y=3)
    def __repr__(self):
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    # Vector addition: component-wise sum
    def __add__(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    # Vector subtraction: component-wise difference
    def __sub__(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    # Overload the * operator
    # - Scalar multiplication when 'other' is a number
    # - Dot product when 'other' is another vector of the same type
    def __mul__(self, other):
        if type(other) in (int, float):
            # Scale each component by the scalar value
            kwargs = {i: getattr(self, i) * other for i in vars(self)}
            return self.__class__(**kwargs)        
        elif type(self) == type(other):
            # Compute the dot product
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            return sum(args)
        return NotImplemented

    # Equality operator (==): True if all components are equal
    def __eq__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))
        
    # Inequality operator (!=): opposite of equality
    def __ne__(self, other):
        return not self == other

    # Less-than operator (<): compares vector magnitudes
    def __lt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()

    # Greater-than operator (>): compares vector magnitudes
    def __gt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()

    # Less-than-or-equal-to (<=): opposite of greater-than
    def __le__(self, other):
        return not self > other

    # Greater-than-or-equal-to (>=): opposite of less-than
    def __ge__(self, other):
        return not self < other


# ==============================================
# 3D Vector Class — Inherits from R2Vector
# Adds z component and cross product operation
# ==============================================
class R3Vector(R2Vector):
    # Initialize 3D vector with x, y, z components
    def __init__(self, *, x, y, z):
        super().__init__(x=x, y=y)
        self.z = z
        
    # Compute the cross product between two 3D vectors
    def cross(self, other):
        if type(self) != type(other):
            return NotImplemented

        # Cross product formula:
        # (ay*bz - az*by, az*bx - ax*bz, ax*by - ay*bx)
        kwargs = {
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x
        }
        
        # Return a new R3Vector instance representing the cross product
        return self.__class__(**kwargs)


# ==============================================
# Example Usage and Testing
# ==============================================
v1 = R3Vector(x=2, y=3, z=1)
v2 = R3Vector(x=0.5, y=1.25, z=2)

print(f'v1 = {v1}')          # Prints (2, 3, 1)
print(f'v2 = {v2}')          # Prints (0.5, 1.25, 2)

# Vector addition and subtraction
v3 = v1 + v2
print(f'v1 + v2 = {v3}')     # Component-wise addition

v4 = v1 - v2
print(f'v1 - v2 = {v4}')     # Component-wise subtraction

# Dot product
v5 = v1 * v2
print(f'v1 * v2 = {v5}')     # Scalar result

# Cross product
v6 = v1.cross(v2)
print(f'v1 x v2 = {v6}')     # 3D vector result of cross product
