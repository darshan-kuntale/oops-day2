class Instagram:
    def __init__(self, title, description, creator_name, location):
        self.title = title
        self.description = description
        self.creator_name = creator_name
        self.location = location
        self.likes = 0
        self.comments = []   

    def display_title(self):
        print("The title of the reel is", self.title)

    def display_description(self):
        print("The description of the reel is", self.description)

    def display_creator(self):
        print("Creator:", self.creator_name)

    def display_location(self):
        print("Location:", self.location)

    def display_likes(self):
        print("The likes of the reel is", self.likes)

    def display_comments(self):
        print("Comments:", self.comments)

    def liked(self):
        self.likes += 1

    def disliked(self):
        if self.likes > 0:
            self.likes -= 1

    def add_comment(self, comment):
        self.comments.append(comment)



reel1 = Instagram ("dancing", "dancing with friends", "Darshan", "Karnataka")

reel1.liked()
reel1.add_comment("Super Machi")
reel1.add_comment("Awesome")

reel1.display_creator()
reel1.display_location()
reel1.display_comments()
reel1.display_likes()