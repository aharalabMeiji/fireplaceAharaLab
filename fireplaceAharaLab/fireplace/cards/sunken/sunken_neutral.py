from ..utils import *

sunken_neutral=['TSC_001','TSC_002','TSC_003','TSC_003e','TSC_007','TSC_013','TSC_017','TSC_020','TSC_020e','TSC_020e2','TSC_032','TSC_032t','TSC_032t2','TSC_034','TSC_052','TSC_052t','TSC_053','TSC_064','TSC_065','TSC_067','TSC_069','TSC_083e','TSC_632','TSC_632e','TSC_638','TSC_638e','TSC_638t','TSC_638t2','TSC_638t3','TSC_638t4','TSC_640','TSC_641','TSC_641ta','TSC_641tae','TSC_641tb','TSC_641tc','TSC_641td','TSC_641tde','TSC_645','TSC_646','TSC_646t','TSC_647','TSC_647e','TSC_649','TSC_649e2','TSC_823','TSC_823e','TSC_826','TSC_827','TSC_827e','TSC_829','TSC_908','TSC_909','TSC_911','TSC_919','TSC_919t','TSC_926','TSC_928','TSC_935','TSC_938','TSC_960',]

class TSC_001:# <12>[1658]
	""" Naval Mine
	[Deathrattle:] Deal 4 damage to the enemy hero. """
	deathrattle = Hit(ENEMY_HERO, 4)
	pass

class TSC_002:# <12>[1658]
	""" Pufferfist
	After your hero attacks, deal 1 damage to all enemies. """
	events = Attack(FRIENDLY_HERO).after(Hit(ENEMY_CHARACTERS, 1))
	pass

class TSC_003_Action(Choice):
	def choose(self, card):
		super().choose(card)
		if not hasattr(card, 'controller') or not hasattr(card, 'type'):
			return
		log.info("%s chooses %r"%(card.controller.name, card))
		for _card in self.cards:
			if _card is card:
				Buff(_card,'TSC_003e').trigger(self.source)
				break

class TSC_003:# <12>[1658]
	""" Coilfang Constrictor
	[Battlecry:] Look at 3 cards in your opponent's hand and choose one. It can't be played next turn. """
	play = TSC_003_Action(CONTROLLER, RANDOM(ENEMY_HAND)*3)
	pass

TSC_003e=buff(cant_play=True)# <12>[1658]
""" Constricted
Can't be played next turn. """
# NO one_turn_effect

class TSC_007:# <12>[1658]
	""" Gangplank Diver
	[Dormant] for 1 turn.[Rush]. [Immune] while attacking. """
	#		<Tag enumID="791" name="RUSH" type="Int" value="1"/>
	#		<Tag enumID="373" name="IMMUNE_WHILE_ATTACKING" type="Int" value="1"/>
	#		<ReferencedTag enumID="1518" name="DORMANT" type="Int" value="1"/>
	pass

class TSC_013:# <12>[1658]
	""" Slimescale Diver
	[Dormant] for 1 turn.[Rush], [Poisonous] """
	#<Tag enumID="791" name="RUSH" type="Int" value="1"/>
	#<Tag enumID="363" name="POISONOUS" type="Int" value="1"/>
	#<ReferencedTag enumID="1518" name="DORMANT" type="Int" value="1"/>
	pass

class TSC_017:# <12>[1658]###########################
	""" Baba Naga
	[Battlecry:] If you've cast a spell while holding this, deal 3 damage. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0 }
	pass

class TSC_020:# <12>[1658]
	""" Barbaric Sorceress
	[Taunt]. [Battlecry:] Swap the Cost of a random spell in each player's hand. """
	def play(self):
		choice1=[]
		for card in self.controller.hand:
			if card.type==CardType.SPELL:
				choice1.append(card)
		choice2=[]
		for card in self.controller.opponent.hand:
			if card.type==CardType.SPELL:
				choice2.append(card)
		if len(choice1)>0 and len(choice2)>0:
			card1 = random.choice(choice1)
			card2 = random.choice(choice2)
			#card1.cost, card2.cost = card2.cost, card.cost1
			TSC_020e.cost=SET(card2.cost)
			TSC_020e2.cost=SET(card1.cost)
			Buff(card1,'TSC_020e').trigger(self)
			Buff(card2,'TSC_020e2').trigger(self)
	pass	

class TSC_020e:# <12>[1658]
	""" Barbarous
	Attack was swapped. """
	#
	pass
class TSC_020e2:# <12>[1658]
	""" Barbarous
	Cost was swapped. """
	#
	pass

class TSC_032:# <12>[1658]
	""" Blademaster Okani
	[Battlecry:] [Secretly] choose to [Counter] the next minion or spell your opponent plays while this is alive. """
	choose = ('TSC_032t', 'TSC_032t2')
	pass

class TSC_032t:# <12>[1658]
	""" Minion Counter
	[Counter] the next minion your opponent plays. """
	tags = {GameTag.SECRET:1, }
	secret =  Play(OPPONENT, MINION).on(
		Reveal(SELF),
		Destroy(Play.CARD),
		)
	pass

class TSC_032t2:# <12>[1658]
	""" Spell Counter
	[Counter] the next spell your opponent plays. """
	tags = {GameTag.SECRET:1, }
	secret =  Play(OPPONENT, SPELL).on(
		Reveal(SELF),
		Destroy(Play.CARD),
		)
	pass

class TSC_034:# <12>[1658]
	""" Gorloc Ravager
	[Battlecry:] Draw 3 Murlocs. """
	play = Draw(CONTROLLER, RANDOM(FRIENDLY_DECK+MURLOC)) * 3
	pass

class TSC_052:# <12>[1658]################
	""" School Teacher
	[Battlecry:] Add a 1/1 Nagaling to your hand. [Discover] a spell that costs (3) or less to teach it. """
	play = Give(CONTROLLER, 'TSC_052t'), Discover(CONTROLLER, RandomSpell(cost=[3,2,1,0])*3)
	## Discover したspell のbattlecryをTSC_052tに付与する。（どうやって？）
	pass

class TSC_052t:# <12>[1658]
	""" Nagaling
	[Battlecry:] Cast {0}. """
	pass

class TSC_053:# <12>[1658]
	""" Rainbow Glowscale
	[Spell Damage +1] """
	#
	pass

class TSC_064:# <12>[1658]
	""" Slithering Deathscale
	[Battlecry:] If you've cast three spells while holding this, deal 3 damage to all enemies.@ <i>({0} left!)</i>@ <i>(Ready!)</i> """
	class Hand:
		events = OWN_SPELL_PLAY.on(SidequestCounter(SELF, 3, GiveBattlecry(SELF, [Hit(ENEMY_CHARACTERS, 3)])))
	pass

class TSC_065:# <12>[1658]
	""" Helmet Hermit
	Can't attack. """
	#
	pass

class TSC_067:# <12>[1658]
	""" Ambassador Faelin
	[Battlecry:] Put 3 [Colossal] minions on the bottom of your deck. """
	play = PutOnBottom(CONTROLLER, RandomMinion(colossal=True)) * 3
	pass

class TSC_069:# <12>[1658]
	""" Amalgam of the Deep
	[Battlecry:] Choose a friendly minion. [Discover] a minion of the same minion type. """
	requirements = {
		PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	play = Discover(CONTROLLER, RandomMinion(race = RACE(TARGET)))
	pass

#class TSC_083e:# <12>[1658] -> <5>[1658]
#	""" Lamplight
#	Increased stats. """
#	#
#	pass

class TSC_632:# <12>[1658]
	""" Click-Clocker
	[Divine Shield]. [Battlecry:]Give a random Mech inyour hand +1/+1. """
	play = Buff(RANDOM(FRIENDLY_HAND + MECH), 'TSC_632e')
	pass

TSC_632e=buff(1,1)# <12>[1658]
""" Robo-claws
+1/+1. """

class TSC_638:# <12>[1658]
	""" Piranha Swarmer
	[Rush]After you summon a PiranhaSwarmer, gain +1 Attack. """
	events = Summon(CONTROLLER, FRIENDLY_MINIONS + ID('TSC_638')).after(Buff(SELF, 'TSC_638e'))
	pass

TSC_638e=buff(1,0)# <12>[1658]
""" Swarming
Increased Attack. """

class TSC_638t:# <12>[1658]
	""" Piranha Swarmer
	[Rush]After you summon a PiranhaSwarmer, gain +1 Attack. """
	events = Summon(CONTROLLER, FRIENDLY_MINIONS + ID('TSC_638')).after(Buff(SELF, 'TSC_638e'))
	pass

class TSC_638t2:# <12>[1658]
	""" Piranha Swarmer
	[Rush]After you summon a PiranhaSwarmer, gain +1 Attack. """
	events = Summon(CONTROLLER, FRIENDLY_MINIONS + ID('TSC_638')).after(Buff(SELF, 'TSC_638e'))
	pass

class TSC_638t3:# <12>[1658]
	""" Piranha Swarmer
	[Rush]After you summon a PiranhaSwarmer, gain +1 Attack. """
	events = Summon(CONTROLLER, FRIENDLY_MINIONS + ID('TSC_638')).after(Buff(SELF, 'TSC_638e'))
	pass

class TSC_638t4:# <12>[1658]
	""" Piranha Swarmer
	[Rush]After you summon a PiranhaSwarmer, gain +1 Attack. """
	events = Summon(CONTROLLER, FRIENDLY_MINIONS + ID('TSC_638')).after(Buff(SELF, 'TSC_638e'))
	pass

class TSC_640:# <12>[1658]
	""" Reefwalker
	[Battlecry and Deathrattle:] Summon a 1/1 Piranha Swarmer. """
	play = Summon(CONTROLLER, 'TSC_638')
	deathrattle = Summon(CONTROLLER, 'TSC_638')
	pass

class TSC_641:# <12>[1658]
	""" Queen Azshara
	[Battlecry:] If you've cast three spells while holding this, choose an Ancient Relic.@ <i>({0} left!)</i>@ <i>(Ready!)</i> """
	entourage = ['TSC_641ta','TSC_641tb','TSC_641tc','TSC_641td']
	class Hand:
		events = OWN_SPELL_PLAY.on(SidequestCounter(SELF, 3, Discover(CONTROLLER, RandomEntourage())))
	pass


class TSC_641ta_Action(TargetedAction):
	TARGET=ActionArg()
	CARD=ActionArg()
	def do(self, source, target, card):
		target.data.scripts.play = card.data.scripts.play
		target.requirements = card.data.requirements
		target.cost = 1
		pass

class TSC_641ta:# <12>[1658]
	""" Ring of Tides
	After you cast a spell, this becomes a copy of it that costs (1). """
	class Hand:
		events = OWN_SPELL_PLAY.after(TSC_641ta_Action(SELF, Play.CARD))
	pass

class TSC_641tae:# <12>[1658]
	""" Shifting
	Transforming into your spells. """
	#
	pass

class TSC_641tb:# <12>[1658]##
	""" Horn of Ancients
	Add a random [Colossal] minion to your hand.It costs (1). """
	play = Give(CONTROLLER, RandomMinion(colossal=True)).then(Buff(Give.CARD, 'TSC_641tde'))
	pass

class TSC_641tc:# <12>[1658]#############################
	""" Xal'atath
	After you cast a spell, deal 2 damage to the enemy hero and lose 1 Durability. """
	#
	pass

class TSC_641td:# <12>[1658]
	""" Tidestone of Golganneth
	Shuffle 5 randomspells into your deck.Set their Cost to (1).Draw two cards. """
	play = (Shuffle(CONTROLLER, RandomSpell()).then(Buff(Shuffle.CARD,'TSC_641tde'))) * 5, Draw(CONTROLLER) * 2
	pass

TSC_641tde=buff(cost=SET(1))# <12>[1658]
""" Reduced
Costs (1). """

class TSC_645:# <12>[1658]
	""" Mothership
	[Rush][Deathrattle:] Summon two random Mechs that cost (3) or less. """
	#
	pass

class TSC_646:# <12>[1658]
	""" Seascout Operator
	[Battlecry:] If you control a Mech, summon two 2/1 Mechafish. """
	#
	pass

class TSC_646t:# <12>[1658]
	""" Mechafish
	 """
	#
	pass

class TSC_647:# <12>[1658]
	""" Pelican Diver
	[Dormant] for 1 turn.[Rush] """
	#
	pass

class TSC_647e:# <12>[1658]
	""" Diving
	[Dormant]. Awaken in @ |4(turn, turns). """
	#
	pass

class TSC_649:# <12>[1658]
	""" Ini Stormcoil
	[Battlecry:] Choose a friendlyMech. Summon a copy of itwith [Rush], [Windfury], and[Divine Shield]. """
	#
	pass

class TSC_649e2:# <12>[1658]
	""" Enhanced!
	Granted [Rush], [Divine Shield] and [Windfury]. """
	#
	pass

class TSC_823:# <12>[1658]
	""" Murkwater Scribe
	[Battlecry:] The next spell you play costs (1) less. """
	play = Buff(FRIENDLY_HAND + SPELL, 'TSC_823e')
	pass

class TSC_823e:# <12>[1658]
	""" Murky
	Your next spell costs (1) less. """
	cost = lambda self, i : max(i-1,0)
	events = OWN_SPELL_PLAY.on(Destroy(SELF))
	pass

class TSC_826:# <12>[1658]
	""" Crushclaw Enforcer
	[Battlecry:] If you've cast a spell while holding this, draw a Naga. """
	class Hand:
		events = OWN_SPELL_PLAY.on(SidequestCounter(SELF, 1, [SetAttr(SELF, '_sidequest_counter_', 1)]))
	play = CheckAttribute(SELF, '_sidequest_counter_') & Give(CONTROLLER, RANDOM(FRIENDLY_DECK + NAGA))
	pass

class TSC_827:# <12>[1658]
	""" Vicious Slitherspear
	After you cast a spell,gain +1 Attack untilyour next turn. """
	events = OWN_SPELL_PLAY.on(Buff(SELF, 'TSC_827e'))
	pass

class TSC_827e:# <12>[1658]
	""" Vicious
	+1 Attack until your next turn. """
	atk = lambda self, i : i+1
	events = OWN_TURN_BEGIN.on(Destroy(SELF))
	pass



class TSC_829:# <12>[1658]
	""" Naga Giant
	Costs (1) less for each Mana you've spent on spells this game. """
	cost_mod = - Count(FRIENDLY + KILLED + SPELL)
	pass

class TSC_908:# <12>[1658]
	""" Sir Finley, Sea Guide
	[Battlecry:] Swap your hand with the bottom of your deck. """
	def play(self):
		num = len(self.controller.hand)
		for i in range(num):
			log.info("Swap %s and %s"%(self.controller.hand[i], self.controller.deck[i]))
			self.controller.hand[i], self.controller.deck[i] = self.controller.deck[i], self.controller.hand[i] 
	pass

class TSC_909:# <12>[1658]
	""" Tuskarrrr Trawler
	[Battlecry:] [Dredge]. """
	play = Dredge(CONTROLLER)
	pass

class TSC_911_Action(Dredge):
	def choose (self, card):
		super().choose(card)
		card.cost = max(0, card.cost-1)
		pass

class TSC_911:# <12>[1658]
	""" Excavation Specialist
	[Battlecry:] [Dredge].Reduce its Cost by (1). """
	play = TSC_911_Action(CONTROLLER)
	pass

class TSC_919:# <12>[1658]
	""" Azsharan Sentinel
	[Taunt]. [Deathrattle:] Put a'Sunken Sentinel' on the bottom of your deck. """
	deathrattle = PutOnBottom(CONTROLLER, 'TSC_919t')
	pass

class TSC_919t:# <12>[1658]
	""" Sunken Sentinel
	[[Divine Shield],] [[Taunt],][Lifesteal] """
	#
	pass

class TSC_926:# <12>[1658]
	""" Smothering Starfish
	[Battlecry:] [Silence] ALL other minions. """
	play = Silence(ALL_MINIONS - SELF)
	pass

class TSC_928:# <12>[1658]
	""" Security Automaton
	After you summon a Mech, gain +1/+1. """
	events = Summon(CONTROLLER, FRIENDLY_MINIONS + MECH).on(Buff(SELF, 'TSC_928e'))
	pass
TSC_928e=buff(1,1)

class TSC_935:# <12>[1658]
	""" Selfish Shellfish
	[Deathrattle:] Your opponent draws 2 cards. """
	deathrattle = Draw(OPPONENT) * 2
	pass

class TSC_938:# <12>[1658]
	""" Treasure Guard
	[Taunt][Deathrattle:] Draw a card. """
	deathrattle = Draw(CONTROLLER)
	pass

class TSC_960:# <12>[1658]
	""" Twin-fin Fin Twin
	[Rush]. [Battlecry:] Summon a copy of this. """
	play = Summon(CONTROLLER, ExactCopy(SELF))
	pass

