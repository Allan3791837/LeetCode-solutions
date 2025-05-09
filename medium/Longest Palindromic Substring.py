"""Problem description URL:
https://leetcode.com/problems/longest-palindromic-substring/description/
"""
def longest_palindrome():
    str = input("Type something: ")
    while len(str) > 1000:
        str = input(
            "Sentences that contain more than 1000 characters are not allowed. Try again: "
        )
    import re

    while re.search(r"\W", str):
        str = input("Only English letters are allowed. Try again: ")
    longest_palindromic = ""
    for index, char in enumerate(str):
        for i in range(index, len(str)):
            is_palindromic = str[
                index : i + 1
            ]  # substring that is going to be verified as palindromic or not
            if (
                is_palindromic == is_palindromic[::-1]
                and len(is_palindromic) > len(longest_palindromic)
                and len(is_palindromic) > 1
            ):  # to verify if the substring attends the requirements of the exercise
                longest_palindromic = is_palindromic
    return longest_palindromic


print(longest_palindrome())
input("Press enter to quit")
