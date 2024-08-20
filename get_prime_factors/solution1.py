from typing import List


class Solution:
    def get_prime_factors(self, num: int) -> List[int]:
        factors = []
        divisor = 2

        while divisor <= num:
            if num % divisor == 0:
                factors.append(divisor)
                num = num // divisor
            else:
                divisor += 1

        return factors