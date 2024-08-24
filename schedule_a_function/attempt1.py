from sched import scheduler
from time import time, sleep,  asctime, localtime


class Solution:
    def schedule_function(self, event_time, function, *args):
        s = scheduler(time, sleep)
        s.enterabs(event_time, 1, function, argument=args)
        print(
            f'{function.__name__}() sceduled for ' +
            f'{asctime(localtime(event_time))}'
        )
        s.run()


def main():
    obj = Solution()
    obj.schedule_function(time() + 1, print, 'Howdy!')


if __name__ == '__main__':
    main()