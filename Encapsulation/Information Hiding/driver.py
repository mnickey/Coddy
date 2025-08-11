from securemessenger import SecureMessenger

# Test case handler
test_case = input()
if test_case == "default_test":
    # Standard test case from original problem
    messenger = SecureMessenger("user1")
    
    # Try to add messages before login
    print(messenger.add_message("Hello World!"))
    print(messenger.add_message("Secure Message"))
    
    # Attempt login with wrong password
    print(messenger.login("wrong_pass"))
    
    # Login with correct password
    print(messenger.login("secure123"))
    
    # Add messages after successful login
    print(messenger.add_message("Hello World!"))
    print(messenger.add_message("Secure Message"))
    
    # Retrieve messages
    print(messenger.get_messages())
    
    # Check login attempts
    print(messenger.get_login_attempts())
elif test_case == "custom_password":
    # Test with custom password
    messenger = SecureMessenger("admin", "admin123")
    print(messenger.login("wrong_password"))
    print(messenger.login("admin123"))
    print(messenger.get_login_attempts())
elif test_case == "multiple_login_attempts":
    # Test multiple login attempts
    messenger = SecureMessenger("user2")
    print(messenger.login("attempt1"))
    print(messenger.login("attempt2"))
    print(messenger.login("attempt3"))
    print(messenger.login("secure123"))
    print(messenger.get_login_attempts())
elif test_case == "message_management":
    # Test message management
    messenger = SecureMessenger("user3")
    print(messenger.login("secure123"))
    
    # Add multiple messages
    messages = ["Message 1", "Message 2", "Message 3", "Message 4", "Message 5"]
    for msg in messages:
        print(messenger.add_message(msg))
    
    # Verify all messages
    print(messenger.get_messages())
elif test_case == "empty_messages":
    # Test empty messages case
    messenger = SecureMessenger("user4")
    print(messenger.login("secure123"))
    print(messenger.get_messages())
elif test_case == "access_without_login":
    # Test access without login
    messenger = SecureMessenger("user5")
    print(messenger.add_message("Unauthorized message"))
    print(messenger.get_messages())
elif test_case == "attribute_privacy":
    # Test attribute privacy
    messenger = SecureMessenger("user6")
    
    # Public attribute
    print(f"Public username: {messenger.username}")
    
    # Private attributes - these should raise AttributeError
    try:
        print(messenger.__password)
    except AttributeError as e:
        print("Password is private: AttributeError")
    
    try:
        print(messenger.__messages)
    except AttributeError as e:
        print("Messages are private: AttributeError")
    
    try:
        print(messenger.__login_attempts)
    except AttributeError as e:
        print("Login attempts are private: AttributeError")
    
    try:
        print(messenger.__is_logged_in)
    except AttributeError as e:
        print("Login status is private: AttributeError")
elif test_case == "login_logout_sequence":
    # This test requires extending the class with a logout method
    # For testing purposes, we'll create a subclass with logout functionality
    class ExtendedMessenger(SecureMessenger):
        def logout(self):
            self._SecureMessenger__is_logged_in = False
            return "Logged out successfully"
    
    messenger = ExtendedMessenger("user7")
    print(messenger.login("secure123"))
    print(messenger.add_message("Test message"))
    print(messenger.get_messages())
    print(messenger.logout())
    print(messenger.get_messages())
elif test_case == "stress_test":
    # Stress test with many messages
    messenger = SecureMessenger("user8")
    print(messenger.login("secure123"))
    
    # Add 100 messages
    for i in range(1, 101):
        messenger.add_message(f"Message {i}")
    
    # Verify message count
    messages = messenger.get_messages()
    newline_char = '\n'  # Store the newline character in a variable
    message_count = len(messages.split(newline_char))
    print(f"Added 100 messages. Retrieved {message_count} messages.")
