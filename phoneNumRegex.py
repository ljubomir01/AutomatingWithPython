#Searching phone number patterns using Regex
"""Import the regex module with import re.
Create a Regex object with the re.compile() function. (Remember to use
a raw string.)
Pass the string you want to search into the Regex object’s search()
method. This returns a Match object.
Call the Match object’s group() method to return a string of the actual
matched text."""
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
