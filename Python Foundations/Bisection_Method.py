# The bisection method is a technique for finding the roots of a real-valued function. 
# It works by narrowing down an interval where the square root lies 
# until it converges to a value within a specified tolerance.

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    # Check if the number is negative (square root not defined for negatives in real numbers)
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')

    # Handle the special case when the number is 1
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')

    # Handle the special case when the number is 0
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        # Define the search interval [low, high]
        low = 0
        high = max(1, square_target)  # works for numbers < 1 and > 1
        root = None   # root will remain None if convergence fails
        
        # Iteratively narrow down the interval
        for _ in range(max_iterations):
            mid = (low + high) / 2      # midpoint of current interval
            square_mid = mid**2         # square of midpoint

            # Check if midpoint squared is close enough to target
            if abs(square_mid - square_target) < tolerance:
                root = mid
                break   # stop when within tolerance

            # If square_mid is less than target, search in upper half
            elif square_mid < square_target:
                low = mid
            # Otherwise, search in lower half
            else:
                high = mid

        # If after all iterations no root was found within tolerance
        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    # Return the computed root (or None if not found)
    return root

# Example usage: finding square root of a large number
N = 77878787
square_root_bisection(N)
