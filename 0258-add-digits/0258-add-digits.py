class Solution(object):

    def subAddDigits(self, num):
        if num < 10:
            return num
        return num%10 + self.subAddDigits(num//10)

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        return self.addDigits(self.subAddDigits(num))
        