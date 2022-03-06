
from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType,Rarity,CardClass,Race
from fireplace.actions import Hit

#self.play_card(self.mark1, controller, target=self.mark2)#指定対象に？？する

def SimulateGames_Core_Paladin():
	#PresetGame(pp_CORE_AT_075)
	#PresetGame(pp_CORE_CS2_088)
	#PresetGame(pp_CORE_CS2_089)
	#PresetGame(pp_CORE_CS2_092)
	PresetGame(pp_CORE_CS2_093)#未解決
	#PresetGame(pp_CORE_CS2_097)#未解決
	#PresetGame(pp_CORE_EX1_130)#未解決

class pp_CORE_AT_075(Preset_Play):
    #Your Silver Hand Recruits have +1 Attack
	class1=CardClass.PALADIN#プレーヤー１はパラディン
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player#プレーヤー1
		opponent = controller.opponent#プレーヤー2
		self.mark1=self.exchange_card('CORE_AT_075',controller)#プレーヤー1のハンドにこのカードを入れる。
		self.mark2=self.exchange_card('CS2_101t',controller)#プレーヤー1のハンドにSilver Hand Recruitsを入れる。
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark2, controller)#self.mark2を手元からプレー
		self.play_card(self.mark1, controller)#self.mark1を手元からプレー
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		print("Silver Hand Recruitsにバフがついているかどうかを視認"%())
		for card in controller.field:#フィールドを表示
			self.print_stats ("***",card, show_buff=True)
	pass

class pp_CORE_CS2_088(Preset_Play):
	""" Guardian of Kings
    [Taunt][Battlecry:] Restore #6 Health to your hero. """
	class1=CardClass.PALADIN#プレーヤー１はパラディン
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player#プレーヤー1
		opponent = controller.opponent#プレーヤー2
		self.mark1=self.exchange_card('CORE_CS2_088',controller)#プレーヤー1のハンドにこのカードを入れる。
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		Hit(controller.hero, 10).trigger(opponent)
		#self.play_card(self.mark2, controller)#self.mark2を手元からプレー
		self.play_card(self.mark1, controller)#self.mark1を手元からプレー
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		print("ヒーローの体力が26かどうかを視認"%())
		for card in [controller.hero]:#ハンドを表示
			self.print_stats ("***",card, show_buff=True)
	pass

class pp_CORE_CS2_089(Preset_Play):
	""" Holy Light
    Restore #8 Health to your hero. """
	class1=CardClass.PALADIN#プレーヤー１はパラディン
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player#プレーヤー1
		opponent = controller.opponent#プレーヤー2
		self.mark1=self.exchange_card('CORE_CS2_089',controller)#プレーヤー1のハンドにこのカードを入れる。
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		Hit(controller.hero, 10).trigger(opponent)
		#self.play_card(self.mark2, controller)#self.mark2を手元からプレー
		self.play_card(self.mark1, controller)#self.mark1を手元からプレー
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		print("ヒーローの体力が28かどうかを視認"%())
		for card in [controller.hero]:#ヒーローの体力を表示
			self.print_stats ("***",card, show_buff=True)
	pass

class pp_CORE_CS2_092(Preset_Play):
	""" Blessing of Kings
	Give a minion +4/+4. <i>(+4 Attack/+4 Health)</i> """
	class1=CardClass.PALADIN#プレーヤー１はパラディン
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player#プレーヤー1
		opponent = controller.opponent#プレーヤー2
		self.mark1=self.exchange_card('CORE_CS2_092',controller)#プレーヤー1のハンドにこのカードを入れる。
		self.mark2=self.exchange_card('minionH3',controller)#プレーヤー1のハンドに体力3のミニオンを入れる。
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark2, controller)#self.mark2を手元からプレー
		self.play_card(self.mark1, controller, target=self.mark2)#self.mark1を手元からプレー
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		print("ミニオンにバフがついているかどうかを視認"%())
		for card in controller.field:#フィールドを表示
			self.print_stats ("***",card, show_buff=True)
	pass
    
class pp_CORE_CS2_093(Preset_Play):#フィールドにいるミニオンのスタッツを見る？
    #Deal $2 damage to all enemies.
	class1=CardClass.PALADIN#プレーヤー１はパラディン
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player#プレーヤー1
		opponent = controller.opponent#プレーヤー2
		self.mark1=self.exchange_card('CORE_CS2_093',controller)#プレーヤー1のハンドにこのカードを入れる。
		self.mark2=self.exchange_card('CS2_101t',controller)#プレーヤー1のハンドにSilver Hand Recruitsを入れる。
		self.mark3=self.exchange_card('minionH3',opponent)#プレーヤー2のハンドに体力3のミニオンを入れる
		self.mark4=self.exchange_card('minionH4',opponent)#プレーヤー2のハンドに体力4のミニオンを入れる
		self
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark2, controller)#self.mark2を手元からプレー
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark4, opponent)#self.mark4を手元からプレー
		self.play_card(self.mark3, opponent)#self.mark3を手元からプレー
		#self.play_card(self.mark2, opponent)#
		self.change_turn(opponent)
		self.play_card(self.mark1, controller)#self.mark1を手元からプレー
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		print("相手フィールドのミニオンがダメージを受けているかどうかを視認"%())
		for card in opponent.field:#プレイヤー2のフィールドを表示
			print("field: %s(%s). "%(card, card.id))
		for card in controller.field:#プレイヤー1のフィールドを表示
			print("field: %s(%s). "%(card, card.id))
	pass

class pp_CORE_CS2_097(Preset_Play):#武器を振る？
	""" Truesilver Champion
    Whenever your hero attacks, restore #2_Health to it. """
	class1=CardClass.PALADIN#プレーヤー１はパラディン
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player#プレーヤー1
		opponent = controller.opponent#プレーヤー2
		self.mark1=self.exchange_card('CORE_CS2_092',controller)#プレーヤー1のハンドにこのカードを入れる。
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		Hit(controller.hero, 10).trigger(opponent)
		self.play_card(self.mark1, controller, target=self.mark2)#self.mark1を手元からプレー
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		print("ミニオンにバフがついているかどうかを視認"%())
		for card in controller.field:#フィールドを表示
			self.print_stats ("***",card, show_buff=True)
	pass

class pp_CORE_EX1_130(Preset_Play):
    #Your Silver Hand Recruits have +1 Attack
	class1=CardClass.PALADIN#プレーヤー１はパラディン
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player#プレーヤー1
		opponent = controller.opponent#プレーヤー2
		self.mark1=self.exchange_card('CORE_AT_075',controller)#プレーヤー1のハンドにこのカードを入れる。
		self.mark2=self.exchange_card('CS2_101t',controller)#プレーヤー1のハンドにSilver Hand Recruitsを入れる。
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark2, controller)#self.mark2を手元からプレー
		self.play_card(self.mark1, controller)#self.mark1を手元からプレー
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		print("Silver Hand Recruitsにバフがついているかどうかを視認"%())
		for card in controller.field:#フィールドを表示
			self.print_stats ("***",card, show_buff=True)
	pass