from ..utils import *

FaceHunter = []
#	'BAR_032','BAR_032',
#	'BAR_037','BAR_037',
#	'BAR_551',
#	'BAR_721',
#	'BAR_801','BAR_801',
#	'BT_211','BT_211',
#	'CORE_BRM_013','CORE_BRM_013',
#	'CORE_DS1_184','CORE_DS1_184',
#	'DMF_087','DMF_087',
#	'DMF_088',
#	'SCH_133','SCH_133',
#	'SCH_231','SCH_231',
#	'SCH_279',
#	'SCH_600','SCH_600',
#	'SCH_617','SCH_617',
#	'SCH_713','SCH_713',
#	'SW_321','SW_321',



FaceHunter+=['BAR_032']
#class BAR_032:#OK
#	""" Piercing Shot
#	Deal $6 damage to a minion. Excess damage hits the enemy hero.
#	"""
#	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0}
#	play = HitAndExcessToOther(TARGET,6,ENEMY_HERO)
#	pass



FaceHunter+=['BAR_037','BAR_037e']
#class BAR_037_Warsong_Wrangler(Choice):
#	#Give all copies of it +2/+1 <i>(wherever_they_are)</i>.
#	def choose(self, card):
#		self.next_choice=None
#		super().choose(card)
#		if Config.LOGINFO:
#			print("%s chooses %r"%(card.controller.name, card))
#		for _card in self.cards:
#			if _card is card:
#				if card.type == CardType.HERO_POWER:
#					_card.zone = Zone.PLAY
#				elif len(self.player.hand) < self.player.max_hand_size:
#					if not _card is self.player.hand:
#						_card.zone = Zone.HAND
#		game = card.game
#		cardList = game.decks + game.hands + game.characters
#		for _card in cardList:
#			if _card.id == card.id:
#				Buff(_card,"BAR_037e").trigger(card.controller)
#		pass
#class BAR_037:#OK
#	""" Warsong Wrangler
#	[x][Battlecry:] [Discover] a Beast from your deck. Give all copies of it +2/+1 <i>(wherever_they_are)</i>.
#	"""
#	play = BAR_037_Warsong_Wrangler(CONTROLLER,RANDOM(FRIENDLY_DECK + BEAST)*3)
#	pass
#BAR_037e=buff(atk=2,health=1)


FaceHunter+=['BAR_551']
#class BAR_551:#OK
#	""" Barak Kodobane
#	[x][Battlecry:] Draw a 1, 2,__and 3-Cost spell.
#	"""
#	play = (
#		Give(CONTROLLER,RANDOM(FRIENDLY_DECK+SPELL+(COST==1))),
#		Give(CONTROLLER,RANDOM(FRIENDLY_DECK+SPELL+(COST==2))),
#		Give(CONTROLLER,RANDOM(FRIENDLY_DECK+SPELL+(COST==3)))
#		)
#	pass


FaceHunter+=['BAR_721','BAR_721t','BAR_721t2']
#class BAR_721:#OK
#	"""
#	Mankrik
#	[x][Battlecry:] Help Mankrik find his wife! She was last seen somewhere in your deck.
#	"""
#	play = Shuffle(CONTROLLER,"BAR_721t")
#	pass
#class BAR_721t:#OK OK 22_10_27
#	"""Olgra, Mankrik's Wife
#	[x][Casts When Drawn]	Summon a 3/7 Mankrik,		who immediately attacks		the enemy hero.
#		<Tag enumID="1077" name="CASTSWHENDRAWN" type="Int" value="1"/>
#	"""
#	play = Summon(CONTROLLER,'BAR_721t2'), RegularAttack(FRIENDLY_MINIONS+ID('BAR_721t2'),ENEMY_HERO)
#	pass
#class BAR_721t2:
#	"""Mankrik, Consumed by Hatred
#	vanilla 	"""
#	pass



FaceHunter+=['BAR_801','BAR_035t']
#class BAR_801:#OK
#	""" Wound Prey
#	Deal $1 damage. Summon a 1/1 Hyena with [Rush].
#	"""
#	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_HERO_OR_MINION_TARGET:0}
#	play = (Hit(TARGET,1),Summon(CONTROLLER,'BAR_035t'))
#	pass



FaceHunter+=['BT_211']
class BT_211:
	"""Imprisoned Felmaw
	&lt;b&gt;Dormant&lt;/b&gt; for 2 turns. When this awakens, __attack a random enemy."""
	dormant = 2
	awaken = Attack(SELF, RANDOM_ENEMY_CHARACTER)
	pass



FaceHunter+=['CORE_BRM_013']
#class CORE_BRM_013:# 3 1637
#	""" Quick Shot
#	Deal $3 damage.If your hand is empty, draw a card. """
#	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
#	powered_up = Count(FRIENDLY_HAND - SELF) == 0
#	play = Hit(TARGET, 3), EMPTY_HAND & Draw(CONTROLLER)
#	pass



FaceHunter+=['CORE_DS1_184']
#class CORE_DS1_184:# 3 1637 #
#	""" Tracking
#	[Discover] a card from your deck. """
#	play = GenericChoiceOnDeck(CONTROLLER, FRIENDLY_DECK[:3])
#	pass



FaceHunter+=['DMF_087']
class DMF_087_Action(TargetedAction):
	CONTROLLER=ActionArg()
	DEFENDER=ActionArg()
	def do(self,source,controller,defender):
		excess = source.atk - defender.health
		if excess > 0:
			Hit(controller.opponent.hero, excess).trigger(controller)
		pass
class DMF_087:#OK
	""" Trampling Rhino
	[Rush]. After this attacks and kills a minion, excess damage hits the enemy hero. """
	events = Attack(SELF,ENEMY_MINIONS).on(DMF_087_Action(CONTROLLER,Attack.DEFENDER))
	pass



FaceHunter+=['DMF_088']
class DMF_088_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		CastSecret(card).trigger(self.source)
		pass
class DMF_088:##OK
	""" Rinling's Rifle
	After your hero attacks, [Discover] a [Secret] and cast it. """
	events = Attack(FRIENDLY_HERO).on(DMF_088_Choice(CONTROLLER, RandomSecret()*3))
	pass



FaceHunter+=['SCH_133']
class SCH_133:
	""" Wolpertinger 
	[Battlecry:] Summon a copy of this."""
	play = Summon(CONTROLLER, ExactCopy(SELF))
	pass



FaceHunter+=['SCH_231','SCH_231e']
class SCH_231:
	"""Intrepid Initiate 
	[Spellburst:] Gain +2_Attack."""
	play = OWN_SPELL_PLAY.on(Buff(SELF, "SCH_231e"))#
	pass
SCH_231e = buff(2,0)



FaceHunter+=['SCH_279']
class SCH_279:#OK
	""" Trueaim Crescent SCH_279 
	After your Hero attacks a minion, your minions attack it too. """
	events = Attack(FRIENDLY_HERO,ENEMY_MINIONS).after(#OK for this line
		RegularAttack(FRIENDLY_MINIONS, Attack.DEFENDER)##  need check RegularAttack its validity
	)
	pass



FaceHunter+=['SCH_600','SCH_600t1','SCH_600t2','SCH_600t3','SCH_600t3e']
class SCH_600:#OK
	## Demon Companion SCH_600
	""" Summon a random Demon Companion. """
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	play = Summon(CONTROLLER, RandomID("SCH_600t1", "SCH_600t2", "SCH_600t3"))
class SCH_600t1:
	""" Reffuh """
	pass
class SCH_600t2:
	""" Shima """
	pass
class SCH_600t3:
	""" Kolek
	[x]Your other minions have +1 Attack. """
	update = Refresh(FRIENDLY_MINIONS - SELF, buff="SCH_600t3e")
SCH_600t3e = buff(1,0)



FaceHunter+=['SCH_617','SCH_617e','SCH_617t']
class SCH_617:
	""" Adorable Infestation 
	Give a minion +1/+1. Summon a 1/1 Cub. Add a Cub to your hand. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "SCH_617e"), Summon(CONTROLLER, "SCH_617t"), Give(CONTROLLER, "SCH_617t")
SCH_617e = buff(1, 1)
class SCH_617t:
	pass



FaceHunter+=['SCH_713','SCH_713e','SCH_713e2']
class SCH_713:#OK
	""" Cult Neophyte (Rare)
	[Battlecry:] Your opponent's spells cost (1) more next_turn. """
	play = OWN_TURN_END.on( Buff(CONTROLLER, "SCH_713e"))
	pass
class SCH_713e:
	update = Refresh(ENEMY_HAND + SPELL, buff="SCH_713e2")
	#Spoiled!
SCH_713e2 = buff(cost=1)
#Spoiling



FaceHunter+=['SW_321','SW_321e']
#class SW_321:#OK
#	""" Aimed Shot
#	Deal $3 damage. Your next Hero Power deals 2 more damage. """
#	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_HERO_OR_MINION_TARGET:0}
#	play = (Hit(TARGET,3),Buff(CONTROLLER,'SW_321e'))
#	pass
#class SW_321e:
#	""" Aiming
#	Your next Hero Power deals 2 more damage. """
#	events=Activate(CONTROLLER, HERO_POWER).on(Hit(Activate.TARGET, 2), Destroy(SELF))
#	pass



#############################





