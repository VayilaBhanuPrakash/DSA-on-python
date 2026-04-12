class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n=len(asteroids)
        l=[]
        i=0
        while i<n:
            if len(l)==0:
                l.append(asteroids[i])
                i+=1
            else:
                while i<n and len(l) and asteroids[i]>0 and l[-1]>0:
                    l.append(asteroids[i])
                    i+=1
                while i<n and len(l) and asteroids[i]<0 and l[-1]<0:
                    l.append(asteroids[i])
                    i+=1
                while i<n and len(l) and asteroids[i]>0 and l[-1]<0:
                    """if asteroids[i]>-l[-1]:
                        pass
                        #l.append(asteroids[i])
                        #i+=1
                    elif asteroids[i]<-l[-1]:
                        l.append(asteroids[i])
                        i+=1
                    else:
                        l.append(asteroids[i])
                        i+=1"""
                    l.append(asteroids[i])
                    i+=1
                while i<n and  len(l) and asteroids[i]<0 and l[-1]>0:
                    if -asteroids[i]>l[-1]:
                        l.pop()
                        #l.append(asteroids[i])
                        #i+=1
                    elif -asteroids[i]<l[-1]:
                        i+=1
                    else:
                        l.pop()
                        i+=1
        return l
        