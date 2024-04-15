 class Solution:
    def interpret(self, command: str) -> str:
        res = command.replace("()","o")
        res = res.replace("(al)","al")
        return res
