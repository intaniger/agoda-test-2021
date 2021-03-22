from utils import parse_date


class PR:
    def __init__(self, jsonedPR):
        self.__number = jsonedPR['number']
        self.__title = jsonedPR['title']
        self.__created_at = parse_date(jsonedPR['created_at'])
        self.__state = jsonedPR['state']
        self.__login = jsonedPR['user']['login']

    def __str__(self):
        return 'PR-%d - %s \n\
Created by %s on %s\n\
This PR is %s' % (self.__number, self.__title, self.__login, self.__created_at.strftime("%B %d, %Y"), self.__state)
