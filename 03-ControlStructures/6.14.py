###
# influencer
#
facebook = input("Facebook?")
twitter = input("Twitter?")
instagram = input("Instagram?")
if (facebook == "True" and twitter == "True") or (facebook == "True" and instagram == "True") or (twitter == "True" and instagram == "True") :
    print("You're good influencer. ")
else : 
    print("Bad influencer. ")