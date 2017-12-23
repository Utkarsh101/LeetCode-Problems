class Solution:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def isValid(self,text):
        
        def matches(open,close):
            openers = "({["
            closers = ")}]"
            return openers.index(open) == closers.index(close)
    
        s = Solution()
        index = 0
        balanced = True
    
        while index < len(text):
            symbol = text[index]
        
            if symbol in ("({["):
                s.push(symbol)
            else:
                if s.isEmpty():
                    balanced = False
                elif symbol in (")}]"):
                    popped = s.pop()
                
                    if not matches(popped,symbol):
                        balanced = False
        
            index += 1
        
        if (balanced and s.isEmpty()):
            return True
        else:
            return False