

class MRAvarageFriends():

    def mapper(self, key, value):
        # Extract ages and number of friends
        (userID, name, age, nFriends) = value.split(',')
        print(name)
        
        print(age)
MRAvarageFriends.mapper()
