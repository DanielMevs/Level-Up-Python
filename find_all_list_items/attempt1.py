class Solution:
    def find_all_list_items(self, nums, target):
        result = []

        def dfs(current, temp):
            for i, element in enumerate(current):
                if isinstance(element, list):
                    temp.append(i)
                    dfs(element, temp)
                    temp.pop()
                if element == target and temp:
                    result.append(temp)
                elif element == target and not temp:
                    result.append(element)
        
        dfs(nums, [])
        return result
        
