
class Genzo(object):
	"""
	Situation Vector with evolutionary calculation 
	"""
	def __init__(self, _weight, _name, _myClass, _hisClass, _rating):
		super(Genzo, self).__init__()
		self.weight=_weight
		self.name=_name
		self.myClass=_myClass
		self.hisClass=_hisClass
		self.rating=_rating

	def __str__(self):
		return "%s(%s)<%s>"%(self.name,self.myClass,str(self.weight))

	def __eq__(self,obj):
		return str(self)==str(obj)

class GenzoWeight(object):
	"""
	Weight for Genzo agent
	"""
	def __init__(self, w):
		self.myHeroH = w[0]#自ヒーローのHP
		self.hisHeroH = -w[1]#相手ヒーローのHP
		self.myCharA = w[2]#自分のフィールドにあるミニョンの攻撃力の総和
		self.myCharH = w[3]#自分のフィールドにあるミニョンのHPの総和
		self.myTauntCharH = w[4]#自分のフィールドにある挑発ミニョンのHPの総和
		self.hisCharA = -w[5]#相手のフィールドにあるミニョンの攻撃力の総和
		self.hisCharH = -w[6]#相手のフィールドにあるミニョンのHPの総和
		self.hisTauntCharH = -w[7]#相手のフィールドにある挑発ミニョンのHPの総和
		self.MinionCH = w[8]#手持ちのミニョンのカードのHPの総和
		self.SpellCN = w[9]#手持ちの呪文のカードの枚数
		self.BattleCryCN = -w[10]#雄叫びカードの枚数
		self.ChargeCN = -w[11]#突撃カードの枚数
		self.WinduryCN = -w[12]#疾風カードの枚数
		self.TauntCN = -w[13]#挑発カードの枚数
		self.DamageCN = -w[14]#ダメージカードの枚数
		self.GainCN = -w[15]#獲得#回復カードの枚数
		self.SummonCN = -w[16]#召喚カードの枚数
		self.LifeStealCN = -w[17]#生命奪取カードの枚数
		self.GiveCN = -w[18]#付与カードの枚数
		self.VanillaCN = -w[19]#バニラカードの枚数

	def __str__(self):
		myText =  ''+str(self.myHeroH)+','
		myText += str(-self.hisHeroH)+','
		myText += str(self.myCharA)+','
		myText += str(self.myCharH)+','
		myText += str(self.myTauntCharH)+','
		myText += str(-self.hisCharA)+','
		myText += str(-self.hisCharH)+','
		myText += str(-self.hisTauntCharH)+','
		myText += str(-self.MinionCH)+','
		myText += str(self.SpellCN)+','
		myText += str(self.BattleCryCN)+','
		myText += str(-self.ChargeCN)+','
		myText += str(-self.WinduryCN)+','
		myText += str(-self.TauntCN)+','
		myText += str(-self.DamageCN)+','
		myText += str(-self.GainCN)+','
		myText += str(-self.SummonCN)+','
		myText += str(-self.LifeStealCN)+','
		myText += str(-self.GiveCN)+','
		myText += str(-self.VanillaCN)
		return myText

	def __eq__(self,obj):
		return self.myHeroH==obj.myHeroH and self.hisHeroH==obj.hisHeroH and \
			self.myCharA==obj.myCharA and self.myCharH==obj.myCharH and self.myTauntCharH==obj.myTauntCharH and \
			self.hisCharA==obj.hisCharA and self.hisCharH==obj.hisCharH and self.hisTauntCharH==obj.hisTauntCharH and \
			self.MinionCH==obj.MinionCH and self.SpellCN==obj.SpellCN 

	def deepcopy(self):
		import random
		wgt = [self.myHeroH,-self.hisHeroH,self.myCharA,self.myCharH,\
		self.myTauntCharH,-self.hisCharA,-self.hisCharH,-self.hisTauntCharH,\
		self.MinionCH,self.SpellCN,\
		-self.BattleCryCN,-self.ChargeCN,-self.WinduryCN,-self.TauntCN,\
		-self.DamageCN,-self.GainCN,-self.SummonCN,-self.LifeStealCN,\
		-self.GiveCN,-self.VanillaCN]
		return GenzoWeight(wgt)

	def deepcopyAndPerturb(self):
		import random
		wgt = [self.myHeroH,-self.hisHeroH,self.myCharA,self.myCharH,\
		self.myTauntCharH,-self.hisCharA,-self.hisCharH,-self.hisTauntCharH,\
		self.MinionCH,self.SpellCN,\
		-self.BattleCryCN,-self.ChargeCN,-self.WinduryCN,-self.TauntCN,\
		-self.DamageCN,-self.GainCN,-self.SummonCN,-self.LifeStealCN,\
		-self.GiveCN,-self.VanillaCN]
		plus = random.randint(0,19)
		wgt[plus] += 3
		minus = random.randint(0,19)
		wgt[minus] -= 3
		if wgt[minus]<1 :
			wgt[minus]=1
		return GenzoWeight(wgt)

