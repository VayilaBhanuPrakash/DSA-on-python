class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if (int(ord(coordinates[0]))%2==0 and int(coordinates[1])%2==0) or (int(ord(coordinates[0]))%2!=0 and int(coordinates[1])%2!=0):
            return False
        return True
        
        