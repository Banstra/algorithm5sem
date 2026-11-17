from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):

    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


# ============ РЕКУРСИВНЫЕ ОБХОДЫ (DFS) ============

def inorder_traversal(root, result=None):

    if result is None:
        result = []
    if root:
        inorder_traversal(root.left, result)   # 1. Левое поддерево
        result.append(root.value)              # 2. Корень
        inorder_traversal(root.right, result)  # 3. Правое поддерево
    return result


def preorder_traversal(root, result=None):
    """
    Preorder (прямой обход):
    Корень -> Левое поддерево -> Правое поддерево
    """
    if result is None:
        result = []
    if root:
        result.append(root.value)              # 1. Корень
        preorder_traversal(root.left, result)  # 2. Левое поддерево
        preorder_traversal(root.right, result) # 3. Правое поддерево
    return result


def postorder_traversal(root, result=None):
    """
    Postorder (обратный обход):
    Левое поддерево -> Правое поддерево -> Корень
    """
    if result is None:
        result = []
    if root:
        postorder_traversal(root.left, result)  # 1. Левое поддерево
        postorder_traversal(root.right, result) # 2. Правое поддерево
        result.append(root.value)               # 3. Корень
    return result


# ============ ИТЕРАТИВНЫЙ ОБХОД (BFS) ============

def level_order_traversal(root):
    """
    Level-order (поуровневый обход):
    Обход дерева по уровням слева направо.
    Используется очередь (queue) для хранения узлов.
    """
    if root is None:
        return []
    
    result = []
    queue = deque([root])  # Очередь для BFS
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        # Обрабатываем все узлы текущего уровня
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.value)
            
            # Добавляем детей в очередь для следующего уровня
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result


tree = None
values = [int(x) for x in input("Введите список чисел через пробел: ").split()]

for value in values:
    tree = insert(tree, value)

print("=" * 50)
print("Рекурсивные обходы (DFS):")
print("=" * 50)

print(f"\nInorder (симметричный):  {inorder_traversal(tree)}")
print(f"  -> Для BST возвращает отсортированный список")

print(f"\nPreorder (прямой):       {preorder_traversal(tree)}")
print(f"  -> Сначала корень, потом поддеревья")

print(f"\nPostorder (обратный):    {postorder_traversal(tree)}")
print(f"  -> Сначала поддеревья, потом корень")

print("\n" + "=" * 50)
print("Итеративный обход (BFS):")
print("=" * 50)

print(f"\nLevel-order (поуровневый):")
levels = level_order_traversal(tree)
for i, level in enumerate(levels):
    print(f"  Уровень {i}: {level}")