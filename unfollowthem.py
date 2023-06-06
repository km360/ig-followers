# Script to determine which IG accounts do not follow back 
import json

with open('FOLLOWERS_FILE_NAME') as file:
    followers_json = json.load(file)


with open('FOLLOWING_FILE_NAME') as file:
    following_json = json.load(file)

following_list = []
for following in following_json["relationships_following"]:
    following_list.append(following["string_list_data"][0]["value"])

for follower in followers_json["relationships_followers"]:
    if follower["string_list_data"][0]["value"] in following_list:
        following_list.remove(follower["string_list_data"][0]["value"])

for user in following_list:
    print(user)
