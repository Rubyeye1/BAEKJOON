import sys
sys.setrecursionlimit(10 ** 6)                      # 런타임 에러를 해결하기 위한 setrecursionlimit 함수.(재귀의 최대 깊이를 늘리기)


class Node:                                         # 노드 클래스를 정의.
    def __init__(self, data):                       # 데이터와 왼쪽 오른쪽 자식노드를 가지고 있다.
        self.data = data
        self.left = None
        self.right = None

class Tree:                                         # 트리 클래스를 정의.
    def __init__(self):                             # 루트 노드를 가지고 있다.
        self.root = None
    def add(self, data):                            # 트리 클래스의 add 메소드.
        if self.root == None:                       # 전위 순회한 값이 주어지므로 루트 노드가 없으면 처음 들어오는 값을 root로 정할 수 있다.
            self.root = Node(data)
        else:
            cur = self.root                         # 만약 루트 노드가 존재하면 일단 현재(cur)을 루트노드로 설정해두고.
            while(True):
                if cur.data > data:                 # 루트노드의 데이터보다 현재 들어온 데이터가 작으면 (이진 검색트리)
                    if(cur.left == None):           # 거기에다가 노드의 왼쪽 자식이 없으면
                        cur.left = Node(data)       # 왼쪽 자식을 들어온 데이터의 노드로 만들고
                        break                       # break를 한다
                    cur = cur.left                  # 루트노드의 데이터보다 현재 들어온 데이터가 적은데 노드의 왼쪽 자식이 존재하면 cur(현재 노드)를 왼쪽 자식의 노드로 바꾼다
                                                    # 이렇게 하는 이유는 맨 위 루트 노드부터 검사하기 위해서.
                else:
                    if(cur.right == None):          # 왼쪽과 같은 방식으로 루트노드의 데이터보다 현재 들어온 데이터가 클 경우
                        cur.right = Node(data)      # 거기에다가 노드의 오른쪽 자식이 없으면 만들고
                        break
                    cur = cur.right                 # 루트노드의 데이터보다 현재 들어온 데이터가 큰데 노드의 오른쪽 자식이 존재하면 cur(현재 노드)를 오른쪽 자식의 노드로 바꾼다
    def postOrder(self, node=None):                 # 후위 순회 메소드
        global answer                               # global 변수로 answer 리스트를 만들어 넣고 거기에 후위순회 순서로 데이터를 append로 넣는다.
        if node == None:
            node = self.root
        if node.left != None:
            self.postOrder(node.left)
        if node.right != None:
            self.postOrder(node.right)
        answer.append(node.data)


answer = []
tree = Tree()
while True:
    try:
        tree.add(int(input()))
    except:                                         # 더이상 들어올 입력값이 없을때 while문을 끝내기 위한 try except문.
        break
tree.postOrder()
Numtree = len(answer)                               # answer의 개수를 세고
for i in range(Numtree):                            # answer(후위순회)을 출력한다.
    print(answer[i])