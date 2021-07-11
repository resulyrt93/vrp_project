class SolverException(Exception):
    """
    Raised when OR-Tools solving errors.
    """
    pass


class ValidationException(Exception):
    """
    Raised when route message validation errors.
    """
    pass
