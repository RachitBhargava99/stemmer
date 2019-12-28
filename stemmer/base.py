class BaseStemmer:
    """
    Base Stemmer class to store basic information.
    This class is inherited by all the other Stemmer classes.

    ...

    Attributes
    ----------
    _word : str
        the initial word given by the user
    _stemmer : str
        name of the stemmer requested to be used
    """

    def __init__(self, word, s_name):
        """
        Parameters
        ----------
        word : str
            the initial word provided by the user
        s_name : str
            name of the stemmer requested to be used
        """
        self._word = word
        self._stemmer = s_name
