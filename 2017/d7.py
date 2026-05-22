testing_input =  """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""


class Node:
    def __init__(self, name):
        self.name = name
        self.value = -1
        self.childs = []
        self.parent = None

    def set_value(self, value):
        self.value = value

    def add_childs(self, childs):
        for child in childs:
            child.parent = self.name
            self.childs.append(child)

    def total(self):
        ret = map(lambda child: child.total(), self.childs)
        return self.value + sum(list(ret))



class NodeTree:
    def __init__(self):
        self.tree = {}
        self.relationships = {} 

    def parser(self, payload):
        trees = []
        for line in payload.split("\n"):
            if not line:
                continue 

            if "->" not in line:
                raw_node = line.split(" ")
            else:
                raw_node = line.split("->")[0].split(" ")
                self.relationships[raw_node[0]] = line.split("->")[1].split(",")

            name = raw_node[0]
            value = int(raw_node[1][1:-1])

            self.tree[name] = Node(name)
            self.tree[name].set_value(value) 

            #print('name: ', name, ' value: ', value)

        return self
    
    def build_graph(self):
        for key in self.relationships:
            nodes = list(map(lambda name: self.tree[name.strip()], self.relationships[key]))
            self.tree[key].add_childs(nodes)

        return self

    def get_root(self):
        for key in self.tree:
            node = self.tree[key]
            if node.parent == None:
                print("root node: ", node.name)
                return node

    def _recursive_unbalance_finder(self, node):
        if node.childs:
            for child in node.childs:
                self._recursive_unbalance_finder(child)
        else:
            print('node name: ', node.name, ' ->', node.total())
        

        return False

    def _freq(self, nodes):
        freq = {}
        for node in nodes:
            t = node.total()
            freq[t] = [node] if t not in freq else freq[t] + [node]

        low_key = min(freq, key=lambda k: len(freq[k]))

        return freq[low_key] 
    

    def _find_unbalances_recursively(self, nodes):
        
        
        print('ntotal: ', self._freq(nodes)[0].name)

        

    def find_unbalances(self):
        root = self.get_root()
        
        self._find_unbalances_recursively(root.childs)
        


        


def solve_puzzle_one(payload):
    root = NodeTree().parser(payload).build_graph().get_root()

    print("Solution 1: ", root.name)
    
    return True

def solve_puzzle_2nd_part(payload):
    root = NodeTree().parser(payload).build_graph().find_unbalances()


    return True

payload = open("./d7.db").read()

solve_puzzle_one(payload)
solve_puzzle_2nd_part(testing_input)
