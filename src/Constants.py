from re import escape

# CONSTANTS FOR REGEX VALUES
FIND_WORD_REGEX_VALUE=r'(?:\w+|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
FIND_URL_REGEX_VALUE = r'http[s]?://(?:\w+|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
FIND_EMAIL_REGEX_VALUE = r"^((?!\.)[\w\-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])$"
# ISSUES WITH:
# FIND_BASE64_REGEX_VALUE = r'^[-A-Za-z0-9+/]*={0,3}$'