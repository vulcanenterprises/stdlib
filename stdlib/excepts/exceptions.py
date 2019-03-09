"""
exceptions.py
=========================================================
The exceptions.py module for python stdlib
"""
class IllegalArgumentException(BaseException):
    """
    Similar to Java exception. Used when an invalid argument is passed to a function
    """
    def __init__(self, msg=''):
        self.msg = msg

    def __str__(self):
        if self.msg:
            print(self.msg)
            return self.msg

        return ''

    def __repr__(self):
        if self.msg:
            print(self.msg)
            return self.msg

        return ''
