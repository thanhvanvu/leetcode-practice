# https://leetcode.com/problems/time-based-key-value-store/description/
# https://www.youtube.com/watch?v=fu2cD_6E8Hw
class TimeMap(object):

    def __init__(self):
        self.time = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.time:
            self.time[key] = [[value, timestamp]]
        else:
            value_time = self.time[key]
            value_time.append([value, timestamp])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """

        result = ''
        if key not in self.time:
            return ""

        value = self.time[key]

        l = 0
        r = len(value) - 1

        while l <= r:
            mid = (l + r) // 2
            if timestamp >= value[mid][1]:
                result = value[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return result

    def print(self):
        print(self.time)


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo", "bar", 1)
obj.set("foo", "bar2", 2)
obj.set("foo", "bar3", 3)
obj.set("foo", "bar4", 4)
obj.set("foo", "bar6", 6)
obj.set("foo", "bar7", 7)
obj.set("thanh", "bar3", 4)
obj.print()
print(obj.get("foo", 5))
