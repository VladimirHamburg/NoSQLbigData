'''
Created on 19.06.2015

@author: marilena
'''
import twitter
import simplejson

def GetFollowerIDs(self, userid=None, cursor=-1, count = 10):
    url = 'http://twitter.com/followers/ids.json'
    parameters = {}
    parameters['cursor'] = cursor
    if userid:
        parameters['user_id'] = userid
        remaining = count
        while remaining > 1:
            remaining -= 1
            json = self._FetchUrl(url, parameters=parameters)
            try:
                data = simplejson.loads(json)
                self._CheckForTwitterError(data)
                except twitterError:
                    break
                return data

def main():
    api = twitter.Api(consumer_key='XXXX',
                      consumer_secret='XXXXX',
                      access_token_key='XXXXX',
                      access_token_secret='XXXXXX')
    user=api.GetUser(screen_name="XXXXXX")
    count = 100 # you can find optimum value by trial & error
    while(#users not empty):
        users=api.GetFollowerIDs(user,count)
