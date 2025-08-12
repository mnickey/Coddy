from customlist import CustomList


def test_basic_functionality():
    """Test basic CustomList functionality"""
    try:
        # Test initialization
        empty_list = CustomList()
        assert len(empty_list) == 0, f"Empty list should have length 0, but has {len(empty_list)}"
        
        init_list = CustomList([1, 2, 3])
        assert len(init_list) == 3, f"Initialized list should have length 3, but has {len(init_list)}"
        
        # Test indexing
        assert init_list[0] == 1, f"First element should be 1, but got {init_list[0]}"
        init_list[1] = 10
        assert init_list[1] == 10, f"Element after assignment should be 10, but got {init_list[1]}"
        
        # Test string representation
        assert str(init_list) == "[1, 10, 3]", f"String representation incorrect, got {str(init_list)}"
        
        # Test addition
        combined = init_list + CustomList([4, 5])
        assert len(combined) == 5, f"Combined list should have length 5, but has {len(combined)}"
        assert combined[3] == 4, f"Fourth element of combined list should be 4, but got {combined[3]}"
        
        # Test iteration and contains
        items = []
        for item in combined:
            items.append(item)
        assert items == [1, 10, 3, 4, 5], f"Iteration produced incorrect items: {items}"
        
        assert 10 in combined, "10 should be in the list"
        assert 7 not in combined, "7 should not be in the list"
        
        # Test append and pop
        combined.append(6)
        assert len(combined) == 6, f"After append, length should be 6, but got {len(combined)}"
        assert combined[5] == 6, f"Last element after append should be 6, but got {combined[5]}"
        
        popped = combined.pop()
        assert popped == 6, f"Popped value should be 6, but got {popped}"
        assert len(combined) == 5, f"After pop, length should be 5, but got {len(combined)}"
        
        # Test clear
        combined.clear()
        assert len(combined) == 0, f"After clear, length should be 0, but got {len(combined)}"
        
        print("Basic functionality tests passed!")
        return True
    except Exception as e:
        print(f"Basic functionality test failed: {e}")
        return False


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    try:
        # Test with empty list operations
        empty_list = CustomList()
        
        # Test pop on empty list
        try:
            empty_list.pop()
            assert False, "pop() on empty list should raise IndexError"
        except IndexError:
            pass  # Expected behavior
        
        # Test indexing on empty list
        try:
            value = empty_list[0]
            assert False, "Indexing empty list should raise IndexError"
        except IndexError:
            pass  # Expected behavior
            
        # Test with None values
        none_list = CustomList([None, None])
        assert len(none_list) == 2, f"List with None values should have length 2, got {len(none_list)}"
        assert none_list[0] is None, "First element should be None"
        
        # Test with mixed types
        mixed_list = CustomList([1, "string", 3.14, [1, 2], {"key": "value"}])
        assert len(mixed_list) == 5, f"Mixed type list should have length 5, got {len(mixed_list)}"
        assert mixed_list[1] == "string", f"Second element should be 'string', got {mixed_list[1]}"
        
        # Test adding with regular list
        result = mixed_list + [6, 7, 8]
        assert len(result) == 8, f"After adding regular list, length should be 8, got {len(result)}"
        assert result[5] == 6, f"Sixth element should be 6, got {result[5]}"
        
        # Test adding with empty list
        result = mixed_list + []
        assert len(result) == 5, f"After adding empty list, length should be 5, got {len(result)}"
        assert result[0] == 1, f"First element should still be 1, got {result[0]}"
        
        # Test repr
        repr_str = repr(CustomList([1, 2, 3]))
        assert repr_str == "CustomList([1, 2, 3])", f"repr should be 'CustomList([1, 2, 3])', got {repr_str}"
        
        print("Edge case tests passed!")
        return True
    except Exception as e:
        print(f"Edge case test failed: {e}")
        return False


def test_large_lists():
    """Test performance with large lists"""
    try:
        # Create and test operations on large lists
        # Create a large list
        large_list = CustomList(range(10000))
        assert len(large_list) == 10000, f"Large list should have length 10000, got {len(large_list)}"
        
        # Test indexing on large list
        assert large_list[9999] == 9999, f"Last element should be 9999, got {large_list[9999]}"
        
        # Test contains on large list
        assert 5000 in large_list, "5000 should be in the large list"
        assert 10001 not in large_list, "10001 should not be in the large list"
        
        # Test addition of two large lists
        other_large = CustomList(range(10000, 20000))
        combined = large_list + other_large
        assert len(combined) == 20000, f"Combined large lists should have length 20000, got {len(combined)}"
        assert combined[0] == 0, f"First element should be 0, got {combined[0]}"
        assert combined[19999] == 19999, f"Last element should be 19999, got {combined[19999]}"
        
        print("Large list tests passed!")
        return True
    except Exception as e:
        print(f"Large list test failed: {e}")
        return False


def test_nested_lists():
    """Test with nested CustomList objects"""
    try:
        # Test nested CustomList objects
        inner1 = CustomList([1, 2, 3])
        inner2 = CustomList([4, 5, 6])
        outer = CustomList([inner1, inner2, 7])
        
        assert len(outer) == 3, f"Outer list should have length 3, got {len(outer)}"
        assert outer[0] is inner1, "First element should be inner1"
        assert len(outer[0]) == 3, f"First inner list should have length 3, got {len(outer[0])}"
        assert outer[0][1] == 2, f"Second element of first inner list should be 2, got {outer[0][1]}"
        
        # Test modifying inner list
        inner1.append(4)
        assert len(outer[0]) == 4, f"After append, inner list should have length 4, got {len(outer[0])}"
        assert outer[0][3] == 4, f"Fourth element of inner list should be 4, got {outer[0][3]}"
        
        # Test nested addition
        result = outer[0] + outer[1]
        assert len(result) == 7, f"Combined inner lists should have length 7, got {len(result)}"
        assert result[0] == 1, f"First element should be 1, got {result[0]}"
        assert result[6] == 6, f"Last element should be 6, got {result[6]}"
        
        print("Nested list tests passed!")
        return True
    except Exception as e:
        print(f"Nested list test failed: {e}")
        return False


def test_custom_operations():
    """Test custom operations and combinations"""
    try:
        # Test custom operations and method combinations
        # Test chained operations
        list1 = CustomList([1, 2])
        list2 = CustomList([3, 4])
        list3 = CustomList([5, 6])
        
        # Chain additions
        result = list1 + list2 + list3
        assert len(result) == 6, f"Chained addition should have length 6, got {len(result)}"
        assert result[5] == 6, f"Last element should be 6, got {result[5]}"
        
        # Test append and pop sequence
        test_list = CustomList([1, 2, 3])
        test_list.append(4)
        test_list.append(5)
        assert test_list.pop() == 5, "First pop should return 5"
        assert test_list.pop() == 4, "Second pop should return 4"
        assert len(test_list) == 3, f"After two pops, length should be 3, got {len(test_list)}"
        
        # Test clear and then append
        test_list.clear()
        assert len(test_list) == 0, f"After clear, length should be 0, got {len(test_list)}"
        test_list.append(10)
        assert len(test_list) == 1, f"After append to cleared list, length should be 1, got {len(test_list)}"
        assert test_list[0] == 10, f"Element should be 10, got {test_list[0]}"
        
        # Test adding empty lists
        empty1 = CustomList()
        empty2 = CustomList()
        empty_sum = empty1 + empty2
        assert len(empty_sum) == 0, f"Sum of empty lists should be empty, got length {len(empty_sum)}"
        
        print("Custom operations tests passed!")
        return True
    except Exception as e:
        print(f"Custom operations test failed: {e}")
        return False


# Run the selected test or all tests
test_case = input()

if test_case == "basic":
    test_basic_functionality()
elif test_case == "edge":
    test_edge_cases()
elif test_case == "large":
    test_large_lists()
elif test_case == "nested":
    test_nested_lists()
elif test_case == "custom":
    test_custom_operations()
else:
    print("Invalid test case. Running basic tests by default.")
    test_basic_functionality()
