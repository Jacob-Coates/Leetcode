class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root,store):
            if root.left != None:
                dfs(root.left,store)
            if root.right != None:
                dfs(root.right,store) 
            if root.left == None and root.right == None:
                store.append(root.val)
        store1,store2 = [],[]
        dfs(root1,store1)
        dfs(root2,store2)
        if len(store1) != len(store2):
            return False
        else: 
            for i in range(len(store1)):
                if store1[i] != store2[i]:
                    return False
            return True
