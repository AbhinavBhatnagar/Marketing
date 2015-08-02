__author__ = 'abhatna4'

import tweepy
import time

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


twitter_analysis = open('twitter_analysis_friend.txt','w')

def authentication():
    auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    return api


def verify_authentication(api):
    if api.verify_credentials:
        print 'Successfully logged in!!'


def get_ids(api):
    with open('twitter.txt', 'r') as file:
        for lines in file:
            line = lines.rstrip("\n")
            get_network_details(api, line)


def get_user_details(api, userid):
    try:
        if userid == '36426236':
            user = api.get_user(screen_name='DavinaViviano')
            return user.friends_count
        else:
            user = api.get_user(user_id=userid)
            return user.friends_count
    except:
        print "No followers_count information found"
        pass

def get_network_details(api, userid):
    #try:
        if userid == '36426236':
            user = tweepy.Cursor(api.friends, screen_name = 'DavinaViviano', count = 5000).items()
        else:
            user = tweepy.Cursor(api.friends, user_id = userid, count = 5000).items()

        followers = get_user_details(api, userid)
        print "user_id: "+ str(userid) + " friends_count: " + str(followers)
        count = 1


        while count <= followers:
                try:
                    u = next(user)
                    count += 1
                    print u.id + " " + u.screen_name
                    twitter_analysis.write(str(userid) + '\t' + str(u.id) + '\t' + u.screen_name + '\n')
                    print "wrote"
                except:
                    print 'We got a timeout ... Sleeping for 15 minutes'
                    time.sleep(15*60)
                    u = next(user)
                    count += 1
                    print u.id + " " + u.screen_name
                    twitter_analysis.write(str(userid) + '\t' + str(u.id) + '\t' + u.screen_name + '\n')
                    print "wrote"
        return
    # except:
    #     print "No followers information found"
    #     pass

def main():
        api = authentication()
        verify_authentication(api)
        get_ids(api)



if __name__ == '__main__':
    main()