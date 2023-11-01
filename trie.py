from typing import List


class Trie:

    def __init__(self):
        self.root_node = self.node_proto()

    @staticmethod
    def node_proto():
        return [None] * 27

    @staticmethod
    def char_token(c):
        return ord(c) - 97
    @staticmethod
    def tokenize_string(word) -> List[int]:
        return [ord(l) - 97 for l in word]

    def insert(self, word: str) -> None:

        root = self.root_node
        for c in word:
            t = self.char_token(c)
            if not root[t]:
                child = self.node_proto()
                root[t] = child
                root = child
            else:
                root = root[t]

        root[26] = self.node_proto()

    def search(self, word: str) -> bool:
        # tokens = self.tokenize_string(word) + [26]
        root = self.root_node
        for c in word:
            t = self.char_token(c)
            if not root[t]:
                return False
            else:
                root = root[t]

        return root[26] is not None


    def startsWith(self, prefix: str) -> bool:
        root = self.root_node
        for c in prefix:
            t = self.char_token(c)
            if not root[t]:
                return False
            else:
                root = root[t]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


def test_case1():
    val1 = Trie.tokenize_string("a")
    # val2 = Trie.tokenize_string("A")

    val3 = Trie.tokenize_string("z")
    # val4 = Trie.tokenize_string("Z")
    assert val1 == [0]
    assert val3 == [25]


def test_case2():
    t = Trie()
    t.insert("apple")

    assert t.startsWith("app")
    assert not t.startsWith("ban")
    assert not t.startsWith("ppl")


def test_case3():
    t = Trie()
    t.insert("apple")

    assert t.search("apple")
    assert not t.search("app")
    assert t.startsWith("appl")


def test_case4():
    cmd_log = ["Trie", "insert", "insert", "insert", "insert", "insert", "insert", "search", "search", "search", "search",
           "search", "search", "search", "search", "search", "startsWith", "startsWith", "startsWith", "startsWith",
           "startsWith", "startsWith", "startsWith", "startsWith", "startsWith"]

    arg_log = [[], ["app"], ["apple"], ["beer"], ["add"], ["jam"], ["rental"], ["apps"], ["app"], ["ad"], ["applepie"],
           ["rest"], ["jan"], ["rent"], ["beer"], ["jam"], ["apps"], ["app"], ["ad"], ["applepie"], ["rest"], ["jan"],
           ["rent"], ["beer"], ["jam"]]

    exp_log = [None, None, None, None, None, None, None, False, True, False, False, False, False, False, True, True,
               False, True, True, False, False, False, True, True, True]

    t = Trie()
    log = []
    for cmd, arg, exp in zip(cmd_log, arg_log, exp_log):
        if cmd == "insert":
            t.insert(arg[0])
            log.append(None)
        elif cmd == "search":
            log.append(t.search(arg[0]))
        elif cmd == "startsWith":
            log.append(t.startsWith(arg[0]))
        else:
            log.append(None)

    print()
    for res, exp, cmd, arg in zip(log, exp_log, cmd_log, arg_log):
        if res != exp:
            assert res == exp, f"failed on command {cmd} ({arg}). returned {res} but should return {exp}"

    assert log == exp_log
