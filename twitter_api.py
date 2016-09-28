import tweepy
import time
from tweepy.error import TweepError



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
