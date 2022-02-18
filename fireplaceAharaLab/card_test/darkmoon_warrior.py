from .simulate_game import Preset_Play,PresetGame

def SimulateGames_Darkmoon_Warrior():
	PresetGame(pp_DMF_522)#

##################################

class pp_DMF_522(Preset_Play):
	"""Minefield
	Deal 5 damage randomly split among all minions."""
	const1 = 0
	const2 = 0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('DMF_522',controller)#Minefield
		self.mark2=self.exchange_card('vanillaH3',opponent)#vanilla
		self.mark3=self.exchange_card('vanillaH2',opponent)#vanilla
		self.mark4=self.exchange_card('vanillaH2',controller)#vanilla
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark4, controller)#バニラ
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark2, opponent)#バニラ
		self.play_card(self.mark3, opponent)#バニラ
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller)#Minefield
		self.change_turn(controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		hero = controller.opponent.hero
		## 5ダメージを「生きているミニオン」に当てたい。
		print("mark2: health:%d<-3, zone:%s"%(self.mark2.health, self.mark2.zone))
		print("mark3: health:%d<-2, zone:%s"%(self.mark3.health, self.mark3.zone))
		print("mark4: health:%d<-2, zone:%s"%(self.mark4.health, self.mark4.zone))
		pass

##################################

