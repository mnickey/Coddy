class SecureMessenger:
    def __init__(self, username, password="secure123"):
        # TODO: Initialize the SecureMessenger with username and password
        # TODO: Store username as a public attribute
        self.username = username
        # TODO: Store password as a private attribute using double underscore prefix (__password)
        self.__password = password
        # TODO: Initialize an empty private list for messages (__messages)
        self.__messages = []
        # TODO: Initialize a private counter for login attempts (__login_attempts = 0)
        self.__login_attempts = 0
        # TODO: Initialize a private boolean flag for login status (__is_logged_in = False)
        self.__is_logged_in = False

    def add_message(self, message):
        if self.__is_logged_in:
            self.__messages.append(message)
            return f"Message added: {message}"
        else:
            return f"Error: You must be logged in to add messages"
        # TODO: Check if user is logged in using the private __is_logged_in attribute
        # TODO: If logged in, append the message to the private __messages list
        #       and return exactly: f"Message added: {message}"
        # TODO: If not logged in, return exactly: "Error: You must be logged in to add messages"


    def login(self, password):
        # TODO: Increment the private __login_attempts counter
        # TODO: Compare the provided password with the stored private __password
        # TODO: If passwords match, set private __is_logged_in to True
        #       and return exactly: "Login successful"
        # TODO: If passwords don't match, return exactly: "Login failed: Incorrect password"
        self.__login_attempts += 1
        if password == self.__password:
            self.__is_logged_in = True
            return f"Login successful"
        else:
            return f"Login failed: Incorrect password"

    def get_messages(self):
        # TODO: Check if user is logged in using the private __is_logged_in attribute
        # TODO: If logged in but __messages list is empty, return exactly: "No messages"
        # TODO: If logged in and messages exist, return all messages joined with newlines
        #       using: "\n".join(self.__messages)
        # TODO: If not logged in, return exactly: "Error: You must be logged in to view messages"
        if self.__is_logged_in:
            if len(self.__messages) > 0:
                return "\n".join(self.__messages)
            else:
                return f"No messages"
        else:
            return f"Error: You must be logged in to view messages"

    def get_login_attempts(self):
    # TODO: Return a string with the number of login attempts
    # Format exactly as: f"Login attempts: {self.__login_attempts}"
        return f"Login attempts: {self.__login_attempts}"
