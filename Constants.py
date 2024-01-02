from re import escape


FIND_WORD_REGEX_VALUE=rescape(word)+r'(?:\w+|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
FIND_URL_REGEX_VALUE = r'http[s]?://(?:\w+|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
FIND_EMAIL_REGEX_VALUE = r"^((?!\.)[\w\-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])$"
FIND_BASE64_REGEX_VALUE = r'^(?:([a-z0-9A-Z+\/]){4})*(?1)(?:(?1)==|(?1){2}=|(?1){3})$'