class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        min_diff = 721
        
        for i in range(len(timePoints)):
            timePoints[i] = self.convertToMinutes(timePoints[i])

        for i in range(len(timePoints)):
            if i == len(timePoints) - 1:
                diff = abs(timePoints[i] - timePoints[0])
            else:
                diff = abs(timePoints[i] - timePoints[i + 1])
            if diff > 720:
                diff = 1440 - diff
            if diff < min_diff:
                min_diff = diff
        # print(min_diff)
        
        return min_diff
    
    def convertToMinutes(self, time):
        time = time.split(":")
        h1 = int(time[0])
        m1 = int(time[1])
        
        return (h1 * 60) + m1
    
        
        

        
