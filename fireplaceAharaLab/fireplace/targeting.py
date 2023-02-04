"""
Targeting logic
"""
from hearthstone.enums import CardType, PlayReq, Rarity, Zone
from hearthstone.utils import CARDRACE_TAG_MAP
from enum import IntEnum

TARGETING_PREREQUISITES = (
	PlayReq.REQ_TARGET_TO_PLAY,
	PlayReq.REQ_TARGET_FOR_COMBO,
	PlayReq.REQ_TARGET_IF_AVAILABLE,
	#PlayReq.REQ_TARGET_IF_AVAILABLE_AND_DRAGON_IN_HAND,
	PlayReq.REQ_TARGET_IF_AVAILABLE_AND_MINIMUM_FRIENDLY_MINIONS,
	PlayReq.REQ_TARGET_IF_AVAILABLE_AND_MINIMUM_FRIENDLY_SECRETS,
	PlayReq.REQ_TARGET_IF_AVAILABLE_AND_HERO_ATTACKED_THIS_TURN,
)


def race_identity(target, param):
	""" def race_identity(target, param): """
	if target.type==CardType.MINION:
		if target.race==param:
			return True
		if target.data.tags.get(CARDRACE_TAG_MAP[param]):
			return True
	return False

# Requirements-based targeting
def is_valid_target(self, target, requirements=None):
	if target is self:
		# Battlecries can never target themselves
		return False

	if target.type == CardType.MINION:
		if target.dormant:
			return False
		if target.dead:
			return False
		if target.stealthed and self.controller != target.controller:
			return False
		if target.immune and self.controller != target.controller:
			return False
		if self.type == CardType.SPELL and target.cant_be_targeted_by_abilities:
			return False
		if self.type == CardType.SPELL and target.cant_be_targeted_by_spells:
			return False
		if self.type == CardType.HERO_POWER and target.cant_be_targeted_by_hero_powers:
			return False

	if target.cant_be_targeted_by_opponents and self.controller != target.controller:
		return False

	if requirements is None:
		requirements = self.requirements

	# Check if the entity can ever target other entities
	for req in TARGETING_PREREQUISITES:
		if req in requirements:
			break
	else:
		return False

	for req, param in requirements.items():
		if req == PlayReq.REQ_MINION_TARGET:
			if target.type == CardType.HERO or target.type != CardType.MINION or target.zone!=Zone.PLAY:
				return False
		elif req == PlayReq.REQ_FRIENDLY_TARGET:
			if target.controller != self.controller:
				return False
		elif req == PlayReq.REQ_ENEMY_TARGET:
			if target.controller == self.controller:
				return False
		elif req == PlayReq.REQ_DAMAGED_TARGET:
			if not target.damage:
				return False
		elif req == PlayReq.REQ_FROZEN_TARGET:
			if not target.frozen:
				return False
		elif req == PlayReq.REQ_TARGET_MAX_ATTACK:
			if target.atk > param or 0:
				return False
		elif req == PlayReq.REQ_TARGET_WITH_RACE:
			if param<=100:
				if target.type == CardType.MINION:
					if  race_identity(target, param)==False :
						return False
				else:
					return False
			else:
				race1=int(param/100)
				race2=param%100
				if target.type != CardType.MINION or (race_identity(target, race1)==False and race_identity(target, race2)==False):
					return False
		elif req == PlayReq.REQ_HERO_TARGET:
			if target.type != CardType.HERO:
				return False
		elif req == PlayReq.REQ_TARGET_MIN_ATTACK:
			if target.atk < param:
				return False
		elif req == PlayReq.REQ_MUST_TARGET_TAUNTER:
			if not target.taunt:
				return False
		elif req == PlayReq.REQ_UNDAMAGED_TARGET:
			if hasattr(target, 'damage')==False:
				return False
			elif hasattr(target, 'damage') and target.damage:
				return False
		elif req == PlayReq.REQ_LEGENDARY_TARGET:
			if target.rarity != Rarity.LEGENDARY:
				return False
		elif req == PlayReq.REQ_TARGET_WITH_BATTLECRY:
			if not target.has_battlecry:
				return False
		elif req == PlayReq.REQ_TARGET_WITH_DEATHRATTLE:
			if not target.has_deathrattle:
				return False
		elif req == PlayReq.REQ_HERO_OR_MINION_TARGET:# 
			if target.type != CardType.MINION and target.type != CardType.HERO:
				return False
		elif req == PlayReq.REQ_TARGET_IF_AVAILABLE_AND_MINIMUM_FRIENDLY_MINIONS:# 
			if len(target.controller.field)<param:
				return False
		elif req == 1002:## REQ_TARGET_WITHOUT_RACE
			if target.type != CardType.MINION or target.race == param:
				return False
		elif req == 1003:# REQ_NONGOLDEN_TARGET# 
			if hasattr(target.controller.game, 'parent'):
				if target.id in target.controller.game.parent.BG_Gold.values():
					return False
		elif req == 1004:## REQ_TARGET_ID
			if target.type != CardType.MINION or target.id != param:
				return False
		elif req == 1005:## PlayReq.REQ_TARGET_IMP:
			if target.type != CardType.MINION or getattr(target,'race', False) != True:
				return False
		

	return True
