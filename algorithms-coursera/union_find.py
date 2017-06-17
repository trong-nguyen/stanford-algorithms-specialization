import operator

class UnionFind(object):
	"""
	Datastructure for quick querying and merging of items in clusters
	Theoretical complexity: O(log*n)
	- Merge by rank
	- Path compression

	The current implementation has a complexity of O(logn) for union 
	due to forced updating leader of all merged vertices
	"""

	RANK_IDX = 1
	VERT_IDX = 0

	def __init__(self, vertices):
		super(UnionFind, self).__init__()
		self.my_leader = {v: [v, 0] for v in vertices}
		self.groups = len(vertices)

	def find(self, v):
		root = v
		leader = None #arbitrary
		while leader != root:
			leader = root
			root = self.my_leader[root][self.VERT_IDX]

		#updating
		self.my_leader[v][self.VERT_IDX] = root

		return root

	def union(self, u, v):
		u_cluster = self.find(u)
		v_cluster = self.find(v)

		if u_cluster == v_cluster:
			return False

		u_rank = self.my_leader[u_cluster][self.RANK_IDX]
		v_rank = self.my_leader[v_cluster][self.RANK_IDX]

		# Merge by rank
			# get the higher ranked cluster
		leader = u_cluster if u_rank >= v_rank else v_cluster
			# get the lower ranked cluster
		subtree_leader = v_cluster if leader == u_cluster else u_cluster

		self.my_leader[subtree_leader][self.VERT_IDX] = leader

		# delete subtree_leader
		self.groups -= 1

		# update leader's rank
		self.my_leader[leader][self.RANK_IDX] += 1		
		return True

	def __len__(self):
		return self.groups

	def get(self):
		'''
		Get the groups of clustered vertices
		'''

		clusters = {}
		for v, (leader, rank) in self.my_leader.iteritems():
			clusters[leader] = clusters.get(leader, [])
			clusters[leader].append(v)
		return clusters.values()

