class UnionFind(object):
	"""docstring for UnionFind"""
	VERTICE_NOT_FOUND = -1
	def __init__(self, vertices):
		super(UnionFind, self).__init__()
		self.my_leader = {v: [v, 0] for v in vertices}
		self.my_children = {v: (v,) for v in vertices}

	def find(self, v):
		vr = self.my_leader.get(v, (self.VERTICE_NOT_FOUND, 0))
		return vr[0]

	def union(self, u, v):
		u_cluster = self.find(u)
		v_cluster = self.find(v)

		if u_cluster == v_cluster:
			return False

		u_rank = self.my_leader[u_cluster][1]
		v_rank = self.my_leader[v_cluster][1]

		# Merge by rank
			# get the higher ranked cluster
		leader = u_cluster if u_rank >= v_rank else v_cluster
			# get the lower ranked cluster
		subtree_leader = v_cluster if leader == u_cluster else u_cluster

		# update children's leader
		subtree_underlings = self.my_children[subtree_leader]

		self.my_children[leader] += subtree_underlings
		for underling in subtree_underlings:
			# leader changed, not rank
			self.my_leader[underling][0] = leader

		# delete subtree_leader
		del self.my_children[subtree_leader]

		# update leader's rank
		self.my_leader[leader][1] += 1		
		return True

	def __len__(self):
		return len(self.my_children)

	def get(self):
		return self.my_children.values()