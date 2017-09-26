#! /usr/bin/python
class Song(object):
	
	def __init__(self,lyrics):
		self.lyrics=lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday_song= Song(["Happy birthday to you","I don't know you"])
saints_song=Song(["When the saints","come maarching iiiin"])

happy_bday_song.sing_me_a_song()
saints_song.sing_me_a_song()
happy_bday_song.lyrics.append(saints_song.lyrics)
print happy_bday_song.lyrics
print len(happy_bday_song.lyrics)
happy_bday_song.sing_me_a_song()
raw_input(">")