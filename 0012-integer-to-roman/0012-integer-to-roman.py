class Solution:
    def intToRoman(self, num: int) -> str:
        tous = num//1000
        huns = (num-(1000*tous))//100
        tens = (num-((tous*1000)+(huns*100)))//10
        ones = (num-((tous*1000)+(huns*100)+(tens*10)))//1
        th = tous * "M"
        if huns < 4:
            hu = huns * "C"
        elif huns == 4:
            hu = "CD"
        elif huns == 5:
            hu = "D"
        elif huns < 9:
            hu = "D"+((huns-5)*"C")
        elif huns == 9:
            hu = "CM"

        if tens < 4:
            te = tens * "X"
        elif tens == 4:
            te = "XL"
        elif tens == 5:
            te = "L"
        elif tens < 9:
            te = "L"+((tens-5)*"X")
        elif tens == 9:
            te = "XC"
            
        if ones < 4:
            on = ones * "I"
        elif ones == 4:
            on = "IV"
        elif ones == 5:
            on = "V"
        elif ones < 9:
            on = "V"+((ones-5)*"I")
        elif ones == 9:
            on = "IX"
            
        return th+hu+te+on
        