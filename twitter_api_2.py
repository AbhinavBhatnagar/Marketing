__author__ = 'abhatna4'



import tweepy
import time

consumer_key ='DXdBKyRN1GRGDELKshSAMP6OV'
consumer_secret='5JGhI6NXMCXxvwAnCqGRGoiJJ4WqwWgAVCO4yPb1cDl6SwSrqa'
access_token='3301220526-Mlqg3WXC39b3kdNIT2MknC4xkoduZerlF2FUamP'
access_secret='TK594X1Q0MvHLMj7WjerENqxPTtXwnpCEA7cUQfN0Kc4I'

twitter_analysis = open('twitter_analysis_2.txt','w')

def authentication():
    auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    return api


def verify_authentication(api):
    if api.verify_credentials:
        print 'Successfully logged in!!'


def get_ids(api):
    with open('twitter_2.txt', 'r') as file:
        for lines in file:
            line = lines.rstrip("\n")
            #get_user_details(api, line)
            get_network_details(api, line)


def get_user_details(api, userid):
    print userid
    try:
        if userid == '36426236':
            user = api.get_user(screen_name='DavinaViviano')
            return user.followers_count
        else:
            user = api.get_user(user_id=userid)
            return user.followers_count
    except:
        pass

def get_network_details(api, userid):
    try:
        if userid == '36426236':
            user = tweepy.Cursor(api.followers, screen_name = 'DavinaViviano').items()
            #user = tweepy.Cursor(api.friends, screen_name = 'DavinaViviano').items()
        else:
            user = tweepy.Cursor(api.followers, user_id = userid, count = 5000).items()
            #user = tweepy.Cursor(api.friends, user_id = userid, count = 5000).items()

        followers = get_user_details(api, userid)
        print followers
        count = 1


        while count <= followers:
                try:
                    u = next(user)
                    count += 1
                    print u.screen_name
                    twitter_analysis.write(userid+'\t'+u.id+'\t'+u.screen_name +' \n')
                except:
                    print 'We got a timeout ... Sleeping for 15 minutes'
                    time.sleep(15*60)
                    u = next(user)
                    count += 1
                    print u.screen_name
                    twitter_analysis.write(userid+'\t'+u.id+'\t'+u.screen_name +' \n')
        return
    except:
        pass

def main():
        api = authentication()
        verify_authentication(api)
        get_ids(api)



if __name__ == '__main__':
    main()