SIMILAR_ACCOUNT="simolifedotcom"
USERNAME="saidmhamdi1"
PASSWORD="Said2003"
from insta import  InstaFollower


inst=InstaFollower()
inst.login(USERNAME,PASSWORD)
inst.find_followers()
inst.follow()