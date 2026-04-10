class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n=len(image)
        for i in range(n):
            image[i]=image[i][::-1]
        for i in range(n):
            for j in range(len(image[i])):
                image[i][j]=1-image[i][j]
        return image
        