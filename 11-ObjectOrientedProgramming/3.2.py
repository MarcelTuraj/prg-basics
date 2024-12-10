class Music:
    def __init__(self, author, title, album, year):
        self.author = author
        self.title = title
        self.album = album
        self.year = year
    def __str__(self):
        return f"""                 Performer:   {self.author}
                 Title:       {self.title}
                 Album:       {self.album}
                 Year:        {self.year}
                 """

def main():
    music_info1 = Music("Metallica", "No Remorse", "Kill 'em All", 1983)
    print(music_info1)

if __name__ == "__main__":
    main()