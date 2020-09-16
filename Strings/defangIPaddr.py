# String problem 1108: Defanging an IP Address

# Given a valid (IPv4) IP address, return a defanged version of that IP.
# A defanged IP address replaces every period "." with "[.]".

# Input: address = "255.100.50.0" --> Output: "255[.]100[.]50[.]0"


class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace('.', '[.]')
