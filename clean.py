__author__ = 'abhatna4'

import sys

def main():
    counter = 0
    twitter_count = 0
    fb_count = 0
    ln_count = 0
    twitter_ids = open('twitter.txt','w')
    facebook_ids = open('facebook.txt','w')
    linked_ids = open('linkedin.txt','w')
    with open('Abhinav.txt', 'r') as file:
        for lines in file:
            if "UserID" in lines:
                print lines
                counter += 1
                if 'twitter' in lines:
                    ids = lines.split(",")
                    for id in ids:
                        if 'twitter' in id:
                            sep = id.split("""'""")
                            get_id = sep[1].split("@")[0]+"\n"
                            twitter_ids.write(get_id)
                    twitter_count += 1

                if 'facebook' in lines:
                    ids = lines.split(",")
                    for id in ids:
                        if 'facebook' in id:
                            sep = id.split("""'""")
                            get_id = sep[1].split("@")[0]+"\n"
                            facebook_ids.write(get_id)

                    fb_count += 1

                if 'linkedin' in lines:
                    ids = lines.split(",")
                    for id in ids:
                        if 'linkedin' in id:
                            sep = id.split("""'""")
                            get_id = sep[1].split("@")[0]+"\n"
                            linked_ids.write(get_id)

                    ln_count += 1
    print counter
    print twitter_count
    print fb_count
    print ln_count





if __name__ == "__main__":
    main()

