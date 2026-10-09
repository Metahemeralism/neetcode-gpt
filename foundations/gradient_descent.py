class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        
        def obj(x: int):
            return x**2

        def deriv(x):
            return 2 * x

        def update(x, learning_rate):
            return x - learning_rate * deriv(x)

        x = init

        for i in range(iterations):
            x = update(x, learning_rate)
        return round(x,5)

        

        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        pass
