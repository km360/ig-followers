# Script to determine which IG accounts you do not follow back 
import json
with open('FOLLOWERS_FILE_NAME') as file:
    followers_json = json.load(file)

with open('FOLLOWING_FILE_NAME') as file:
    following_json = json.load(file)

follower_list = []
for follower in followers_json["relationships_followers"]:
    follower_list.append(follower["string_list_data"][0]["value"])

for following in following_json["relationships_following"]:
    if following["string_list_data"][0]["value"] in follower_list:
        follower_list.remove(following["string_list_data"][0]["value"])

for user in follower_list:
    print(user)
