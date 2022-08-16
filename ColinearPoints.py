class Solution:
    def fix_fuel_config(self,config):
        #Parse input
        pointsList = [] 
        points = config.split(";")
        for point in points:
            xyVals = point.split(":")
            pointsList.append((xyVals[0],xyVals[1]))

        #If 2 x-values are the same, return "KEEP_PREVIOUS"
        xValsInPointsList = []
        for i in pointsList:
            if i[0] in xValsInPointsList:
                return "KEEP_PREVIOUS"
            else:
                xValsInPointsList.append(i[0])
        #Need to figure out if point are colinear
        #For points A,B,C,D deal with ABC,ABD,ACD,BCD in that order
        #Use the triangle method to test if 3 points are colinear 
        #Triangle method - If area of triangle between 3 points is 0, the points are colinear
        #This will identify if 1 of the points is not colinear, but will only narrow it down to 3
        #A is 0, B is 1, C is 2, D is 3
        aX = pointsList[0][0]
        aY = pointsList[0][1]
        bX = pointsList[1][0]
        bY = pointsList[1][1]
        cX = pointsList[2][0]
        cY = pointsList[2][1]
        dX = pointsList[3][0]
        dY = pointsList[3][1]
        #ABC
        areaABC = (float(aX)*(float(bY)-float(cY))+float(bX)*(float(cY)-float(aY))+float(cX)*(float(aY)-float(bY)))/2
        #ABD
        areaABD = (float(aX)*(float(bY)-float(dY))+float(bX)*(float(dY)-float(aY))+float(dX)*(float(aY)-float(bY)))/2
        #ACD
        areaACD = (float(aX)*(float(cY)-float(dY))+float(cX)*(float(dY)-float(aY))+float(dX)*(float(aY)-float(cY)))/2
        #BCD
        areaBCD = (float(bX)*(float(cY)-float(dY))+float(cX)*(float(dY)-float(bY))+float(dX)*(float(bY)-float(cY)))/2

        #If points are colinear, return input
        if areaABC == 0 and areaABD == 0 and areaACD == 0 and areaBCD == 0:
            return config
        #If 1 point is not colinear, identify which point and fix it   
        elif areaABC == 0 and areaABD != 0 and areaACD != 0 and areaBCD != 0:   
            #The error is point D
            #Make equation of line between A and B
            gradient = (float(aY)-float(bY))/(float(aX)-float(bX))
            y = gradient*(float(dX)-float(aX))+float(aY)
            if float(y) == int(y):
                y = int(y)
            return "%s:%s;%s:%s;%s:%s;%s:%s"%(aX,aY,bX,bY,cX,cY,dX,y)
        elif areaABC != 0 and areaABD == 0 and areaACD != 0 and areaBCD != 0:   
            #The error is point C
            #Make equation of line between A and B
            gradient = (float(aY)-float(bY))/(float(aX)-float(bX))
            y = gradient*(float(cX)-float(aX))+float(aY)
            if float(y) == int(y):
                y = int(y)
            return "%s:%s;%s:%s;%s:%s;%s:%s"%(aX,aY,bX,bY,cX,y,dX,dY)
        elif areaABC != 0 and areaABD != 0 and areaACD == 0 and areaBCD != 0:   
            #The error is point B
            #Make equation of line between A and C
            gradient = (float(aY)-float(cY))/(float(aX)-float(cX))
            y = gradient*(float(bX)-float(aX))+float(aY)
            if float(y) == int(y):
                y = int(y)
            return "%s:%s;%s:%s;%s:%s;%s:%s"%(aX,aY,bX,y,cX,cY,dX,dY)
        elif areaABC != 0 and areaABD != 0 and areaACD != 0 and areaBCD == 0:   
            #The error is point A
            #Make equation of line between B and C
            gradient = (float(bY)-float(cY))/(float(bX)-float(cX))
            y = gradient*(float(aX)-float(bX))+float(bY)
            if float(y) == int(y):
                y = int(y)
            return "%s:%s;%s:%s;%s:%s;%s:%s"%(aX,y,bX,bY,cX,cY,dX,dY)
               
        #If not, return "KEEP_PREVIOUS"
        else:
            return "KEEP_PREVIOUS"

solution=Solution()
print(solution.fix_fuel_config("1:1;2:2;3.5:3.5;4:5"))
