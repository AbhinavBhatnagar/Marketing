import tweepy
import time
from tweepy.error import TweepError

# consumer_key ='tvDWUBs5uLxDKcX46hb9hrRRz'
# consumer_secret='H8eV9R18QeFzrSuj8Iej0q34G54JE0aWRZanVBHaF8A7P4q2FJ'
# access_token='2686774352-ZSE3Huo8guJH12omd2WqNFsex5CmobBcYCv7w3Q'
# access_secret='tG5xVth829giNpdt96KzMRjAOKnQH2RXCskp77mQpuzFU'
# consumer_key ='6fMe5TOT8d9VKfjDwkHLFZIGS'
# consumer_secret='wDpBpzHa42CORI2TxLfIotAb6Xj6L56nE7qqMpXMC46ZXP5fY8'
# access_token='2686774352-RHzenqDp7RRLbd9HMIZDOFquL1PmV0TIEqcDrfB'
# access_secret='HJLvy5hiU3NoYNBnPwY2EKGTQ49e87aY2eEkaBtpN66j5'
consumer_key ='DXdBKyRN1GRGDELKshSAMP6OV'
consumer_secret='5JGhI6NXMCXxvwAnCqGRGoiJJ4WqwWgAVCO4yPb1cDl6SwSrqa'
access_token='3301220526-Mlqg3WXC39b3kdNIT2MknC4xkoduZerlF2FUamP'
access_secret='TK594X1Q0MvHLMj7WjerENqxPTtXwnpCEA7cUQfN0Kc4I'

twitter_analysis = open('twitter_analysis.txt','a+')

def authentication():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_secret)
    # auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    return api


def verify_authentication(api):
    if api.verify_credentials:
        print 'Successfully logged in!!'


def get_ids(api):
    with open('twitter.txt', 'r') as file:
        for lines in file:
            line = lines.rstrip("\n")
            print line
            #get_user_details(api, line)
            get_network_details(api, line)


def get_user_details(api, userid):
    try:
        if userid == '36426236':
            user = api.get_user(screen_name='DavinaViviano')
            return user.followers_count
        else:
            user = api.get_user(user_id=userid)
            return user.followers_count
    except:
        print "No followers_count information found"
        pass

def get_network_details(api, userid):
    try:
        followers = get_user_details(api, userid)
        print "user_id: "+ str(userid) + " followers_count: " + str(followers)
        count = 1
        # if userid == '36426236':
        #     user = tweepy.Cursor(api.followers, screen_name = 'DavinaViviano', count = 5000).items()
        #     #user = tweepy.Cursor(api.friends, screen_name = 'DavinaViviano').items()
        # else:
        user = tweepy.Cursor(api.followers, user_id=userid).items()
            #user = tweepy.Cursor(api.friends, user_id = userid, count = 5000).items()

        while count <= followers:
                try:
                    u = next(user)
                    count += 1
                    print str(u.id) + " " + str(u.screen_name)
                    twitter_analysis.write(str(userid) + '\t' + str(u.id) + '\t' + u.screen_name + '\n')
                except TweepError as e:
                    print e.message
                    print e.reason
                    print e.response
                    time.sleep(15*60)
                    u = next(user)
                    count += 1
                    print str(u.id) + " " + u.screen_name
                    twitter_analysis.write(str(userid) + '\t' + str(u.id) + '\t' + u.screen_name + '\n')

        print "Wrote for user: "+ str(userid)
        return
    except TweepError as e:
        print e.message
        print e.reason
        print e.response
    #     print "No followers information found"
    #     pass

def main():
        api = authentication()
        verify_authentication(api)
        get_ids(api)



if __name__ == '__main__':
    main()
