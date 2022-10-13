from ..utils import *

Rev_Shaman=[]

Rev_Totemic_Evidence=True
Rev_Framester=True
Rev_Torghast_Custodian=True
Rev_Criminal_Lineup=True
Rev_Baroness_Vashj=True
Rev_Muck_Pools=True
Rev_Gigantotem=True
Rev_Carving_Chisel=True
Rev_Convincing_Disguise=True
Rev_The_Stonewright=True
Rev_Muck_Pools=True
Rev_Primordial_Wave=True
Rev_Baroness_Vashj=True
Rev_Party_Favor_Totem=True
Rev_Crud_Caretaker=True
Rev_Relics_of_Old=True


class MorphCostup(TargetedAction):
	"""
	Morph minion target into a cost-up minion
	TARGET = ActionArg()
	AMOUNT = IntArg()
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		amount = max(target.cost+amount, 0)
		card = RandomMinion(cost=amount).execute(self)
		if target.id!='REV_925':
			Morph(target, card).trigger(source)
		else:
			Summon(source.controller, card).trigger(self)
	pass


if Rev_Totemic_Evidence:# 
	Rev_Shaman+=['MAW_003']
	#["CS2_050", "CS2_051", "CS2_052", "NEW1_009",] Hero.py
class MAW_003:# <8>[1691]
	""" Totemic Evidence
	Choose a basic Totem and summon it. <b>Infuse (@ Totems):</b> Summon all 4 instead. """
	#
	pass

	Rev_Shaman+=['MAW_003t']
class MAW_003t:# <8>[1691]
	""" Totemic Evidence
	<b>Infused</b> Summon all 4 basic Totems. """
	#
	pass

if Rev_Framester:# 
	Rev_Shaman+=['MAW_005']
class MAW_005:# <8>[1691]
	""" Framester
	<b>Battlecry:</b> Shuffle 3 'Framed' cards into the opponent's deck. When drawn, they <b>Overload</b> for (2). """
	#
	pass

	Rev_Shaman+=['MAW_005t']
class MAW_005t:# <8>[1691]
	""" Framed
	<b>Casts When Drawn</b> <b>Overload:</b> (2) """
	#
	pass

if Rev_Torghast_Custodian:# 
	Rev_Shaman+=['MAW_030']
class MAW_030:# <8>[1691]
	""" Torghast Custodian
	<b>Battlecry:</b> For each enemy minion, randomly gain <b>Rush</b>, <b>Divine Shield</b>, or <b>Windfury</b>. """
	#
	pass

	Rev_Shaman+=['MAW_030e2']
class MAW_030e2:# <8>[1691]
	""" Crawling
	<b>Rush</b>. """
	#
	pass

	Rev_Shaman+=['MAW_030e3']
class MAW_030e3:# <8>[1691]
	""" Sweeping
	<b>Divine Shield</b>. """
	#
	pass

	Rev_Shaman+=['MAW_030e4']
class MAW_030e4:# <8>[1691]
	""" Formidable
	<b>Windfury</b>. """
	#
	pass

if Rev_Criminal_Lineup:# 
	Rev_Shaman+=['REV_517']
class REV_517:# <8>[1691]
	""" Criminal Lineup
	Choose a friendly minion. Summon 3 copies of it. <b>Overload:</b> (2) """
	#
	pass

if Rev_Baroness_Vashj:# 
	Rev_Shaman+=['REV_788']
class REV_788:# <8>[1691]
	""" Baroness Vashj
	{0} {1} {2} {3} """
	#
	pass

if Rev_Muck_Pools:# 
	Rev_Shaman+=['REV_798']
class REV_798:# <8>[1691]
	""" Muck Pools
	{0} {1} """
	#
	pass

if Rev_Gigantotem:# 
	Rev_Shaman+=['REV_838']
class REV_838:# <8>[1691]
	""" Gigantotem
	Costs (1) less for each Totem you've summoned this game. """
	#
	pass

if Rev_Carving_Chisel:# 
	Rev_Shaman+=['REV_917']
class REV_917:# <8>[1691]
	""" Carving Chisel
	After your hero attacks, summon a random basic Totem. """
	#
	pass

if Rev_Convincing_Disguise:# 
	Rev_Shaman+=['REV_920']
class REV_920:# <8>[1691]
	""" Convincing Disguise
	Transform a friendly minion into one that costs (2) more. <b>Infuse (@):</b> Transform all friendly minions instead. """
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_920t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_920t', 1))
	#
	pass

	Rev_Shaman+=['REV_920t']
class REV_920t:# <8>[1691]
	""" Convincing Disguise
	<b>Infused</b> Transform all friendly minions into random ones that cost (2) more. """
	#
	pass

if Rev_The_Stonewright:# 
	Rev_Shaman+=['REV_921']
class REV_921:# <8>[1691]
	""" The Stonewright
	<b>Battlecry:</b> For the rest of the game, your Totems have +2 Attack. """
	#
	pass

	Rev_Shaman+=['REV_921e']
class REV_921e:# <8>[1691]
	""" Living Stone
	Your Totems have +2 Attack. """
	#
	pass

if Rev_Muck_Pools:# 
	Rev_Shaman+=['REV_923']
class REV_923:# <8>[1691]
	""" Muck Pools
	Transform a friendly minion into one that costs (1) more. """
	#
	pass

if Rev_Primordial_Wave:# 
	Rev_Shaman+=['REV_924']
class REV_924:# <8>[1691]
	""" Primordial Wave
	Transform enemy minions  into ones that cost (1) less  and friendly minions into  ones that cost (1) more. """
	#
	pass

if Rev_Baroness_Vashj:# 
	Rev_Shaman+=['REV_925']
class REV_925:# <8>[1691]
	""" Baroness Vashj
	If this would transform into a minion, summon that minion instead. """
	#
	pass

if Rev_Party_Favor_Totem:# 
	Rev_Shaman+=['REV_935']
class REV_935:# <8>[1691]
	""" Party Favor Totem
	At the end of your turn,  summon a random basic  Totem. <b>Infuse (@):</b>  Summon two instead. """
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_935t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_935t', 1))
	#
	pass

	Rev_Shaman+=['REV_935t']
class REV_935t:# <8>[1691]
	""" Party Favor Totem
	<b>Infused </b>At the end of your turn,  summon two random  basic Totems. """
	#
	pass

if Rev_Crud_Caretaker:# 
	Rev_Shaman+=['REV_936']
class REV_936:# <8>[1691]
	""" Crud Caretaker
	<b>Battlecry</b>: Summon a 3/5 Elemental with <b>Taunt</b>. """
	#
	pass

	Rev_Shaman+=['REV_936t']
class REV_936t:# <8>[1691]
	""" Untreated Filth
	<b>Taunt</b> """
	#
	pass

if Rev_Relics_of_Old:# 
	Rev_Shaman+=['REV_942e2']
class REV_942e2:# <8>[1691]
	""" Relics of Old
	Your next spell this turn casts twice. """
	#
	pass

