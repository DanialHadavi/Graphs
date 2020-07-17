
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    # add first node to the path
    path = [starting_node]

    q.enqueue(path)

    while q.size() > 0:
        current_path = q.dequeue()
        # list of next nodes
        new_path = []
        changed = False

        for node in current_path:
            # loop through ancestors for parents
            for ancestor in ancestors:
                # look into ancestor parents with start_node as child
                if ancestor[1] == node:
                    new_path.append(ancestor[0])
                    changed = True
                    q.enqueue(new_path)

        if changed is False:
            if current_path[0] == starting_node:
                return -1
            else:
                return current_path[0]
