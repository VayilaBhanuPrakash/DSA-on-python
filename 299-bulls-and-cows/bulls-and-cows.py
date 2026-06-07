class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_used = [False] * len(secret)
        guess_used = [False] * len(guess)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                secret_used[i] = True
                guess_used[i] = True
        for i in range(len(secret)):
            if secret_used[i]:
                continue
            for j in range(len(guess)):
                if guess_used[j]:
                    continue
                if secret[i] == guess[j]:
                    cows += 1
                    guess_used[j] = True
                    break
        return f"{bulls}A{cows}B"

        