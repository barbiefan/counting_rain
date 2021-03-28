ground = list(map(int, input().split()))

#ground = [0,1,0,2,1,0,1,3,2,1,2,1]
#ground = [1000, 999, 1000]

"""
This should be O((5n/2)*max_heigth)

max(ground) is O(n)
+
for i in range(len(ground)//2) is O(n/2)
+
for i in range(left, right+1) is O(n)

and all of that times heigth since it iterates till max(ground) == 0

"""


drops = 0

if ground != []:
    while (max(ground) > 0):

        left, right = None, None
        for i in range(len(ground)//2):
            if ground[i] > 0 and left is None:
                left = i
            
            if ground[-i-1] > 0 and right is None:
                right = len(ground)-i


        if left is None or right is None:
            break


        for i in range(left,right):
            if ground[i] < 1:
                drops += 1
            ground[i] -= 1




print(drops)
print(iterations)
