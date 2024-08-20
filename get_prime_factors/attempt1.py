from typing import List


class Solution:
    def get_prime_factors(self, num: int) -> List[int]:
        result = []

        def dfs(factor: int, divisor: int) -> None:
            if self.is_prime(factor):
                result.append(factor)
                return
            if factor % divisor == 0:
                self.dfs(divisor, divisor)
                self.dfs(factor // divisor, divisor)
            else:
                divisor += 1
                self.dfs(factor, divisor)

        dfs(num, 2)     
        return result
            
    def is_prime(self, num: int) -> bool:
        for n in range(2, int(num**0.5) + 1):
            if num % n == 0:
                return False
            
        return True