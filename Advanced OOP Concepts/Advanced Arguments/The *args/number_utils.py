def sum_all_numbers(*args):
    # TODO: Check if no arguments were provided
    # TODO: If no arguments, return 0
    if not args:
        return 0
    
    # TODO: Validate that all arguments are numbers (int or float)
    # TODO: Loop through each argument in args
    # TODO: Check if each argument is an instance of int or float using isinstance(arg, (int, float))
    # TODO: If any argument is not a number, print "Error: All arguments must be numbers" and return None
    
    # TODO: If all arguments are valid numbers, return their sum using the sum() function
    for arg in args:
        if not isinstance(arg, (int, float)):
            print("Error: All arguments must be numbers") 
            return None
    
    return sum(args)
