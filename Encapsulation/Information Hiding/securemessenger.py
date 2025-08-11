class SecureMessenger:
    def __init__(self, username, password="secure123"):
        # TODO: Initialize the SecureMessenger with username and password
        # TODO: Store username as a public attribute
        # TODO: Store password as a private attribute using double underscore prefix (__password)
        # TODO: Initialize an empty private list for messages (__messages)
        # TODO: Initialize a private counter for login attempts (__login_attempts = 0)
        # TODO: Initialize a private boolean flag for login status (__is_logged_in = False)
        pass
    
    def add_message(self, message):
        # TODO: Check if user is logged in using the private __is_logged_in attribute
        # TODO: If logged in, append the message to the private __messages list
        #       and return exactly: f"Message added: {message}"
        # TODO: If not logged in, return exactly: "Error: You must be logged in to add messages"
        pass
    
    def login(self, password):
        # TODO: Increment the private __login_attempts counter
        # TODO: Compare the provided password with the stored private __password
        # TODO: If passwords match, set private __is_logged_in to True
        #       and return exactly: "Login successful"
        # TODO: If passwords don't match, return exactly: "Login failed: Incorrect password"
        pass
    
    def get_messages(self):
        # TODO: Check if user is logged in using the private __is_logged_in attribute
        # TODO: If logged in but __messages list is empty, return exactly: "No messages"
        # TODO: If logged in and messages exist, return all messages joined with newlines
        #       using: "\
".join(self.__messages)
        # TODO: If not logged in, return exactly: "Error: You must be logged in to view messages"
        pass
    
    def get_login_attempts(self):
        # TODO: Return a string with the number of login attempts
        #       Format exactly as: f"Login attempts: {self.__login_attempts}"
        pass
