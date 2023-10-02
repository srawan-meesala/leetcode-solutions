class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        if n<3:
            return False
        i = 1
        alice = 0
        bob = 0
        if i < len(colors)-1:
            while True:
                if colors[i-1]==colors[i] and colors[i]==colors[i+1] and colors[i]=='A':
                    colors = colors[:i]+colors[i+1:]
                    alice += 1
                else:
                    i+=1
                if i >= len(colors)-1:
                    break

        j = 1
        if j < len(colors)-1:
            while True:
                if colors[j-1]==colors[j] and colors[j]==colors[j+1] and colors[j]=='B':
                    colors = colors[:j]+colors[j+1:]
                    bob += 1
                else:
                    j+=1
                if j >= len(colors)-1:
                    break

        if alice>bob:
            return True
        else:
            return False