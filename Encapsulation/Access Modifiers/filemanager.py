class FileManager:
    # TODO: Implement the public method read_file(filename) that returns "Reading [filename]"
    # The method should take a filename parameter and return a formatted string
    def read_file(self, filename):
        return f"Reading {filename}"
    
    # TODO: Implement the protected method _check_permissions(filename) that returns "Checking permissions for [filename]"
    # Protected methods in Python are denoted by a single underscore prefix
    # They are still accessible outside the class but indicate they're intended for internal use
    def _check_permissions(self, filename):
        return f"Checking permissions for {filename}"

    # TODO: Implement the private method __decrypt_content(content) that returns "Decrypted: [content]"
    # Private methods in Python are denoted by double underscore prefix
    # They are name-mangled to prevent accidental access from outside the class
    def __decrypt_content(self, content):
        return f"Decrypted: {content}"

    # TODO: Implement the public method get_file_content(filename) that:
    # 1. First calls the protected method _check_permissions(filename)
    # 2. Creates a content string with format "Content of [filename]"
    # 3. Calls the private method __decrypt_content(content) and returns its result
    def get_file_content(self, filename):
        self._check_permissions(filename)
        content = f"Content of {filename}"
        return self.__decrypt_content(content)
