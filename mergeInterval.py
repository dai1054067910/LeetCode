# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals)==0:
            return intervals
        def quickSort(intervals, start_index, end_index):
            def swap(intervals, i, j):
                tmp = intervals[i]
                intervals[i]=intervals[j]
                intervals[j] = tmp
            if end_index<=start_index:
                return
            i=start_index
            j=end_index
            label = intervals[end_index].start
            while i<j:
                while (i<j) & (intervals[i].start<label):
                    i+=1
                while j>=start_index & (intervals[j].start>=label):
                    j-=1
                if i<j:
                    swap(intervals, i, j)
            swap(intervals, i, end_index)

            quickSort(intervals, start_index, i-1)
            quickSort(intervals, i+1, end_index)
            
        def mergeOverLap(intervals):
            small = intervals[0].start
            big = intervals[0].end
            index = 1
            result_index = 0
            while index<len(intervals):
                if intervals[index].start<=big:
                    big = intervals[index].end
                    intervals[result_index].start = small
                    intervals[result_index].end = big
                    print('dont add result_index, index:{}, result_index:{}, intervals[index].start:{}, small:{}, big:{}'.format(index, result_index, intervals[index].start, small, big ))
                else:
                    small = intervals[index].start
                    big = intervals[index].end
                    result_index+=1
                    print('add result_index, index:{}, result_index:{}, intervals[index].start:{}, small:{}, big:{} '.format(index, result_index, intervals[index].start, small, big ))
                index+=1
            return intervals[0:result_index]
        quickSort(intervals, 0, len(intervals)-1)
        for interval in intervals:
            print(interval.start, interval.end)
        return mergeOverLap(intervals)

class1 = Interval(1,3)
class2 = Interval(2, 6)
class3 = Interval(8, 10)
class4 = Interval(15, 18)
a = [class1, class2, class3, class4]
solution = Solution()
solution.merge(a)