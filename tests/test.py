import requests
import json

# Base URLs for the microservices
SONG_SERVICE_URL = "http://localhost:3001"
PROFILE_SERVICE_URL = "http://localhost:3002"

def print_result(test_name, response):
    decoded = response.json()
    print(json.dumps(decoded, indent=4))
    status = decoded.get('status', 'ERROR')
    message = decoded.get('message', None)
    
    if response.status_code == 200:
        print(f"✅ {test_name} Passed\n\tStatus Code {response.status_code}\n\tStatus: {status}")
        if message is not None:
            print(f"\tMessage: {message}")
    else:
        print(f"❌ {test_name} Failed\n\tStatus Code {response.status_code}\n\tStatus: {status}")
        if message is not None:
            print(f"\tMessage: {message}")
    
    print("-"*50)

# Test Cases

def test_add_song():
    song_data = {
        "songName": "No More Parties in LA",
        "songArtistFullName": "Kanye West",
        "songAlbum": "The Life of Pablo"
        }
    response = requests.post(f"{SONG_SERVICE_URL}/addSong", json=song_data)
    print_result("Add Song", response)

def test_get_song_by_id(song_id):
    response = requests.get(f"{SONG_SERVICE_URL}/getSongById/{song_id}")
    print_result("Get Song by ID", response)

def test_delete_song_by_id(song_id):
    response = requests.delete(f"{SONG_SERVICE_URL}/deleteSongById/{song_id}")
    print_result("Delete Song by ID", response)

def test_update_song_favourites_count(song_id, should_decrement):
    data = {"songId": song_id, "shouldDecrement": should_decrement}
    response = requests.put(f"{SONG_SERVICE_URL}/updateSongFavouritesCount", json=data)
    print_result("Update Song Favourites Count", response)

def test_delete_profile(user_name):
    response = requests.delete(f"{PROFILE_SERVICE_URL}/profile/{user_name}")
    print_result("Delete Profile", response)

def test_add_profile():
    profile_data = {"userName": USERNAME, "fullName": "Test User", "password": "testPassword"}
    response = requests.post(f"{PROFILE_SERVICE_URL}/profile", json=profile_data)
    print_result("Add Profile", response)

def test_follow_friend(user_name, friend_user_name):
    data = {"userName": user_name, "friendUserName": friend_user_name}
    response = requests.put(f"{PROFILE_SERVICE_URL}/followFriend", json=data)
    print_result("Follow Friend", response)

def test_unfollow_friend(user_name, friend_user_name):
    data = {"userName": user_name, "friendUserName": friend_user_name}
    response = requests.put(f"{PROFILE_SERVICE_URL}/unfollowFriend", json=data)
    print_result("Unfollow Friend", response)

def test_like_song(user_name, song_id):
    data = {"userName": user_name, "songId": song_id}
    response = requests.put(f"{PROFILE_SERVICE_URL}/likeSong", json=data)
    print_result("Like Song", response)

def test_unlike_song(user_name, song_id):
    data = {"userName": user_name, "songId": song_id}
    response = requests.put(f"{PROFILE_SERVICE_URL}/unlikeSong", json=data)
    print_result("Unlike Song", response)

def test_get_all_friend_favourite_song_titles(user_name):
    response = requests.get(f"{PROFILE_SERVICE_URL}/getAllFriendFavouriteSongTitles/{user_name}")
    print_result("Get All Friend Favourite Song Titles", response)

def test_find_trending_songs(limit=None):
    params = {}
    if limit is not None:
        params['limit'] = limit
    response = requests.get(f"{SONG_SERVICE_URL}/trending", params=params)
    print_result("Find Trending Songs", response)

def test_get_made_for_you_playlist():
    response = requests.get(f"{SONG_SERVICE_URL}/madeForYou")
    print_result("Get Made For You Playlist", response)



SONG_ID = "5d61728193528481fe5a3125"
USERNAME = "TestUser-23asd1"
FRIEND_USERNAME = "TestUser-1" #i had previously created a user with this username

    # "_id": ObjectId("5d61728193528481fe5a3125"),
    # "songName": "Sanctuary",
    # "songArtistFullName": "Joji",
    # "songAlbum": "Nectar",
    # "songAmountFavourites": 78

# Running Tests
print("🔎 Running Tests for Song and Profile Microservices")
test_add_song()
test_get_song_by_id(SONG_ID)
test_update_song_favourites_count(SONG_ID, "true")
test_update_song_favourites_count(SONG_ID, "false")


test_find_trending_songs()
test_find_trending_songs(5)  # Testing with a limit
test_get_made_for_you_playlist()


test_add_profile()
test_follow_friend(USERNAME, FRIEND_USERNAME)
test_unfollow_friend(USERNAME, FRIEND_USERNAME)
test_like_song(USERNAME, SONG_ID)
test_unlike_song(USERNAME, SONG_ID)
test_get_all_friend_favourite_song_titles(USERNAME)
test_delete_song_by_id(SONG_ID)
