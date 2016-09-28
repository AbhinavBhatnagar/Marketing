__author__ = 'abhatna4'

import tweepy
import time




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
