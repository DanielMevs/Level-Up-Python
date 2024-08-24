from pickle import dump, load


class Solution:
    def save_dict(self, dictObj: dict, filePath: str) -> None:
        with open(filePath, 'wb') as f:
            dump(dictObj, f)

    def load_dict(self, filePath: str) -> dict:
        with open(filePath, 'rb') as f:
            pulledDict = load(f)
        
        return pulledDict
    

def main():
    filePath = 'myDict.txt'
    myDict = {'one': 1, 'two': 2, 'four': 4, 'seven': 7}
    obj = Solution()
    obj.save_dict(myDict, filePath)
    newDict = obj.load_dict(filePath)
    print(newDict)


if __name__ == '__main__':
    main()
    