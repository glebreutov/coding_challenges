from typing import List


class WordDictionary:

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

    def addWord(self, word: str) -> None:

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
        tails = [self.root_node]
        for c in word:
            if c == ".":
                new_tails = [subnode for node in tails for subnode in node if subnode]
                if not new_tails:
                    return False
                else:
                    tails = new_tails
            else:
                t = self.char_token(c)

                new_tails = [node[t] for node in tails if node[t]]
                if not any(new_tails):
                    return False
                else:
                    tails = new_tails

        # return root[26] is not None
        return any([node[26] for node in tails])



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


def test_case1():
    val1 = WordDictionary.tokenize_string("a")
    # val2 = Trie.tokenize_string("A")

    val3 = WordDictionary.tokenize_string("z")
    # val4 = Trie.tokenize_string("Z")
    assert val1 == [0]
    assert val3 == [25]


def test_case2():
    t = WordDictionary()
    t.addWord("apple")

    assert t.startsWith("app")
    assert not t.startsWith("ban")
    assert not t.startsWith("ppl")


def test_case3():
    t = WordDictionary()
    t.addWord("apple")

    assert t.search("apple")
    assert not t.search("app")
    assert t.startsWith("appl")


def test_case4():
    cmd_log = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]

    arg_log = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

    exp_log = [None,None,None,None,False,True,True,True]

    t = WordDictionary()
    log = []
    for cmd, arg, exp in zip(cmd_log, arg_log, exp_log):
        if cmd == "addWord":
            t.addWord(arg[0])
            log.append(None)
        elif cmd == "search":
            log.append(t.search(arg[0]))
        else:
            log.append(None)

    print()
    for res, exp, cmd, arg in zip(log, exp_log, cmd_log, arg_log):
        if res != exp:
            assert res == exp, f"failed on command {cmd} ({arg}). returned {res} but should return {exp}"

    assert log == exp_log
