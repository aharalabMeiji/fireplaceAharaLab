class Genzo(object):
	"""
	Situation Vector with evolutionary calculation 
	"""
	def __init__(self, _weight,_name,_myClass,_hisClass):
		super(Genzo, self).__init__()
		self.weight=_weight
		self.name=_name
		self.myClass=_myClass
		self.hisClass=_hisClass

	def __str__(self):
		return "name:weight".format(name=self.name,weight=str(self.weight))

	def __eq__(self,obj):
		return str(self)==str(obj)

class GenzoWeight(object):
	"""
	Weight for Genzo agent
	"""
	def __init__(self,myHeroH=1, hisHeroH=1, myCharN=1, myCharH=1, myTauntCharH=1, hisCharN=1, hisCharH=1, hisTauntCharH=1, myMinionCardH=1, mySpellCardN=1):
		self.mHH = myHeroH
		self.hHH = -hisHeroH
		self.mCN = myCharN
		self.mCH = myCharH
		self.mTCH = myTauntCharH
		self.hCN = -hisCharN
		self.hCH = -hisCharH
		self.hTCH = -hisTauntCharH
		self.mMCH = myMinionCardH
		self.mSCN = mySpellCardN

	def __str__(self):
		return "something"

	def __eq__(self,obj):
		return self.mHH==obj.mHH and self.hHH==obj.hHH and self.mCN==obj.mCN and self.mCH==obj.mCH and self.mTCH==obj.mTCH and self.hCN==obj.hCN and self.hCH==obj.hCH and self.hTCH==obj.hTCH and self.mMCH==obj.mMCH and self.mSCN==obj.mSCN 


