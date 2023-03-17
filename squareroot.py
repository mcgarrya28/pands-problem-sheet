def sqrt_newton(n, tol=1e-6):
    """
    Estimate the square root of a number using the Newton method.

    Parameters:
    n (float): The number to find the square root of.
    tol (float, optional): The tolerance level for the estimated square root.
                           Defaults to 1e-6.

    Returns:
    float: The estimated square root of the number.
    """
    x0 = n  # Initial guess
    x1 = (x0 + n / x0) / 2  # Newton's method iteration
    while abs(x1 - x0) > tol:  # Keep iterating until convergence
        x0 = x1
        x1 = (x0 + n / x0) / 2
    return x1

print(sqrt_newton(16))
