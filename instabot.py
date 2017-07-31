import requests,urllib

token = "4017080823.39781b9.d01466496aa349d39485cb9634729e5d"
secondurl = "&access_token="


def post_comment(mediaId,comment,full_Name):
    url='https://api.instagram.com/v1/media/{0}/comments'.format(mediaId)
    data = {'access_token':token,
            'text': comment
            }
    display=requests.post(url,data)
    display=display.json()
    print full_Name +" commented on your post"

def like_media(mediaId,full_Name):
    data = {'access_token':token}
    mediaurl='https://api.instagram.com/v1/media/'+ mediaId +'/likes'
    display = requests.post(mediaurl,data)
    display= display.json()
    print "your post is liked by "+full_Name

def get_user_media_id(user_id):
    firsturl="https://api.instagram.com/v1/users/"+user_id+"/media/recent/?access_token="
    endpoint = firsturl+token
    display= requests.get(endpoint)
    display = display.json()
    url = display['data'][0]['images']['low_resolution']['url']
    print "your media link is "+url
    return [display['data'][0]['id'],url]


def get_user_id(name):

    firsturl = "https://api.instagram.com/v1/users/search?q="
    endpoint = firsturl + name + secondurl + token
    display = requests.get(endpoint)
    display = display.json()
    user_Id = display['data'][0]['id']
    user_Full_Name=display['data'][0]['full_name']
    if ( display['meta']['code'] == 200):
        print "====================== WELCOME TO INSTABOT ============================"

        if len(display['data']) == 0:
            print("user not found")
        else:
            print "((((((((((((((((((( "+user_Full_Name+" )))))))))))))))))))))"
            print"your id is : "+user_Id
            user_choice = raw_input("what do you want to do ? \n\n1. like a post \n2.comment on a post\n3.Download post"
                                    "\n")
            mediaId_url = get_user_media_id(user_Id)
            if (user_choice == '1'):
                like_media(mediaId_url[0],user_Full_Name)
            elif (user_choice == '2'):
                comment = raw_input("enter your comment ")
                post_comment(mediaId_url[0],comment,user_Full_Name)
            elif(user_choice == '3'):
                urllib.urlretrieve(mediaId_url[1],'post.jpg')
            else:
                print("wrong choice ")

    else:
        print"request not accepted"

user_name=raw_input("enter username")
get_user_id(user_name)
