class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles_set=set(map(tuple,obstacles))
        #res=[0,0]
        i=0
        j=0
        #direction=["North","East","South","West"]
        di=0
        Max_val=0
        for ele in commands:
            if ele==-2:
                di-=1
            elif ele==-1:
                di+=1
            else:
                if di%4==0 or di%4==-4:
                    for _ in range(ele):
                        j+=1
                        if (i,j) in obstacles_set:
                            j-=1
                            break
                elif di%4==1 or di%4==-3:
                    for _ in range(ele):
                        i+=1
                        if (i,j) in obstacles_set:
                            i-=1
                            break
                elif di%4==2 or di%4==-2:
                    for _ in range(ele):
                        j-=1
                        if (i,j) in obstacles_set:
                            j+=1
                            break
                else:
                    for _ in range(ele):
                        i-=1
                        if (i,j) in obstacles_set:
                            i+=1
                            break
            Max_val=max(Max_val,(i*i+j*j))
            #print(di)
            #print(res)
        return Max_val
        