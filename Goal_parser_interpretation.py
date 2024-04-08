 class Solution:
    def interpret(self, command: str) -> str:
        res = command.replace("()","o")
        res = result.replace("(al)","al")
        return res
