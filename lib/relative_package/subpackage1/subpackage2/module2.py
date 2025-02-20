"""
Module 2 - Demonstrates relative imports from same and parent packages
"""

# Import single function from same package
from .module1 import function1

# Import entire module from parent package
from .. import module3

# Import multiple functions from same package
from .module1 import function2, helper_function

def main():
    # Demonstrate imports from same package
    print("Calling functions from module1:")
    function1()
    function2()
    print("Helper value:", helper_function())
    
    # Demonstrate imports from parent package
    print("\nCalling functions from module3:")
    module3.function1()
    print("Sum:", module3.calculate_sum(5, 3))
    print("Message:", module3.display_message())

if __name__ == "__main__":
    main()
