from ..utils import *

BG_Alleycat=True
BG_Scavenging_Hyena=True
BG_Silverback_Patriarch=False#new 23.6 banned 24.2 
BG_Leapfrogger=True
BG_Rabid_Saurolisk=True
BG_Sewer_Rat=True
BG_Monstrous_Macaw=True
BG_Rat_Pack=True
BG_Cave_Hydra=True
BG_Reanimating_Rattler=True
BG_Savannah_Highmane=True
BG_Agamaggan_the_Great_Boar=True
BG_Baby_Krush=True#new 23.2
BG_Mama_Bear=True
BG_Palescale_Crocolisk=True
BG_Ghastcoiler=True
BG_Goldrinn_the_Great_Wolf=True
BG_Maexxna=False## banned 23.2


BG_Minion_Undead = []
BG_PoolSet_Undead=[ [],[],[],[],[],[],[]]
BG_Undead_Gold={}

##Rekka no skyfin <marloc+undead> (2/1/3) 
if BG_:
	BG_Minion_Undead += ['BG_CFM_315','BG_CFM_315t','TB_BaconUps_093','TB_BaconUps_093t',]#Alleycat
	BG_PoolSet_Undead[2].append('BG_CFM_315')
	BG_Undead_Gold['BG_CFM_315']='TB_BaconUps_093'
class BG_UND_213:#   
	""" Rekka no skyfin <undead> (1/1)
	."""
	events = BG_Play(CONTROLLER, MINION+BATTLECRY).on(Buff(SELF, 'BG_UND_213e'))
	pass
BG_UND_213e=buff(1,1)
class TB_BaconUps_UND_213:#
	""" Alleycat <beast> (2//2/6)
	"""
	events = BG_Play(CONTROLLER, MINION+BATTLECRY).on(Buff(SELF, 'TB_BaconUps_UND_213'))
	pass
TB_BaconUps_UND_213=buff(2,2)


class BG_UND_544:
	""" Sinrunner Branky (5/4/4)
	Reborn """
	##< when reborn, effects and max_health will be preserved.>
	pass

class BG_UND_534:
	""" KIGA-reshimono
	Avenge (1) Get 1/1 permanently"""
		events = Death(FRIENDLY).on(Avenge(SELF, 1,[BuffPermanently(SELF, 'BG_UND_534e')]))
BG_UND_534e=buff(1,1)

class BG_UND_666:
	"""
	divine shield, reborn"""
	pass
