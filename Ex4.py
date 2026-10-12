class Node:
    def __init__(self, value = None, next_node=None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return f"Node({self.value!r})"

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        new_node = Node(value, self.top)

        self.top = new_node
        self.size += 1
        return self

    def pop(self):

        if self.top is None:
            raise IndexError("нельзя удалить из пустого стека")

        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return value

    def peek(self):
        if self.top is None:
            raise IndexError("peek из пустого списка")
        return self.top.value

    def is_empty(self):
        return self.top is None

    def stack_size(self):
        """Количество элементов в стеке."""
        return self.size

    def __len__(self):
        return self.size

    def __bool__(self):
        return self.top is not None

    def __repr__(self):
        values = []
        current = self.top
        while current is not None:
            values.append(repr(current.value))
            current = current.next
        return "Stack(" + " -> ".join(values) + ")"

if __name__ == "__main__":
    s = Stack()

    print("Пустой?", s.is_empty())  # True

    s.push(1)
    s.push(2)
    s.push(3)
    print(s)                              # Stack(3 -> 2 -> 1)
    print("Размер:", len(s))              # 3
    print("Вершина:", s.peek())           # 3

    print("pop ->", s.pop())              # 3
    print("pop ->", s.pop())              # 2
    print("вершина теперь:", s.peek())    # 1
    print("размер:", s.stack_size())            # 1
    print("пустой?", s.is_empty())
    print("pop ->", s.pop())              # 1
    print("пустой?", s.is_empty())

    for method_name in ("pop", "peek"):
        try:
            getattr(s, method_name)()
        except IndexError as e:
            print(f"{method_name}: IndexError — {e}")