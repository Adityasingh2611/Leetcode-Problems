class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number: int) -> int:
            total_sum = 0
            while number > 0:
                digit = number % 10          # Last digit nikala
                total_sum += digit ** 2      # Square add kiya
                number = number // 10        # Last digit remove kiya
            return total_sum

        seen = set()
        
        # Loop tab tak chalega jab tak n 1 na ban jaye 
        # ya n kisi purane dekhe huye number pe wapas na aa jaye
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1  