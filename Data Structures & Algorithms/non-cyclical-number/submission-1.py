class Solution:
    def isHappy(self, n: int) -> bool:
        saved = {}

        my_num = n

        while True:
            if my_num in saved:
                return False
            num_str = str(my_num)
            new_num = 0
            for digit in num_str:
                new_num += int(digit) ** 2
            
            if new_num == 1:
                return True
            
            saved[my_num] = new_num
            my_num = new_num