#!/usr/bin/python3


from PR import PR
from issues import Issue
from requests import get


class APP:
    API_HOST = "https://api.github.com"
    TOKEN = "78cf525edf5a950fca3275488d82749634c12cbb"

    def __init__(self, httpGet=get):
        self.__httpGet = httpGet
        self.__repository = input('Repository: ')
        self.__type = input('Type (issues / pull-requests): ')

        if(self.__type == 'pull-requests'):
            self.__data = self.getPullRequests(self.__repository)
        elif(self.__type == 'issues'):
            self.__data = self.getIssues(self.__repository)
        else:
            raise 'OMGOMGOMOGMGOM Wat you have input??!'

    def getPullRequests(self, repoName: str):
        data = []
        pulls = self.__httpGet('%s/repos/%s/pulls' % (self.API_HOST, repoName),
                               headers=self.getAuthHeaders(), params=self.getParams())

        for pjson in pulls.json():
            data.append(PR(pjson))

        return data

    def getIssues(self, repoName: str):
        data = []
        issues = self.__httpGet('%s/repos/%s/issues' % (self.API_HOST, repoName),
                                headers=self.getAuthHeaders(), params=self.getParams())

        for ijson in issues.json():
            data.append(Issue(ijson))
        return data

    def getParams(self, limit=10, sort_by='created', direction='desc'):
        return {
            'per_page': limit,
            'sort': sort_by,
            'direction': direction
        }

    def getAuthHeaders(self):
        return {
            'Authorization': 'token %s' % self.TOKEN
        }

    def __str__(self):
        return '\n'.join([data.__str__() for data in self.__data])


app = APP()
print(app)
