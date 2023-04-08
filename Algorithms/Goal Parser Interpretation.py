class Solution:
    def interpret(self, command: str) -> str:
        c1=[]
        for i in command:
            c1=command.replace("()","o")
            c1=c1.replace("(al)","al")
        return c1