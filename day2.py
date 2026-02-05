class Instagram:
    def __init__(self, title, description, creator_name, location):  
        self.title = title
        self.description = description
        self.creator_name = creator_name
        self.location = location
        self.likes = 0
        self.comments = [] 

    # Display methods
    def display_title(self):
        print("The title of the reel is:", self.title)

    def display_description(self):
        print("The description of the reel is:", self.description)

    def display_likes(self):
        print("The likes of the reel are:", self.likes)

    def display_creator(self):
        print("The creator of the reel is:", self.creator_name)

    def display_location(self):
        print("The location of the reel is:", self.location)

    def display_comments(self):
        if self.comments:
            print("Comments on the reel:")
            for idx, comment in enumerate(self.comments, start=1):
                print(f"{idx}. {comment}")
        else:
            print("No comments yet.")

    # Interaction methods
    def liked(self):
        self.likes += 1

    def disliked(self):
        if self.likes > 0:
            self.likes -= 1

    def add_comment(self, comment):
        self.comments.append(comment)


reel1 = Instagram("Dancing", "Dancing with friends", "Darshan", "Bengaluru")
reel1.liked()
reel1.add_comment("Super macha")
reel1.add_comment("chindi what a move")

reel2 = Instagram("Finance Minister Conference", "Conference with Finance minister at Delhi", "Pavan", "Delhi")
reel2.liked()
reel2.add_comment("good budget for country but what about middelclass peoples")

reel1.display_title()
reel1.display_description()
reel1.display_creator()
reel1.display_location()
reel1.display_likes()
reel1.display_comments()

reel2.display_title()
reel2.display_description()
reel2.display_creator()
reel2.display_location()
reel2.display_likes()
reel2.display_comments()

print(id(reel1))
print(id(reel2))
