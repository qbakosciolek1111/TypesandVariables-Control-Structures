###
# Checks whether a person is a good influencer:
# has at least two of the accounts: Facebook, Twitter, Instagram
#
facebook = True
twitter = False
instagram = True

accounts = facebook + twitter + instagram

print(f'facebook = {facebook}')
print(f'twitter = {twitter}')
print(f'instagram = {instagram}')

if accounts >= 2:
     print('You are a good influencer!')
else:
    print('You are not a good influencer.')