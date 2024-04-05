import ao
import mad
import wave
import thread	

class SSound:
	def __init__(self, path):
		self.file = path
		self.format = lower(path.split(".")[-1])
		if self.format == "mp3" or self.format == "mp2" or self.format == "mp1":
			self.sound = mad.MadFile(self.file)
			self.samplerate = self.sound.samplerate()

		if self.format == "wav" or self.format == "wave":
			self.sound = wave.open(self.file,"r")
			self.samplerate = self.sound.getframerate()

		if self.format == "wav" or self.format == "wave":
			self.sound = wave.open(self.file,"r")
			self.samplerate = self.sound.getframerate()
			

	def PlaySound(self, vol, *pos):
		thread.start_new_thread(self._play,())

	def _play(self):
		dev = ao.AudioDevice('alsa', self.samplerate)
		while 1:
			buf = self.sound.read(1)
			if buf is None:
				break
			dev.play(buf, len(buf))
