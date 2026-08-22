class Solution:

  def reverse(self, x: int) -> int:
    INT_MAX = 2**31 - 1  #  2,147,483,647
    INT_MIN = -(2**31)  # -2,147,483,648

    rev = 0
    sign = -1 if x < 0 else 1
    x = abs(x)

    while x != 0:
      pop = x % 10
      x //= 10

      # Check for 32-bit overflow before pushing the next digit
      if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7):
        return 0

      rev = rev * 10 + pop

    return sign * rev