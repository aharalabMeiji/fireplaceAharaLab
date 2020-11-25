from ..utils import *

class SCH_142:#done
	""" Voracious Reader (rare) """
	#At the end of your turn, draw until you have 3 cards.
	events = OWN_TURN_END.on(DrawUntil(CONTROLLER,3))#
	pass

class SCH_143:#done
	""" Divine Rager"""
	#Divine Shield
	pass

class SCH_145:#done
	""" Desk Imp"""
	#Vanilla
	pass

class SCH_146:#done
	""" Robes of Protection (Rare)"""
	#Your minions have &quot;Can't be targeted by spells or Hero Powers.&quot;
	play = Buff(CONTROLLER, "SCH_146e")
	pass
class SCH_146e:
	"""Protected"""
	#Can't be targeted by spells or Hero Powers.
	update = Refresh(FRIENDLY_MINIONS, {GameTag.CANT_BE_TARGETED_BY_HERO_POWERS: 1}), Refresh(FRIENDLY_MINIONS, {GameTag.CANT_BE_TARGETED_BY_SPELLS: 1}) 
	pass

class SCH_157:#done
	""" Enchanted Cauldron (Epic)"""
	#Spellburst: Cast a random spell of the same Cost.(3)
	play = Play(CONTROLLER, SPELL).on(CastSpell(RandomSpell(cost=Attr(Play.CARD, GameTag.COST))))
	pass

class SCH_160:#done
	""" Wandmaker"""
	#Battlecry: Add a 1-Cost spell from your class(HUNTER) to_your hand.
	play = Give(CONTROLLER, RandomSpell(cost=1, card_class=FRIENDLY_CLASS))
	pass

class SCH_162:#done
	""" Vectus"""
	#Battlecry: Summon two 1/1 Whelps. Each gains a Deathrattle from your minions that died this game.
	play = Summon(CONTROLLER, "SCH_162t").then( -Find(FRIENDLY + KILLED + DEATHRATTLE) |
		Buff(Summon.CARD, "SCH_162e").then( 
			CopyDeathrattles(Buff.BUFF, RANDOM(FRIENDLY + KILLED + DEATHRATTLE))
		)
	) *2
	pass
class SCH_162e:
	tags = {GameTag.DEATHRATTLE: True}
	# Experimental Plague
	# Copied Deathrattle from {0}
class SCH_162t:
	# Plagued Hatchling
	# Vanilla
	pass

class SCH_199:#????????????????????????????????????????????? havent
	""" Transfer Student (Epic)"""
	#This has different effects based on which game board you're on.
	pass
class SCH_199t:
	#ストームウィンド(時計台)　スタンダード
	#Divine Shield 
	pass
class SCH_199t2:
	# オーグリマー(煙突つき鍛冶場) スタンダード######################### no-checked
	#&lt;b&gt;Battlecry:&lt;/b&gt; Deal 2 damage.
	requirements = {PlayReq.REQ_ENEMY_TARGET: 0,
			PlayReq.REQ_TARGET_IF_AVAILABLE: 0,}
	play = Hit(TARGET,2)
	pass
class SCH_199t3:
	#パンダリア(銅鑼)スタンダード######################### no-checked
	#&lt;b&gt;Battlecry:&lt;/b&gt; Give a friendly minion +1/+2.
	play = Buff(FRIENDLY_MINIONS,"SCH_199t3e")
	pass
SCH_199t3e=buff(1,2)
#Mark of the Pandaren
class SCH_199t4:
	#ストラングルソーン(滝)スタンダード######################### no-checked
	#&lt;b&gt;Stealth&lt;/b&gt; &lt;b&gt;Poisonous&lt;/b&gt;
	pass
class SCH_199t5:
	pass
class SCH_199t6:
	pass
class SCH_199t7:
	pass
class SCH_199t8:
	pass
class SCH_199t9:
	pass
class SCH_199t10:
	#旧神のささやき(触手の生えた時計台) ワイルド
	pass
class SCH_199t11:
	pass
class SCH_199t12:
	pass
class SCH_199t13:
	pass
class SCH_199t14:
	pass
class SCH_199t15:
	pass
class SCH_199t16:
	pass
class SCH_199t17:
	pass
class SCH_199t18:
	pass
class SCH_199t19:
	#爆誕！悪党同盟(悪党同盟のワゴン) スタンダード######################### no-checked
	#&lt;b&gt;Battlecry:&lt;/b&gt; Add a &lt;b&gt;Lackey&lt;/b&gt; to_your hand.
	entourage = ["CFM_066", "DAL_613", "DAL_614", "DAL_615", "DAL_739",\
	   "DAL_741", "DRG_052" ,"LOOT_306","ULD_616"]
	play = Draw(CONTROLLER, RandomEntourage())
	pass
class SCH_199t20:
	#突撃！探検同盟(石像の折れた脚)　スタンダード
	#Reborn
	pass
class SCH_199t21:################################################### no checked
	# 激闘！ドラゴン大決戦(巨大な背骨) スタンダード
	#&lt;b&gt;Battlecry:&lt;/b&gt; &lt;b&gt;Discover&lt;/b&gt; a Dragon.
	play = DISCOVER(RandomDragon())
	pass
class SCH_199t22:################################################### no checked
	#灰に舞う降魔の狩人(壊れたロボット) スタンダード
	##&lt;b&gt;Dormant&lt;/b&gt; for 2 turns. When this awakens, deal 3 damage to two random enemy minions.
	dormant = 2
	awaken = Hit(RANDOM_ENEMY_MINION,3) * 2
	pass
class SCH_199t23:
	#魔法学院スクロマンス(地下への階段) スタンダード
	#&lt;b&gt;Battlecry:&lt;/b&gt; Add a Dual Class card to your hand.
	# dual class card <=> hasattr(self, "multi_class_group")==True
	#play = ForceDraw(RANDOM_MULTI_CLASS_GROUP) 
	pass
class SCH_199t24:
	pass
class SCH_199t25:
	#突撃！探検同盟(風車) スタンダード
	#&lt;b&gt;Battlecry:&lt;/b&gt; Add an &lt;b&gt;Uldum&lt;/b&gt; Plague spell to your hand.
	pass
class SCH_199t26:################################################### no checked
	#ダークムーン・フェアへの招待状 スタンダード
	#&lt;b&gt;Corrupt:&lt;/b&gt; Gain +2/+2.
	play = Buff(CONTROLLER, "SCH_199t26")
	pass
SCH_199t26t = buff(2,2)

class SCH_224:#OK
	# &lt;b&gt;Spellburst:&lt;/b&gt; If the spell destroys any minions, summon them.
	""" Headmaster Kel'Thuzad (Legendary)"""
	play = Buff(CONTROLLER,"SCH_224e3")
	pass
class SCH_224e3:#OK
	#Kel'thuzad's Call
	events = OWN_SPELL_PLAY.after(
		Dead(ALL_MINIONS + Play.CARD) & (# Dead -> return bool
			Summon(CONTROLLER, "SCH_224t"),
			Destroy(SELF)
		)
	)
	pass
class SCH_224t:
	#Mr. Bigglesworth
	#Vanilla
	pass

class SCH_230:#OK
	""" Onyx Magescribe"""
	# &lt;b&gt;Spellburst:&lt;/b&gt; Add 2 random spells from your class to_your hand.
	play = OWN_SPELL_PLAY.on(
		ForceDraw(RandomSpell(card_class=FRIENDLY_CLASS)) * 2
	)
	pass

class SCH_231:#OK
	"""Intrepid Initiate  &lt;b&gt;Spellburst:&lt;/b&gt; Gain +2_Attack."""
	play = OWN_SPELL_PLAY.on(Buff(SELF, "SCH_231e"))#
	pass
SCH_231e = buff(2,0)

class SCH_232:#OK
	""" Crimson Hothead"""
	#&lt;b&gt;Spellburst:&lt;/b&gt; Gain +1 Attack and &lt;b&gt;Taunt&lt;/b&gt;.
	play = OWN_SPELL_PLAY.on(Buff(SELF, "SCH_232e"))#
	pass
SCH_232e = buff(1, 0, taunt=True)

class SCH_245:#OK
	""" Steward of Scrolls"""
	#&lt;b&gt;Spell Damage +1&lt;/b&gt;&lt;b&gt;Battlecry:&lt;/b&gt; &lt;b&gt;Discover&lt;/b&gt; a spell.
	play = DISCOVER(RandomSpell())
	# 'spellpower=1' has already coded.
	pass

class SCH_248:################################################### no checked
	""" Pen Flinger"""
	# &lt;b&gt;Battlecry:&lt;/b&gt; Deal 1 damage. &lt;b&gt;Spellburst:&lt;/b&gt; Return this to_your hand.
	requirements = {PlayReq.REQ_ENEMY_TARGET: 0,
			PlayReq.REQ_TARGET_IF_AVAILABLE: 0,}
	play = Hit(TARGET, 1), OWN_SPELL_PLAY.on(Bounce(SELF))
	pass

class SCH_259:
	""" Sphere of Sapience (legendary)"""
	#At the start of your turn, look at your top card. You can put it on the bottom _and lose 1 Durability.
	#play = OWN_TURN_BEGIN.on(GenericChoice())
	#??????????????????????????????????????????????
	pass
class SCH_259t:
	"""	A New Fate """
	#Draw a different card.

class SCH_283:
	""" Manafeeder Panthara"""
	#&lt;b&gt;Battlecry:&lt;/b&gt; If you've used your Hero Power this turn, draw a card.
	#play = HERO_POWER_USED & ForceDraw(FRIENDLY) ???????????????????????????????
	pass

class SCH_311:
	""" Animated Broomstick"""
	pass

class SCH_312:#done
	""" Tour Guide"""
	#	&lt;b&gt;Battlecry:&lt;/b&gt; Your next Hero Power costs (0).
	play = Buff(CONTROLLER, "SCH_312e")
class SCH_312e:
	update = Refresh(FRIENDLY_HERO_POWER, {GameTag.COST: SET(0)})
	events = Activate(CONTROLLER, HERO_POWER).on(Destroy(SELF))

class SCH_313:##########################################
	""" Wretched Tutor"""
	#&lt;b&gt;Spellburst:&lt;/b&gt; Deal 2 damage to all other minions.
	play = OWN_SPELL_PLAY.on(Hit(ALL_MINIONS-SELF,2))
	pass

class SCH_428:#done
	""" Lorekeeper Polkelt (Legendary)"""
	#[x]&lt;b&gt;Battlecry:&lt;/b&gt; Reorder your deck from the highest Cost card to the lowest Cost card. 
	def play(self):
		self.controller.deck.sort(key=lambda x:x.cost)
		pass
	pass

class SCH_530:#??????????????????????
	""" Sorcerous Substitute"""
	#&lt;b&gt;Battlecry:&lt;/b&gt; If you have &lt;b&gt;Spell Damage&lt;/b&gt;, summon a copy of this.
	play = Find(FRIENDLY_HAND + SPELLPOWER) & Summon(CONTROLLER, ExactCopy(SELF))
	pass

class SCH_605:###########################################################
	""" Lake Thresher"""
	#Also damages the minions next to whomever this attacks.
	requirements = {PlayReq.REQ_ENEMY_TARGET: 0,
			PlayReq.REQ_TARGET_IF_AVAILABLE: 0,}
	play = Hit(TARGET | TARGET_ADJACENT,Attr(SELF, GameTag.ATK))
	pass

class SCH_707:
	""" Fishy Flyer"""
	#&lt;b&gt;Rush&lt;/b&gt;. &lt;b&gt;Deathrattle:&lt;/b&gt; Add a_4/3 Ghost with &lt;b&gt;Rush&lt;/b&gt; to_your hand.
	deathrattle = Draw(CONTROLLER,"SCH_707t")
	pass
class SCH_707t:
	"""Spectral Flyer"""
	# Rush
	pass

class SCH_708:
	""" Sneaky Delinquent"""
	#&lt;b&gt;Stealth&lt;/b&gt;. &lt;b&gt;Deathrattle:&lt;/b&gt; Add a 3/1 Ghost with &lt;b&gt;Stealth&lt;/b&gt; to your hand.
	deathrattle = Draw(CONTROLLER,"SCH_708t")
	pass
class SCH_708t:
	"""Spectral Delinquent"""
	#Stealth

class SCH_709:
	""" Smug Senior"""
	#&lt;b&gt;Taunt&lt;/b&gt;. &lt;b&gt;Deathrattle:&lt;/b&gt; Add a_5/7 Ghost with &lt;b&gt;Taunt&lt;/b&gt; to_your hand.
	deathrattle = Draw(CONTROLLER,"SCH_709t")
	pass
class SCH_709t:
	"""Spectral Senior"""
	#Taunt
	pass

class SCH_710:
	""" Ogremancer"""
	#[x]Whenever your opponent casts a spell, summon a 2/2 Skeleton with &lt;b&gt;Taunt&lt;/b&gt;.
	secret = Play(ENEMY,SPELL).after(Summon(CONTROLLER,"SCH_710t"))
	pass
class SCH_710t:
	"""Risen Skeleton"""
	#Taunt
	pass

class SCH_711:
	""" Plagued Protodrake"""
	#&lt;b&gt;Deathrattle:&lt;/b&gt; Summon a random 7-Cost minion.
	deathrattle = Summon(CONTROLLER, RandomMinion(cost=7))
	pass

class SCH_713:
	""" Cult Neophyte (Rare)"""
	#&lt;b&gt;Battlecry:&lt;/b&gt; Your opponent's spells cost (1) more next_turn.
	events = OWN_TURN_BEGIN.on( Buff(CONTROLLER, "SCH_713e"))
	pass
class SCH_713e:
	update = Refresh(ENEMY_HAND + SPELL, buff="SCH_713e2")
	#Spoiled!
SCH_713e2=buff(cost=1)
	#Spoiling
class SCH_714:
	""" Educated Elekk (epic)"""
	#[x]Whenever a spell is played, this minion remembers it.
	#&lt;b&gt;Deathrattle:&lt;/b&gt; Shuffle the spells into your deck.
	pass
class SCH_714e:
	pass

class SCH_717:
	""" Keymaster Alabaster"""
	#[x]Whenever your opponent _draws a card, add a copy to_ _your hand that costs (1).
	events = Draw(OPPONENT).on(Give(CONTROLLER, ExactCopy(Draw.CARD)))
	pass





