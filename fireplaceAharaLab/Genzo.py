
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
		self.myHeroH = w[0]#自ヒーローのHPを増やす
		self.hisHeroH = w[1]#相手ヒーローのHPを減らす
		self.myCharA = w[2]#自分のフィールドにあるミニョンの攻撃力の総和を増やす
		self.myCharH = w[3]#自分のフィールドにあるミニョンのHPの総和を増やす
		self.myTauntCharH = w[4]#自分のフィールドにある挑発ミニョンのHPの総和を増やす
		self.hisCharA = w[5]#相手のフィールドにあるミニョンの攻撃力の総和を減らす
		self.hisCharH = w[6]#相手のフィールドにあるミニョンのHPの総和を減らす
		self.hisTauntCharH = w[7]#相手のフィールドにある挑発ミニョンのHPの総和を減らす
		self.MinionCH = w[8]#手持ちのミニョンのカードを使う
		self.SpellCN = w[9]#手持ちの呪文のカードを使う
		self.BattleCryCN = w[10]#雄叫びカードを使う
		self.ChargeCN = w[11]#突撃カードを使う
		self.WinduryCN = w[12]#疾風カードを使う
		self.TauntCN = w[13]#挑発カードを使う
		self.DamageCN = w[14]#ダメージカードを使う
		self.GainCN = w[15]#獲得#回復カードを使う
		self.SummonCN = w[16]#召喚カードを使う
		self.LifeStealCN = w[17]#生命奪取カードを使う
		self.GiveCN = w[18]#付与カードを使う
		self.VanillaCN = w[19]#バニラカードを使う

	def __str__(self):
		myText = str(self.myHeroH)+','
		myText += str(self.hisHeroH)+','
		myText += str(self.myCharA)+','
		myText += str(self.myCharH)+','
		myText += str(self.myTauntCharH)+','
		myText += str(self.hisCharA)+','
		myText += str(self.hisCharH)+','
		myText += str(self.hisTauntCharH)+','
		myText += str(self.MinionCH)+','
		myText += str(self.SpellCN)+','
		myText += str(self.BattleCryCN)+','
		myText += str(self.ChargeCN)+','
		myText += str(self.WinduryCN)+','
		myText += str(self.TauntCN)+','
		myText += str(self.DamageCN)+','
		myText += str(self.GainCN)+','
		myText += str(self.SummonCN)+','
		myText += str(self.LifeStealCN)+','
		myText += str(self.GiveCN)+','
		myText += str(self.VanillaCN)
		return myText

	def __eq__(self,obj):
		return self.name==obj.name 

	def deepcopy(self):
		import random
		wgt = [self.myHeroH,self.hisHeroH,self.myCharA,self.myCharH,\
		self.myTauntCharH,self.hisCharA,self.hisCharH,self.hisTauntCharH,\
		self.MinionCH,self.SpellCN,\
		self.BattleCryCN,self.ChargeCN,self.WinduryCN,self.TauntCN,\
		self.DamageCN,self.GainCN,self.SummonCN,self.LifeStealCN,\
		self.GiveCN,self.VanillaCN]
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

