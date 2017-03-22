class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = []
        output = ""
        remainder_1000 = num % 1000
        integer_1000 = num / 1000
        res.append("M"*integer_1000)
        if remainder_1000 < 900:
            num = remainder_1000
        else:
            res.append("CM")
            num = remainder_1000 - 900

        remainder_500 = num % 500
        integer_500 = num / 500
        res.append("D"*integer_500)
        if remainder_500 < 400:
            num = remainder_500
        else:
            res.append("CD")
            num = remainder_500 - 400

        remainder_100 = num % 100
        integer_100 = num / 100
        res.append("C"*integer_100)
        if remainder_100 < 90:
            num = remainder_100
        else:
            res.append("XC")
            num = remainder_100 - 90

        remainder_50 = num % 50
        integer_50 = num / 50
        res.append("L"*integer_50)
        if remainder_50 < 40:
            num = remainder_50
        else:
            res.append("XL")
            num = remainder_50 - 40

        remainder_10 = num % 10
        integer_10 = num / 10
        res.append("X"*integer_10)
        if remainder_10 < 9:
            num = remainder_10
        else:
            res.append("IX")
            num = remainder_10 - 9

        remainder_5 = num % 5
        integer_5 = num / 5
        res.append("V"*integer_5)
        if remainder_5 < 4:
            res.append("I"*remainder_5)
        else:
            res.append("IV")

        for s in res:
            output = output + s
        return output
