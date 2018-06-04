class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        # Add one to the last digit
        digits[-1] += 1
        if digits[-1] >= 10:
            carry = 1
            digits[-1] -= 10

        # Iterate through the rest of the digits
        # adding carries as necessary
        for i in range(len(digits)-2, -1, -1):
            digits[i] += carry
            carry = 0
            if digits[i] >= 10:
                digits[i] -= 10
                carry = 1

        # If there is a carry at the end, need to add a 1
        # to the start of the list
        if carry == 1:
            digits = [1] + digits

        return digits
