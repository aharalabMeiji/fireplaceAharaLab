
from ..utils import *

Sunken_Neutral=[]



Sunken_Snapdragon=True  ###
Sunken_Ozumat=True  ###
Sunken_Neptulon_the_Tidehunter=True  ###
Sunken_Bubbler=True  ###
Sunken_Coilfang_Constrictor=True  ###
Sunken_Naval_Mine=True  ###
Sunken_Pufferfist=True  ###
Sunken_Gangplank_Diver=True  ###
Sunken_Slimescale_Diver=True  ###
Sunken_Baba_Naga=True  ###
Sunken_Barbaric_Sorceress=True  ###
Sunken_Blademaster_Okani=True  ###
Sunken_Gorloc_Ravager=True  ###
Sunken_School_Teacher=True  ###
Sunken_Rainbow_Glowscale=True  ###
Sunken_Slithering_Deathscale=True  ###
Sunken_Helmet_Hermit=True  ###
Sunken_Ambassador_Faelin=True  ###
Sunken_Amalgam_of_the_Deep=True  ###
Sunken_Click_Clocker=True  ###
Sunken_Piranha_Swarmer=True  ###
Sunken_Reefwalker=True  ###
Sunken_Queen_Azshara=True  ###
Sunken_Mothership=True  ###
Sunken_Seascout_Operator=True  ###
Sunken_Pelican_Diver=True  ###
Sunken_Ini_Stormcoil=True  ###
Sunken_Murkwater_Scribe=True  ###
Sunken_Crushclaw_Enforcer=True  ###
Sunken_Vicious_Slitherspear=True  ###
Sunken_Naga_Giant=True  ###
Sunken_Sir_Finley_Sea_Guide=True  ###
Sunken_Tuskarrrr_Trawler=True  ###
Sunken_Excavation_Specialist=True  ###
Sunken_Azsharan_Sentinel=True  ###
Sunken_Smothering_Starfish=True  ###
Sunken_Security_Automaton=True  ###
Sunken_Selfish_Shellfish=True  ###
Sunken_Treasure_Guard=True  ###
Sunken_Twin_fin_Fin_Twin=True  ###


##############################################



if Sunken_Snapdragon:# 
	Sunken_Neutral+=['TID_710']
	Sunken_Neutral+=['TID_710e']
class TID_710:# <12>[1658]
	""" Snapdragon
	[Battlecry:] Give all[Battlecry] minions in your deck +1/+1. """
	def play(self):
		controller=self.controller
		for card in controller.deck:
			if card.has_battlecry:
				Buff(card, 'TID_710e').trigger(self)
		pass
	pass
TID_710e=buff(1,1)# <12>[1658]
""" Razor Sharp	+1/+1. """




if Sunken_Ozumat:# 
	Sunken_Neutral+=['TID_711']
	Sunken_Neutral+=['TID_711t','TID_711t2','TID_711t3','TID_711t4','TID_711t5','TID_711t6']
class TID_711_Deathrattle(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = target
		for card in controller.field:
			if card.id in ['TID_711t','TID_711t2','TID_711t3','TID_711t4','TID_711t5','TID_711t6']:
				alive_minions=[card for card in controller.opponent.field if card._to_be_destroyed==False]
				if len(alive_minions)>0:
					target = random.choice(alive_minions)
					Destroy(target).trigger(self)
class TID_711:# <12>[1658]
	""" Ozumat
	[Colossal +6] [Deathrattle:] For each of Ozumat's Tentacles, destroy a random enemy minion. """
	play = (
		Summon(CONTROLLER,'TID_711t'),
		Summon(CONTROLLER,'TID_711t2'),
		Summon(CONTROLLER,'TID_711t3'),
		Summon(CONTROLLER,'TID_711t4'),
		Summon(CONTROLLER,'TID_711t5'),
		Summon(CONTROLLER,'TID_711t6'))
	deathrattle = TID_711_Deathrattle(CONTROLLER)
	pass
class TID_711t:# <12>[1658]
	""" Ozumat's Tentacle
	 """
	pass
class TID_711t2:# <12>[1658]
	""" Ozumat's Tentacle
	 """
	pass
class TID_711t3:# <12>[1658]
	""" Ozumat's Tentacle
	 """
	pass
class TID_711t4:# <12>[1658]
	""" Ozumat's Tentacle
	 """
	pass
class TID_711t5:# <12>[1658]
	""" Ozumat's Tentacle
	 """
	pass
class TID_711t6:# <12>[1658]
	""" Ozumat's Tentacle
	 """
	pass




if Sunken_Neptulon_the_Tidehunter:# 
	Sunken_Neutral+=['TID_712']
	Sunken_Neutral+=['TID_712t','TID_712t2']
class TID_712_Attack(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=source.controller
		if isinstance(target,list):
			target = target[0]
		for card in controller.field:
			if card.id in ['TID_712t','TID_712t2']:
				RegularAttack(card, target)
				source.stop_attack=True
		pass
class TID_712:# <12>[1658]
	""" Neptulon the Tidehunter
	[Colossal +2], [Rush], [Windfury]Whenever Neptulon attacks,if you control any Hands,they attack instead. """
	play=Summon(CONTROLLER,'TID_712t'),Summon(CONTROLLER,'TID_712t2')
	events = Attack(SELF).on(TID_712_Attack(Attack.DEFENDER))
	pass
class TID_712t:# <12>[1658]
	""" Neptulon's Hand
	[Immune] while attacking. """
	pass
class TID_712t2:# <12>[1658]
	""" Neptulon's Hand
	[Immune] while attacking. """
	pass




if Sunken_Bubbler:# 
	Sunken_Neutral+=['TID_713']
class TID_713:# <12>[1658]
	""" Bubbler
	After this minion takes exactly one damage, destroy it. <i>(Pop!)</i> """
	events = Damage(SELF, 1).on(Destroy(SELF))
	pass




if Sunken_Coilfang_Constrictor:# 
	Sunken_Neutral+=['TID_744']
	Sunken_Neutral+=['TID_744e']
class TID_744_Choice(Choice):
	def choose(self, card):
		super().choose(card)
		Buff(card,'TID_744e').trigger(self.source)

class TID_744:# <12>[1658] ########## need check #############
	""" Coilfang Constrictor
	[Battlecry:] Look at 3 cards in your opponent's hand and choose one. It can't be played next turn. """
	play = TID_744_Choice(CONTROLLER, RANDOM(ENEMY_HAND)*3)
	pass
class TID_744e:# <12>[1658]
	""" Constricted
	Can't be played next turn. """
	tags={GameTag.CANT_PLAY:True}
	events=EndTurn(OPPONENT).on(Destroy(SELF))
	#
	pass




if Sunken_Naval_Mine:# 
	Sunken_Neutral+=['TSC_001']
class TSC_001:# <12>[1658]
	""" Naval Mine
	[Deathrattle:] Deal 4 damageto the enemy hero. """
	#
	pass




if Sunken_Pufferfist:# 
	Sunken_Neutral+=['TSC_002']
class TSC_002:# <12>[1658]
	""" Pufferfist
	After your hero attacks, deal 1 damage to all enemies. """
	#
	pass




if Sunken_Gangplank_Diver:# 
	Sunken_Neutral+=['TSC_007']
class TSC_007:# <12>[1658]
	""" Gangplank Diver
	[Dormant] for 1 turn.[Rush]. [Immune] while attacking. """
	#
	pass




if Sunken_Slimescale_Diver:# 
	Sunken_Neutral+=['TSC_013']
class TSC_013:# <12>[1658]
	""" Slimescale Diver
	[Dormant] for 1 turn.[Rush], [Poisonous] """
	#
	pass




if Sunken_Baba_Naga:# 
	Sunken_Neutral+=['TSC_017']
class TSC_017:# <12>[1658]
	""" Baba Naga
	[Battlecry:] If you've casta spell while holding this, deal 3 damage. """
	#
	pass




if Sunken_Barbaric_Sorceress:# 
	Sunken_Neutral+=['TSC_020']
	Sunken_Neutral+=['TSC_020e']
	Sunken_Neutral+=['TSC_020e2']
class TSC_020:# <12>[1658]
	""" Barbaric Sorceress
	[Taunt]. [Battlecry:] Swap the Cost of a random spell in each player's hand. """
	#
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




if Sunken_Blademaster_Okani:# 
	Sunken_Neutral+=['TSC_032']
	Sunken_Neutral+=['TSC_032t']
	Sunken_Neutral+=['TSC_032t2']
class TSC_032:# <12>[1658]
	""" Blademaster Okani
	[Battlecry:] [Secretly] choose to[Counter] the next minion orspell your opponent playswhile this is alive. """
	play = GenericChoicePlay(CONTROLLER, RandomID('TSC_032t','TSC_032t2'))
	events = Death(SELF).on(Destroy(FRIENDLY + SECRET + ID('TSC_032t')), Destroy(FRIENDLY + SECRET + ID('TSC_032t2')))
class TSC_032t:# <12>[1658]
	""" Minion Counter (spell)-> secret
	[Counter] the next minionyour opponent plays. """
	tags = { GameTag.SECRET: True}
	secret = Play(OPPONENT, MINION).on(Reveal(SELF), Counter(Play.CARD))
	pass
class TSC_032t2:# <12>[1658]
	""" Spell Counter (spell)-> secret
	[Counter] the next spell your opponent plays. """
	tags = { GameTag.SECRET: True}
	secret = Play(OPPONENT, SPELL).on(Reveal(SELF), Counter(Play.CARD))
	pass




if Sunken_Gorloc_Ravager:# 
	Sunken_Neutral+=['TSC_034']
class TSC_034:# <12>[1658]
	""" Gorloc Ravager
	[Battlecry:] Draw 3 Murlocs. """
	#
	pass




if Sunken_School_Teacher:# 
	Sunken_Neutral+=['TSC_052']
	Sunken_Neutral+=['TSC_052t']
class TSC_052:# <12>[1658]
	""" School Teacher
	[Battlecry:] Add a 1/1 Nagaling to your hand. [Discover] a spell that costs (3) or less to teach it. """
	#
	pass
class TSC_052t:# <12>[1658]
	""" Nagaling
	[Battlecry:] Cast {0}. """
	#
	pass




if Sunken_Rainbow_Glowscale:# 
	Sunken_Neutral+=['TSC_053']
class TSC_053:# <12>[1658]
	""" Rainbow Glowscale
	[Spell Damage +1] """
	#
	pass




if Sunken_Slithering_Deathscale:# 
	Sunken_Neutral+=['TSC_064']
class TSC_064:# <12>[1658]
	""" Slithering Deathscale
	[Battlecry:] If you've cast three spells while holding this, deal 3 damage to all enemies.@ <i>({0} left!)</i>@ <i>(Ready!)</i> """
	#
	pass




if Sunken_Helmet_Hermit:# 
	Sunken_Neutral+=['TSC_065']
class TSC_065:# <12>[1658]
	""" Helmet Hermit
	Can't attack. """
	#
	pass




if Sunken_Ambassador_Faelin:# 
	Sunken_Neutral+=['TSC_067']
class TSC_067:# <12>[1658]
	""" Ambassador Faelin
	[Battlecry:] Put 3 [Colossal] minions on the bottom of your deck. """
	#
	pass




if Sunken_Amalgam_of_the_Deep:# 
	Sunken_Neutral+=['TSC_069']
class TSC_069:# <12>[1658] ####### need check ##########
	""" Amalgam of the Deep
	[Battlecry:] Choose a friendly minion. [Discover] a minionof the same minion type. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0,}
	play = Discover(CONTROLLER, RandomMinion(race=RACE(TARGET)))
	pass




if Sunken_Click_Clocker:# 
	Sunken_Neutral+=['TSC_632']
	Sunken_Neutral+=['TSC_632e']
class TSC_632:# <12>[1658] ## visually OK
	""" Click-Clocker
	[Divine Shield]. [Battlecry:]Give a random Mech inyour hand +1/+1. """
	play = Buff(RANDOM(FRIENDLY_HAND + MECH), 'TSC_632e')
	pass
TSC_632e=buff(1,1)# <12>[1658]




if Sunken_Piranha_Swarmer:# 
	Sunken_Neutral+=['TSC_638']
	Sunken_Neutral+=['TSC_638e']
	Sunken_Neutral+=['TSC_638t']
	Sunken_Neutral+=['TSC_638t2']
	Sunken_Neutral+=['TSC_638t3']
	Sunken_Neutral+=['TSC_638t4']
class TSC_638:# <12>[1658]
	""" Piranha Swarmer
	[Rush]After you summon a PiranhaSwarmer, gain +1 Attack. """
	#
	pass
class TSC_638e:# <12>[1658]
	""" Swarming
	Increased Attack. """
	#
	pass
class TSC_638t:# <12>[1658]
	""" Piranha Swarmer
	[Rush]After you summon a PiranhaSwarmer, gain +1 Attack. """
	#
	pass
class TSC_638t2:# <12>[1658]
	""" Piranha Swarmer
	[Rush]After you summon a PiranhaSwarmer, gain +1 Attack. """
	#
	pass
class TSC_638t3:# <12>[1658]
	""" Piranha Swarmer
	[Rush]After you summon a PiranhaSwarmer, gain +1 Attack. """
	#
	pass
class TSC_638t4:# <12>[1658]
	""" Piranha Swarmer
	[Rush]After you summon a PiranhaSwarmer, gain +1 Attack. """
	#
	pass




if Sunken_Reefwalker:# 
	Sunken_Neutral+=['TSC_640']
class TSC_640:# <12>[1658] ## visually OK
	""" Reefwalker
	[Battlecry and Deathrattle:] Summon a 1/1 Piranha Swarmer. """
	play = Summon(CONTROLLER,'TSC_638')
	deathrattle = Summon(CONTROLLER,'TSC_638')
	pass




if Sunken_Queen_Azshara:# 
	Sunken_Neutral+=['TSC_641']
	Sunken_Neutral+=['TSC_641ta']
	Sunken_Neutral+=['TSC_641tae']
	Sunken_Neutral+=['TSC_641tb']
	Sunken_Neutral+=['TSC_641tc']
	Sunken_Neutral+=['TSC_641td']
	Sunken_Neutral+=['TSC_641tde']
class TSC_641:# <12>[1658]
	""" Queen Azshara
	[Battlecry:] If you've cast three spells while holding this, choose an Ancient Relic.@ <i>({0} left!)</i>@ <i>(Ready!)</i> """
	#
	pass
class TSC_641ta:# <12>[1658]
	""" Ring of Tides
	After you cast a spell, this becomes a copy of it that costs (1). """
	#
	pass
class TSC_641tae:# <12>[1658]
	""" Shifting
	Transforming into your spells. """
	#
	pass
class TSC_641tb:# <12>[1658]
	""" Horn of Ancients
	Add a random [Colossal] minion to your hand.It costs (1). """
	#
	pass
class TSC_641tc:# <12>[1658]
	""" Xal'atath
	After you cast a spell, deal 2 damage to the enemy hero and lose 1 Durability. """
	#
	pass
class TSC_641td:# <12>[1658]
	""" Tidestone of Golganneth
	Shuffle 5 randomspells into your deck.Set their Cost to (1).Draw two cards. """
	#
	pass
class TSC_641tde:# <12>[1658]
	""" Reduced
	Costs (1). """
	#
	pass




if Sunken_Mothership:# 
	Sunken_Neutral+=['TSC_645']
class TSC_645:# <12>[1658] ############## need check #####
	""" Mothership
	[Rush][Deathrattle:] Summon two random Mechs that cost (3) or less. """
	deathrattle=Summon(CONTROLLER, RandomMech(cost=RandomNumber(1, 2, 3)))
	pass




if Sunken_Seascout_Operator:# 
	Sunken_Neutral+=['TSC_646']
	Sunken_Neutral+=['TSC_646t']
class TSC_646:# <12>[1658]
	""" Seascout Operator
	[Battlecry:] If you control a Mech, summon two 2/1 Mechafish. """
	play = Find(FRIENDLY_MINIONS + MECH) & (Summon(CONTROLLER, 'TSC_646t')*2)
	pass
class TSC_646t:# <12>[1658]
	""" Mechafish """




if Sunken_Pelican_Diver:# 
	Sunken_Neutral+=['TSC_647']
	Sunken_Neutral+=['TSC_647e']
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




if Sunken_Ini_Stormcoil:# 
	Sunken_Neutral+=['TSC_649']
	Sunken_Neutral+=['TSC_649e2']
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




if Sunken_Murkwater_Scribe:# 
	Sunken_Neutral+=['TSC_823']
	Sunken_Neutral+=['TSC_823e']
class TSC_823:# <12>[1658]
	""" Murkwater Scribe
	[Battlecry:] The next spell you play costs (1) less. """
	#
	pass
class TSC_823e:# <12>[1658]
	""" Murky
	Your next spell costs (1) less. """
	#
	pass




if Sunken_Crushclaw_Enforcer:# 
	Sunken_Neutral+=['TSC_826']
class TSC_826:# <12>[1658]
	""" Crushclaw Enforcer
	[Battlecry:] If you've cast a spell while holding this, draw a Naga. """
	#
	pass




if Sunken_Vicious_Slitherspear:# 
	Sunken_Neutral+=['TSC_827']
	Sunken_Neutral+=['TSC_827e']
class TSC_827:# <12>[1658]
	""" Vicious Slitherspear
	After you cast a spell,gain +1 Attack untilyour next turn. """
	events = OWN_SPELL_PLAY.after(Buff(SELF, 'TSC_827e'))
	pass
class TSC_827e:# <12>[1658]
	""" Vicious
	+1 Attack until your next turn. """
	tags = {GameTag.TAG_ONE_TURN_EFFECT:True , GameTag.ATK:1, }
	pass




if Sunken_Naga_Giant:# 
	Sunken_Neutral+=['TSC_829']
class TSC_829:# <12>[1658]
	""" Naga Giant
	Costs (1) less for each Mana you've spent on spells this game. """
	#
	pass




if Sunken_Sir_Finley_Sea_Guide:# 
	Sunken_Neutral+=['TSC_908']
class TSC_908:# <12>[1658]
	""" Sir Finley, Sea Guide
	[Battlecry:] Swap yourhand with the bottom ofyour deck. """
	#
	pass




if Sunken_Tuskarrrr_Trawler:# 
	Sunken_Neutral+=['TSC_909']
class TSC_909:# <12>[1658]
	""" Tuskarrrr Trawler
	[Battlecry:] [Dredge]. """
	#
	pass




if Sunken_Excavation_Specialist:# 
	Sunken_Neutral+=['TSC_911']
class TSC_911:# <12>[1658]
	""" Excavation Specialist
	[Battlecry:] [Dredge].Reduce its Cost by (1). """
	#
	pass




if Sunken_Azsharan_Sentinel:# 
	Sunken_Neutral+=['TSC_919']
	Sunken_Neutral+=['TSC_919t']
class TSC_919:# <12>[1658]
	""" Azsharan Sentinel
	[Taunt]. [Deathrattle:] Put a'Sunken Sentinel' on thebottom of your deck. """
	#
	pass
class TSC_919t:# <12>[1658]
	""" Sunken Sentinel
	[[Divine Shield],] [[Taunt],][Lifesteal] """
	#
	pass




if Sunken_Smothering_Starfish:# 
	Sunken_Neutral+=['TSC_926']
class TSC_926:# <12>[1658]
	""" Smothering Starfish
	[Battlecry:] [Silence] ALL other minions. """
	#
	pass




if Sunken_Security_Automaton:# 
	Sunken_Neutral+=['TSC_928']
class TSC_928:# <12>[1658]
	""" Security Automaton
	After you summon a Mech, gain +1/+1. """
	#
	pass




if Sunken_Selfish_Shellfish:# 
	Sunken_Neutral+=['TSC_935']
class TSC_935:# <12>[1658]
	""" Selfish Shellfish
	[Deathrattle:] Your opponent draws 2 cards. """
	#
	pass




if Sunken_Treasure_Guard:# 
	Sunken_Neutral+=['TSC_938']
class TSC_938:# <12>[1658]

	""" Treasure Guard
	[Taunt][Deathrattle:] Draw a card. """
	#
	pass




if Sunken_Twin_fin_Fin_Twin:# 
	Sunken_Neutral+=['TSC_960']
class TSC_960:# <12>[1658]
	""" Twin-fin Fin Twin
	[Rush]. [Battlecry:] Summon a copy of this. """
	#
	pass



