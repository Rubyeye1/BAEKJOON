class Node:                                                     # Node 클래스 정의.
    def __init__(node, data, left_node, right_node):            # 각 노드들은 데이터, 왼쪽 노드 노드, 오른쪽 자식 노드를 가진다.
        node.data = data
        node.left_node = left_node
        node.right_node = right_node

def pre_order(node):                                            # 전위 순회를 수행하는 pre_order 함수.
    print(node.data, end = '')                                  # 전위순회이므로 먼저 중간 데이터를 출력하고.
    if node.left_node != '.':                                   # 재귀적으로 함수를 호출한다.
        pre_order(tree[node.left_node])
    if node.right_node != '.':
        pre_order(tree[node.right_node])

def in_order(node):                                             # 중위 순회를 수행하는 in_order 함수.
    if node.left_node != '.':                                   # 중위 순회이므로 왼쪽을 먼저 호출하고 재귀적으로 수행한다.
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != '.':
        in_order(tree[node.right_node])

def post_order(node):                                           # 후위 순회를 수행하는 post_order 함수.
    if node.left_node != '.':                                   # 후위 순회이므로 맨 마지막에 중간 data를 출력한다.
        post_order(tree[node.left_node])
    if node.right_node != '.':
        post_order(tree[node.right_node])
    print(node.data, end='')

n = int(input())                                                # n을 입력받고.
tree = {}                                                       # tree 딕셔너리를 생성.

for _ in range(n):                                              # n개의 노드를 만든다.
    data, left_node, right_node = input().split(' ')
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])