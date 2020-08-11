class Genzo(object):
	"""
	Situation Vector with evolutionary calculation 
	"""
	def __init__(self, _weight,_name,_myClass,_hisClass,_rating):
		super(Genzo, self).__init__()
		self.weight=_weight
		self.name=_name
		self.myClass=_myClass
		self.hisClass=_hisClass
		self.rating=_rating

	def __str__(self):
		return "name:weight".format(name=self.name,weight=str(self.weight))

	def __eq__(self,obj):
		return str(self)==str(obj)

class GenzoWeight(object):
	"""
	Weight for Genzo agent
	"""
	def __init__(self, w):
		self.myHeroH = w[0]
		self.hisHeroH = -w[1]
		self.myCharN = w[2]
		self.myCharH = w[3]
		self.myTauntCharH = w[4]
		self.hisCharN = -w[5]
		self.hisCharH = -w[6]
		self.hisTauntCharH = -w[7]
		self.MinionCH = w[8]
		self.SpellCN = w[9]
		self.BattleCryCN = -w[10]#雄叫び
		self.ChargeCN = -w[11]#突撃
		self.WinduryCN = -w[12]#疾風
		self.TauntCN = -w[13]#挑発
		self.DamageCN = -w[14]#ダメージ
		self.GainCN = -w[15]#獲得#回復
		self.SummonCN = -w[16]#召喚
		self.LifeStealCN = -w[17]#生命奪取
		self.GiveCN = -w[18]#付与
		self.VanillaCN = -w[19]#バニラカード
#		#self. = -AddCopyCardN#追加
#		#self. = -DiscoverCardN#発見
#		#self. = -SilenceCardN#沈黙
#		#self. = -SpellBurstCardN#魔法活性
#		#self. = -OutCastCardN#異端

	def __str__(self):
		myText =  ''+str(self.myHeroH)+','
		myText += str(-self.hisHeroH)+','
		myText += str(self.myCharN)+','
		myText += str(self.myCharH)+','
		myText += str(self.myTauntCharH)+','
		myText += str(-self.hisCharN)+','
		myText += str(-self.hisCharH)+','
		myText += str(-self.hisTauntCharH)+','
		myText += str(self.MinionCH)+','
		myText += str(self.SpellCN)+','
		myText += str(-self.BattleCryCN)+','
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
		return self.mHH==obj.mHH and self.hHH==obj.hHH and self.mCN==obj.mCN and self.mCH==obj.mCH and self.mTCH==obj.mTCH and self.hCN==obj.hCN and self.hCH==obj.hCH and self.hTCH==obj.hTCH and self.mMCH==obj.mMCH and self.mSCN==obj.mSCN 


