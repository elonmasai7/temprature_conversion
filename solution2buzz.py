class Solution(object):
    def fizzBuzz(self, n):
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer

solution = Solution()

n1 = 3
output1 = solution.fizzBuzz(n1)
print("Input:", n1)
print("Output:", output1)

n2 = 5
output2 = solution.fizzBuzz(n2)
print("Input:", n2)
print("Output:", output2)

n3 = 15
output3 = solution.fizzBuzz(n3)
print("Input:", n3)
print("Output:", output3)
