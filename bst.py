# Binary search tree
class binarySearchTree:
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None

    def insert(self,val):
        # check jika tidak ada root
        if (self.val == None):
            self.val = val
        # periksa dimana harus memasukkan
        else:
            # periksa duplikat, lalu hentikan dan kembalikan
            if val == self.val: return 'tidak ada duplikat yang diizinkan di binary search tree'
            # periksa apakah nilai yang akan disisipkan < nilai currentNode
            if (val < self.val):
                # periksa apakah ada node kiri ke currentNode jika true maka recurse(rekursif)
                if(self.left):
                    self.left.insert(val)
                # sisipkan di mana kiri currentNode ketika currentNode.left=None
                else: self.left = binarySearchTree(val)

            # langkah-langkah yang sama seperti di atas di sini kondisi yang kita periksa adalah nilai yang harus dimasukkan > nilai currentNode
            else:
                if(self.right):
                    self.right.insert(val)
                else: self.right = binarySearchTree(val)




    def breadthFirstSearch(self):
        currentNode = self
        bfs_list = []
        queue = []
        queue.insert(0,currentNode)
        while(len(queue) > 0):
            currentNode = queue.pop()
            bfs_list.append(currentNode.val)
            if(currentNode.left):
                queue.insert(0,currentNode.left)
            if(currentNode.right):
                queue.insert(0,currentNode.right)

        return bfs_list

    # In order berarti child sebelah kiri pertama, kemudian parent, pada child terakhir sebelah kanan
    def Search_INorder(self):
        return self.InOrder([])

    # Pre order berarti parent pertama, kemudian child sebelah kiri, pada child terakhir sebelah kanan
    def Search_PREorder(self):
        return self.PreOrder([])

    # Post order means first left child, then right child , at last parent
    def Search_POSTorder(self):
        return self.PostOrder([])

    def InOrder(self, lst):
        if (self.left):
            self.left.InOrder(lst)
        lst.append(self.val)
        if (self.right):
            self.right.InOrder(lst)
        return lst

    def PreOrder(self, lst):
        lst.append(self.val)
        if (self.left):
            self.left.PreOrder(lst)
        if (self.right):
            self.right.PreOrder(lst)
        return lst

    def PostOrder(self, lst):
        if (self.left):
            self.left.PostOrder(lst)
        if (self.right):
            self.right.PostOrder(lst)
        lst.append(self.val)
        return lst

    def findNodeAndItsParent(self,val, parent = None):
        # mengembalikan node dan induknya sehingga kita dapat menghapus node dan merekonstruksi pohon dari induknya
        if val == self.val: return self, parent
        if (val < self.val):
            if (self.left):
                return self.left.findNodeAndItsParent(val, self)
            else: return 'Not found'
        else:
            if (self.right):
                return  self.right.findNodeAndItsParent(val, self)
            else: return 'Not found'

    # menghapus node berarti kita harus mengatur ulang beberapa bagian dari tree
    def delete(self,val):
        # periksa apakah nilai yang ingin kita hapus ada di tree
        if(self.findNodeAndItsParent(val)=='Tidak ditemukan'): return 'Node tidak ada di tree'
        # kita mendapatkan node yang ingin kita hapus dan parent-node-nya dari metode findNodeAndItsParent
        deleteing_node, parent_node = self.findNodeAndItsParent(val)
        # periksa berapa banyak node child yang akan kita hapus dengan traversePreOrder dari deleteing_node
        nodes_effected = deleteing_node.PreOrder([])
        # jika len(nodes_effected)==1 berarti, node yang akan dihapus tidak memiliki anak
        # jadi kita bisa memeriksa dari node induknya posisi (kiri atau kanan) dari node yang ingin kita hapus
        # dan arahkan posisi ke 'None' yaitu node dihapus
        if (len(nodes_effected)==1):
            if (parent_node.left.val == deleteing_node.val) : parent_node.left = None
            else: parent_node.right = None
            return 'Succesfully deleted'
        # jika len(nodes_effected) > 1 yang berarti node yang akan kita hapus memiliki 'anak',
        # jadi treenya harus diatur ulang dari deleteing_node
        else:
            # jika node yang ingin kita hapus tidak memiliki induk berarti node yang akan dihapus adalah node 'root'
            if (parent_node == None):
                nodes_effected.remove(deleteing_node.val)
                # membuat node 'root' yaitu self value, left, right ke None,
                # ini berarti kita perlu menerapkan pohon baru lagi tanpa node yang dihapus
                self.left = None
                self.right = None
                self.val = None
                # pembangunan pohon baru
                for node in nodes_effected:
                    self.insert(node)
                return 'berhasil dihapus'

            # jika node yang ingin kita hapus memiliki induk
            # traverse dari parent_node
            nodes_effected = parent_node.PreOrder([])
            # penghapusan node
            if (parent_node.left == deleteing_node) : parent_node.left = None
            else: parent_node.right = None
            # menghapus parent_node, deleteing_node dan memasukkan nodes_effected di pohon
            nodes_effected.remove(deleteing_node.val)
            nodes_effected.remove(parent_node.val)
            for node in nodes_effected:
                self.insert(node)

        return 'Berhasil Dihapus'



bst = binarySearchTree(20)
lists = {2, 52, 12, 14, 34, 45}
for i in lists:
    bst.insert(i)


print('IN order: ',bst.Search_INorder()) # berguna dalam menyortir pohon dalam urutan asceding
print('PRE order:' ,bst.Search_PREorder()) # pre order berguna dalam merekonstruksi pohon
print('POST order:', bst.Search_POSTorder()) # berguna dalam menemukan simpul daun

print(bst.delete(20))
