# Tests to see if a is equal to b
def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)

# Tests to see if a is not equal to b
def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)

# Tests to see if the item is in the collection list
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)

# Tests to see if the item is not in the collection list    
def test_not_in(collection, item):
    assert item not in collection, "{0} contains {1}".format(collection, item)
    
# Tests to see if the value is in between the collection list
def test_between_list(collection, value):
    assert max(collection) >= value and min(collection) <= value, "{1} is not in range {0}".format(collection, value)

# Tests to see if the value is in between two values
def test_between_values(lower_limit, upper_limit, value):
    assert lower_limit <= value <= upper_limit, "{0} is not between {1} and {2}".format(value, lower_limit, upper_limit)

def test_exception_was_raised(func, args, message):
    """
    Test that an error gets thrown inside of a given function. Raises
    AssertionError if the error message was different from the expected
    message
    `func` is a reference to the function that is to be called
    `args` is a tuple containing the arguments that are to be provided to
        `func`
    `message` is the string that is expected to be output by the error once
        it's thrown
    """
    try:
        # Call the function and unpack the `args` tuple by using `*`. This
        # will unpack each of the items from the `args` tuple to pass 
        # them into the function as arguments
        func(*args)

        # Execution will cease at this point if the error was successfully
        # thrown, and will move onto the `except` block. If the
        # function was successfully executed without throwing an error, we'll
        # raise an AssertionError here to inform the developer that the
        # function didn't throw an error as expected
        assert False, "Exception was not raised"
    except Exception as e:
        # The message that was thrown will be stored in the exception
        # instance as the first item in the list of `args`. This will allow us
        # to check to see if the message that was thrown is the same as the
        # message that the developer was expecting 
        assert e.args[0] == message, "The message that was provided did not match the message thrown"
        
test_not_equal('world', 'hello')
test_are_equal('hello', 'hello')
test_not_in("hello", "u")
test_between_list([1,2,3,4,5], 3)