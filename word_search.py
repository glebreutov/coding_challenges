from collections import defaultdict, deque
from dataclasses import dataclass
from typing import List, Set, Tuple, Dict, Optional, Deque
from pytest_unordered import unordered


@dataclass
class Node:
    val: str
    row: int
    cell: int
    neighbours: Set

    def __hash__(self):
        return self.row * 1000 + self.cell


class Solution:

    @staticmethod
    def adj_cell_ids(idx_curr, cell_num):
        n_map = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row_idx = int(idx_curr / cell_num)
        cell_idx = idx_curr % cell_num
        for a, b in n_map:
            yield cell_num * (row_idx + a) + cell_idx + b

    def graph2(self, board):
        row_num = len(board)
        col_num = len(board[0])

        alphabet = defaultdict(list)
        nodes_by_num = []
        nodes_by_addr = dict()

        for i in range(row_num):
            for j in range(col_num):
                c = board[i][j]
                n = Node(c, i, j, set())
                alphabet[c].append(n)
                nodes_by_num.append(n)
                nodes_by_addr[(i, j)] = n

        n_map = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for node in nodes_by_num:
            for a, b in n_map:
                addr = (node.row + a, node.cell + b)
                if addr in nodes_by_addr:
                    node.neighbours.add(nodes_by_addr[addr])

        return alphabet

    @staticmethod
    def stat_split(alphabet: Dict[str, Deque[Node]], word: str):
        letter_stat = [len(alphabet[l]) for l in word]

        sp = min([(i, s) for i, s in enumerate(letter_stat)], key=lambda x: x[1])[0]

        if sp == 0:
            return word, ""
        elif sp == len(word) - 1:
            return word[:sp], ""
        else:

            fw = word[:(sp+1)][::-1]
            sw = word[(sp-1):]
            assert fw[0] + sw[0] == word
            return fw, sw

    @staticmethod
    def stat_reverse(alphabet: Dict[str, List[Node]], word: str):
        letter_stat = [len(alphabet[l]) for l in word]

        if len(letter_stat) < 2:
            return word

        if letter_stat[0] > letter_stat[-1]:
            return word[::-1]
        else:
            return word

    def search_head(self, alphabet: Dict[str, List[Node]], word: str):

        t1 = Solution.stat_reverse(alphabet, word)
        # t1, t2 = Solution.stat_split(alphabet, word)
        # print(word, t1)
        first_letter = t1[0]
        start_points = alphabet[first_letter]
        for st_point in start_points:
            fw = self.search_tail(st_point, t1, set())
            # fw = self.search_tail_stack(st_point, t1)
            if fw:
                return True
        return False

    def search_tail_stack(self, node: Node, word):
        stack = [[] for _ in range(len(word))]
        stack[0].append(node)
        i = 0
        while i >= 0:
            # stack[i] = [n for n in stack[i] if n.val == word[i]]
            stack_level = stack[i]
            letter = word[i]
            if stack_level:
                cv = stack_level.pop()
                is_matched_node = cv.val == letter

                if is_matched_node and i == len(stack) - 1:
                    return True
                elif is_matched_node:
                    i += 1
                    stack[i].extend(cv.neighbours)
            else:
                i -= 1
        return False

    def search_tail(self, node: Node, word: str, visited: Set):
        if node in visited:
            return False

        if not word:
            return True
        # print(node.val, node.row, node.cell)

        head = word[0]
        tail = word[1:]

        if node.val != head:
            return False
        elif not tail:
            return True
        else:
            # nv = visited.copy()
            # nv.add(node)
            visited.add(node)
            for n in node.neighbours:
                found = self.search_tail(n, tail, visited)
                if found:
                    return True
            visited.discard(node)
            return False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        al = self.graph2(board)

        return [word for word in words if self.search_head(al, word)]


def test_case1():
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ]
    words = ["oath", "pea", "eat", "rain"]
    exp = ["oath", "eat", ]

    assert Solution().findWords(board, words) == exp


def test_adj_idx():
    res = list(Solution.adj_cell_ids(0, 3))

    assert res


def test_case2():
    board = [["a", "a"]]
    words = ["aa"]
    exp = ["aa"]

    assert Solution().findWords(board, words) == exp


def test_case3():
    board = [["a"]]
    words = ["a"]
    assert Solution().findWords(board, words) == ["a"]


def test_case4():
    board = [["a", "b", "c"],
             ["a", "e", "d"],
             ["a", "f", "g"]]
    words = ["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ade"]

    exp = ["abcdefg", "befa", "eaabcdgfa", "gfedcbaaa"]

    assert Solution().findWords(board, words) == unordered(exp)


def test_case6():
    board = [["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]]
    words = ["oa", "oaa"]
    exp = ["oa", "oaa"]

    assert Solution().findWords(board, words) == unordered(exp)


def test_case_huge():
    board = [["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"], ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
             ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"], ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
             ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"], ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
             ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"], ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
             ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"], ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"]]

    words = ["ababababaa", "ababababab", "ababababac", "ababababad", "ababababae", "ababababaf", "ababababag",
             "ababababah", "ababababai", "ababababaj", "ababababak", "ababababal", "ababababam", "ababababan",
             "ababababao", "ababababap", "ababababaq", "ababababar", "ababababas", "ababababat", "ababababau",
             "ababababav", "ababababaw", "ababababax", "ababababay", "ababababaz", "ababababba", "ababababbb",
             "ababababbc", "ababababbd", "ababababbe", "ababababbf", "ababababbg", "ababababbh", "ababababbi",
             "ababababbj", "ababababbk", "ababababbl", "ababababbm", "ababababbn", "ababababbo", "ababababbp",
             "ababababbq", "ababababbr", "ababababbs", "ababababbt", "ababababbu", "ababababbv", "ababababbw",
             "ababababbx", "ababababby", "ababababbz", "ababababca", "ababababcb", "ababababcc", "ababababcd",
             "ababababce", "ababababcf", "ababababcg", "ababababch", "ababababci", "ababababcj", "ababababck",
             "ababababcl", "ababababcm", "ababababcn", "ababababco", "ababababcp", "ababababcq", "ababababcr",
             "ababababcs", "ababababct", "ababababcu", "ababababcv", "ababababcw", "ababababcx", "ababababcy",
             "ababababcz", "ababababda", "ababababdb", "ababababdc", "ababababdd", "ababababde", "ababababdf",
             "ababababdg", "ababababdh", "ababababdi", "ababababdj", "ababababdk", "ababababdl", "ababababdm",
             "ababababdn", "ababababdo", "ababababdp", "ababababdq", "ababababdr", "ababababds", "ababababdt",
             "ababababdu", "ababababdv", "ababababdw", "ababababdx", "ababababdy", "ababababdz", "ababababea",
             "ababababeb", "ababababec", "ababababed", "ababababee", "ababababef", "ababababeg", "ababababeh",
             "ababababei", "ababababej", "ababababek", "ababababel", "ababababem", "ababababen", "ababababeo",
             "ababababep", "ababababeq", "ababababer", "ababababes", "ababababet", "ababababeu", "ababababev",
             "ababababew", "ababababex", "ababababey", "ababababez", "ababababfa", "ababababfb", "ababababfc",
             "ababababfd", "ababababfe", "ababababff", "ababababfg", "ababababfh", "ababababfi", "ababababfj",
             "ababababfk", "ababababfl", "ababababfm", "ababababfn", "ababababfo", "ababababfp", "ababababfq",
             "ababababfr", "ababababfs", "ababababft", "ababababfu", "ababababfv", "ababababfw", "ababababfx",
             "ababababfy", "ababababfz", "ababababga", "ababababgb", "ababababgc", "ababababgd", "ababababge",
             "ababababgf", "ababababgg", "ababababgh", "ababababgi", "ababababgj", "ababababgk", "ababababgl",
             "ababababgm", "ababababgn", "ababababgo", "ababababgp", "ababababgq", "ababababgr", "ababababgs",
             "ababababgt", "ababababgu", "ababababgv", "ababababgw", "ababababgx", "ababababgy", "ababababgz",
             "ababababha", "ababababhb", "ababababhc", "ababababhd", "ababababhe", "ababababhf", "ababababhg",
             "ababababhh", "ababababhi", "ababababhj", "ababababhk", "ababababhl", "ababababhm", "ababababhn",
             "ababababho", "ababababhp", "ababababhq", "ababababhr", "ababababhs", "ababababht", "ababababhu",
             "ababababhv", "ababababhw", "ababababhx", "ababababhy", "ababababhz", "ababababia", "ababababib",
             "ababababic", "ababababid", "ababababie", "ababababif", "ababababig", "ababababih", "ababababii",
             "ababababij", "ababababik", "ababababil", "ababababim", "ababababin", "ababababio", "ababababip",
             "ababababiq", "ababababir", "ababababis", "ababababit", "ababababiu", "ababababiv", "ababababiw",
             "ababababix", "ababababiy", "ababababiz", "ababababja", "ababababjb", "ababababjc", "ababababjd",
             "ababababje", "ababababjf", "ababababjg", "ababababjh", "ababababji", "ababababjj", "ababababjk",
             "ababababjl", "ababababjm", "ababababjn", "ababababjo", "ababababjp", "ababababjq", "ababababjr",
             "ababababjs", "ababababjt", "ababababju", "ababababjv", "ababababjw", "ababababjx", "ababababjy",
             "ababababjz", "ababababka", "ababababkb", "ababababkc", "ababababkd", "ababababke", "ababababkf",
             "ababababkg", "ababababkh", "ababababki", "ababababkj", "ababababkk", "ababababkl", "ababababkm",
             "ababababkn", "ababababko", "ababababkp", "ababababkq", "ababababkr", "ababababks", "ababababkt",
             "ababababku", "ababababkv", "ababababkw", "ababababkx", "ababababky", "ababababkz", "ababababla",
             "abababablb", "abababablc", "ababababld", "abababable", "abababablf", "abababablg", "abababablh",
             "ababababli", "abababablj", "abababablk", "ababababll", "abababablm", "ababababln", "abababablo",
             "abababablp", "abababablq", "abababablr", "ababababls", "abababablt", "abababablu", "abababablv",
             "abababablw", "abababablx", "abababably", "abababablz", "ababababma", "ababababmb", "ababababmc",
             "ababababmd", "ababababme", "ababababmf", "ababababmg", "ababababmh", "ababababmi", "ababababmj",
             "ababababmk", "ababababml", "ababababmm", "ababababmn", "ababababmo", "ababababmp", "ababababmq",
             "ababababmr", "ababababms", "ababababmt", "ababababmu", "ababababmv", "ababababmw", "ababababmx",
             "ababababmy", "ababababmz", "ababababna", "ababababnb", "ababababnc", "ababababnd", "ababababne",
             "ababababnf", "ababababng", "ababababnh", "ababababni", "ababababnj", "ababababnk", "ababababnl",
             "ababababnm", "ababababnn", "ababababno", "ababababnp", "ababababnq", "ababababnr", "ababababns",
             "ababababnt", "ababababnu", "ababababnv", "ababababnw", "ababababnx", "ababababny", "ababababnz",
             "ababababoa", "ababababob", "ababababoc", "ababababod", "ababababoe", "ababababof", "ababababog",
             "ababababoh", "ababababoi", "ababababoj", "ababababok", "ababababol", "ababababom", "ababababon",
             "ababababoo", "ababababop", "ababababoq", "ababababor", "ababababos", "ababababot", "ababababou",
             "ababababov", "ababababow", "ababababox", "ababababoy", "ababababoz", "ababababpa", "ababababpb",
             "ababababpc", "ababababpd", "ababababpe", "ababababpf", "ababababpg", "ababababph", "ababababpi",
             "ababababpj", "ababababpk", "ababababpl", "ababababpm", "ababababpn", "ababababpo", "ababababpp",
             "ababababpq", "ababababpr", "ababababps", "ababababpt", "ababababpu", "ababababpv", "ababababpw",
             "ababababpx", "ababababpy", "ababababpz", "ababababqa", "ababababqb", "ababababqc", "ababababqd",
             "ababababqe", "ababababqf", "ababababqg", "ababababqh", "ababababqi", "ababababqj", "ababababqk",
             "ababababql", "ababababqm", "ababababqn", "ababababqo", "ababababqp", "ababababqq", "ababababqr",
             "ababababqs", "ababababqt", "ababababqu", "ababababqv", "ababababqw", "ababababqx", "ababababqy",
             "ababababqz", "ababababra", "ababababrb", "ababababrc", "ababababrd", "ababababre", "ababababrf",
             "ababababrg", "ababababrh", "ababababri", "ababababrj", "ababababrk", "ababababrl", "ababababrm",
             "ababababrn", "ababababro", "ababababrp", "ababababrq", "ababababrr", "ababababrs", "ababababrt",
             "ababababru", "ababababrv", "ababababrw", "ababababrx", "ababababry", "ababababrz", "ababababsa",
             "ababababsb", "ababababsc", "ababababsd", "ababababse", "ababababsf", "ababababsg", "ababababsh",
             "ababababsi", "ababababsj", "ababababsk", "ababababsl", "ababababsm", "ababababsn", "ababababso",
             "ababababsp", "ababababsq", "ababababsr", "ababababss", "ababababst", "ababababsu", "ababababsv",
             "ababababsw", "ababababsx", "ababababsy", "ababababsz", "ababababta", "ababababtb", "ababababtc",
             "ababababtd", "ababababte", "ababababtf", "ababababtg", "ababababth", "ababababti", "ababababtj",
             "ababababtk", "ababababtl", "ababababtm", "ababababtn", "ababababto", "ababababtp", "ababababtq",
             "ababababtr", "ababababts", "ababababtt", "ababababtu", "ababababtv", "ababababtw", "ababababtx",
             "ababababty", "ababababtz", "ababababua", "ababababub", "ababababuc", "ababababud", "ababababue",
             "ababababuf", "ababababug", "ababababuh", "ababababui", "ababababuj", "ababababuk", "ababababul",
             "ababababum", "ababababun", "ababababuo", "ababababup", "ababababuq", "ababababur", "ababababus",
             "ababababut", "ababababuu", "ababababuv", "ababababuw", "ababababux", "ababababuy", "ababababuz",
             "ababababva", "ababababvb", "ababababvc", "ababababvd", "ababababve", "ababababvf", "ababababvg",
             "ababababvh", "ababababvi", "ababababvj", "ababababvk", "ababababvl", "ababababvm", "ababababvn",
             "ababababvo", "ababababvp", "ababababvq", "ababababvr", "ababababvs", "ababababvt", "ababababvu",
             "ababababvv", "ababababvw", "ababababvx", "ababababvy", "ababababvz", "ababababwa", "ababababwb",
             "ababababwc", "ababababwd", "ababababwe", "ababababwf", "ababababwg", "ababababwh", "ababababwi",
             "ababababwj", "ababababwk", "ababababwl", "ababababwm", "ababababwn", "ababababwo", "ababababwp",
             "ababababwq", "ababababwr", "ababababws", "ababababwt", "ababababwu", "ababababwv", "ababababww",
             "ababababwx", "ababababwy", "ababababwz", "ababababxa", "ababababxb", "ababababxc", "ababababxd",
             "ababababxe", "ababababxf", "ababababxg", "ababababxh", "ababababxi", "ababababxj", "ababababxk",
             "ababababxl", "ababababxm", "ababababxn", "ababababxo", "ababababxp", "ababababxq", "ababababxr",
             "ababababxs", "ababababxt", "ababababxu", "ababababxv", "ababababxw", "ababababxx", "ababababxy",
             "ababababxz", "ababababya", "ababababyb", "ababababyc", "ababababyd", "ababababye", "ababababyf",
             "ababababyg", "ababababyh", "ababababyi", "ababababyj", "ababababyk", "ababababyl", "ababababym",
             "ababababyn", "ababababyo", "ababababyp", "ababababyq", "ababababyr", "ababababys", "ababababyt",
             "ababababyu", "ababababyv", "ababababyw", "ababababyx", "ababababyy", "ababababyz", "ababababza",
             "ababababzb", "ababababzc", "ababababzd", "ababababze", "ababababzf", "ababababzg", "ababababzh",
             "ababababzi", "ababababzj", "ababababzk", "ababababzl", "ababababzm", "ababababzn", "ababababzo",
             "ababababzp", "ababababzq", "ababababzr", "ababababzs", "ababababzt", "ababababzu", "ababababzv",
             "ababababzw", "ababababzx", "ababababzy", "ababababzz"]
    res = Solution().findWords(board, words)
    assert res


def test_huge2():
    board = [["m", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"],
             ["n", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
             ["o", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
             ["p", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
             ["q", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
             ["r", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
             ["s", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
             ["t", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
             ["u", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
             ["v", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
             ["w", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
             ["x", "y", "z", "a", "a", "a", "a", "a", "a", "a", "a", "a"]]

    words = ["aaaaaaaaaa", "aaaaaaaaab", "aaaaaaaaac", "aaaaaaaaad", "aaaaaaaaae", "aaaaaaaaaf", "aaaaaaaaag",
             "aaaaaaaaah", "aaaaaaaaai", "aaaaaaaaaj", "aaaaaaaaak", "aaaaaaaaal", "aaaaaaaaam", "aaaaaaaaan",
             "aaaaaaaaao", "aaaaaaaaap", "aaaaaaaaaq", "aaaaaaaaar", "aaaaaaaaas", "aaaaaaaaat", "aaaaaaaaau",
             "aaaaaaaaav", "aaaaaaaaaw", "aaaaaaaaax", "aaaaaaaaay", "aaaaaaaaaz", "aaaaaaaaba", "aaaaaaaabb",
             "aaaaaaaabc", "aaaaaaaabd", "aaaaaaaabe", "aaaaaaaabf", "aaaaaaaabg", "aaaaaaaabh", "aaaaaaaabi",
             "aaaaaaaabj", "aaaaaaaabk", "aaaaaaaabl", "aaaaaaaabm", "aaaaaaaabn", "aaaaaaaabo", "aaaaaaaabp",
             "aaaaaaaabq", "aaaaaaaabr", "aaaaaaaabs", "aaaaaaaabt", "aaaaaaaabu", "aaaaaaaabv", "aaaaaaaabw",
             "aaaaaaaabx", "aaaaaaaaby", "aaaaaaaabz", "aaaaaaaaca", "aaaaaaaacb", "aaaaaaaacc", "aaaaaaaacd",
             "aaaaaaaace", "aaaaaaaacf", "aaaaaaaacg", "aaaaaaaach", "aaaaaaaaci", "aaaaaaaacj", "aaaaaaaack",
             "aaaaaaaacl", "aaaaaaaacm", "aaaaaaaacn", "aaaaaaaaco", "aaaaaaaacp", "aaaaaaaacq", "aaaaaaaacr",
             "aaaaaaaacs", "aaaaaaaact", "aaaaaaaacu", "aaaaaaaacv", "aaaaaaaacw", "aaaaaaaacx", "aaaaaaaacy",
             "aaaaaaaacz", "aaaaaaaada", "aaaaaaaadb", "aaaaaaaadc", "aaaaaaaadd", "aaaaaaaade", "aaaaaaaadf",
             "aaaaaaaadg", "aaaaaaaadh", "aaaaaaaadi", "aaaaaaaadj", "aaaaaaaadk", "aaaaaaaadl", "aaaaaaaadm",
             "aaaaaaaadn", "aaaaaaaado", "aaaaaaaadp", "aaaaaaaadq", "aaaaaaaadr", "aaaaaaaads", "aaaaaaaadt",
             "aaaaaaaadu", "aaaaaaaadv", "aaaaaaaadw", "aaaaaaaadx", "aaaaaaaady", "aaaaaaaadz", "aaaaaaaaea",
             "aaaaaaaaeb", "aaaaaaaaec", "aaaaaaaaed", "aaaaaaaaee", "aaaaaaaaef", "aaaaaaaaeg", "aaaaaaaaeh",
             "aaaaaaaaei", "aaaaaaaaej", "aaaaaaaaek", "aaaaaaaael", "aaaaaaaaem", "aaaaaaaaen", "aaaaaaaaeo",
             "aaaaaaaaep", "aaaaaaaaeq", "aaaaaaaaer", "aaaaaaaaes", "aaaaaaaaet", "aaaaaaaaeu", "aaaaaaaaev",
             "aaaaaaaaew", "aaaaaaaaex", "aaaaaaaaey", "aaaaaaaaez", "aaaaaaaafa", "aaaaaaaafb", "aaaaaaaafc",
             "aaaaaaaafd", "aaaaaaaafe", "aaaaaaaaff", "aaaaaaaafg", "aaaaaaaafh", "aaaaaaaafi", "aaaaaaaafj",
             "aaaaaaaafk", "aaaaaaaafl", "aaaaaaaafm", "aaaaaaaafn", "aaaaaaaafo", "aaaaaaaafp", "aaaaaaaafq",
             "aaaaaaaafr", "aaaaaaaafs", "aaaaaaaaft", "aaaaaaaafu", "aaaaaaaafv", "aaaaaaaafw", "aaaaaaaafx",
             "aaaaaaaafy", "aaaaaaaafz", "aaaaaaaaga", "aaaaaaaagb", "aaaaaaaagc", "aaaaaaaagd", "aaaaaaaage",
             "aaaaaaaagf", "aaaaaaaagg", "aaaaaaaagh", "aaaaaaaagi", "aaaaaaaagj", "aaaaaaaagk", "aaaaaaaagl",
             "aaaaaaaagm", "aaaaaaaagn", "aaaaaaaago", "aaaaaaaagp", "aaaaaaaagq", "aaaaaaaagr", "aaaaaaaags",
             "aaaaaaaagt", "aaaaaaaagu", "aaaaaaaagv", "aaaaaaaagw", "aaaaaaaagx", "aaaaaaaagy", "aaaaaaaagz",
             "aaaaaaaaha", "aaaaaaaahb", "aaaaaaaahc", "aaaaaaaahd", "aaaaaaaahe", "aaaaaaaahf", "aaaaaaaahg",
             "aaaaaaaahh", "aaaaaaaahi", "aaaaaaaahj", "aaaaaaaahk", "aaaaaaaahl", "aaaaaaaahm", "aaaaaaaahn",
             "aaaaaaaaho", "aaaaaaaahp", "aaaaaaaahq", "aaaaaaaahr", "aaaaaaaahs", "aaaaaaaaht", "aaaaaaaahu",
             "aaaaaaaahv", "aaaaaaaahw", "aaaaaaaahx", "aaaaaaaahy", "aaaaaaaahz", "aaaaaaaaia", "aaaaaaaaib",
             "aaaaaaaaic", "aaaaaaaaid", "aaaaaaaaie", "aaaaaaaaif", "aaaaaaaaig", "aaaaaaaaih", "aaaaaaaaii",
             "aaaaaaaaij", "aaaaaaaaik", "aaaaaaaail", "aaaaaaaaim", "aaaaaaaain", "aaaaaaaaio", "aaaaaaaaip",
             "aaaaaaaaiq", "aaaaaaaair", "aaaaaaaais", "aaaaaaaait", "aaaaaaaaiu", "aaaaaaaaiv", "aaaaaaaaiw",
             "aaaaaaaaix", "aaaaaaaaiy", "aaaaaaaaiz", "aaaaaaaaja", "aaaaaaaajb", "aaaaaaaajc", "aaaaaaaajd",
             "aaaaaaaaje", "aaaaaaaajf", "aaaaaaaajg", "aaaaaaaajh", "aaaaaaaaji", "aaaaaaaajj", "aaaaaaaajk",
             "aaaaaaaajl", "aaaaaaaajm", "aaaaaaaajn", "aaaaaaaajo", "aaaaaaaajp", "aaaaaaaajq", "aaaaaaaajr",
             "aaaaaaaajs", "aaaaaaaajt", "aaaaaaaaju", "aaaaaaaajv", "aaaaaaaajw", "aaaaaaaajx", "aaaaaaaajy",
             "aaaaaaaajz", "aaaaaaaaka", "aaaaaaaakb", "aaaaaaaakc", "aaaaaaaakd", "aaaaaaaake", "aaaaaaaakf",
             "aaaaaaaakg", "aaaaaaaakh", "aaaaaaaaki", "aaaaaaaakj", "aaaaaaaakk", "aaaaaaaakl", "aaaaaaaakm",
             "aaaaaaaakn", "aaaaaaaako", "aaaaaaaakp", "aaaaaaaakq", "aaaaaaaakr", "aaaaaaaaks", "aaaaaaaakt",
             "aaaaaaaaku", "aaaaaaaakv", "aaaaaaaakw", "aaaaaaaakx", "aaaaaaaaky", "aaaaaaaakz", "aaaaaaaala",
             "aaaaaaaalb", "aaaaaaaalc", "aaaaaaaald", "aaaaaaaale", "aaaaaaaalf", "aaaaaaaalg", "aaaaaaaalh",
             "aaaaaaaali", "aaaaaaaalj", "aaaaaaaalk", "aaaaaaaall", "aaaaaaaalm", "aaaaaaaaln", "aaaaaaaalo",
             "aaaaaaaalp", "aaaaaaaalq", "aaaaaaaalr", "aaaaaaaals", "aaaaaaaalt", "aaaaaaaalu", "aaaaaaaalv",
             "aaaaaaaalw", "aaaaaaaalx", "aaaaaaaaly", "aaaaaaaalz", "aaaaaaaama", "aaaaaaaamb", "aaaaaaaamc",
             "aaaaaaaamd", "aaaaaaaame", "aaaaaaaamf", "aaaaaaaamg", "aaaaaaaamh", "aaaaaaaami", "aaaaaaaamj",
             "aaaaaaaamk", "aaaaaaaaml", "aaaaaaaamm", "aaaaaaaamn", "aaaaaaaamo", "aaaaaaaamp", "aaaaaaaamq",
             "aaaaaaaamr", "aaaaaaaams", "aaaaaaaamt", "aaaaaaaamu", "aaaaaaaamv", "aaaaaaaamw", "aaaaaaaamx",
             "aaaaaaaamy", "aaaaaaaamz", "aaaaaaaana", "aaaaaaaanb", "aaaaaaaanc", "aaaaaaaand", "aaaaaaaane",
             "aaaaaaaanf", "aaaaaaaang", "aaaaaaaanh", "aaaaaaaani", "aaaaaaaanj", "aaaaaaaank", "aaaaaaaanl",
             "aaaaaaaanm", "aaaaaaaann", "aaaaaaaano", "aaaaaaaanp", "aaaaaaaanq", "aaaaaaaanr", "aaaaaaaans",
             "aaaaaaaant", "aaaaaaaanu", "aaaaaaaanv", "aaaaaaaanw", "aaaaaaaanx", "aaaaaaaany", "aaaaaaaanz",
             "aaaaaaaaoa", "aaaaaaaaob", "aaaaaaaaoc", "aaaaaaaaod", "aaaaaaaaoe", "aaaaaaaaof", "aaaaaaaaog",
             "aaaaaaaaoh", "aaaaaaaaoi", "aaaaaaaaoj", "aaaaaaaaok", "aaaaaaaaol", "aaaaaaaaom", "aaaaaaaaon",
             "aaaaaaaaoo", "aaaaaaaaop", "aaaaaaaaoq", "aaaaaaaaor", "aaaaaaaaos", "aaaaaaaaot", "aaaaaaaaou",
             "aaaaaaaaov", "aaaaaaaaow", "aaaaaaaaox", "aaaaaaaaoy", "aaaaaaaaoz", "aaaaaaaapa", "aaaaaaaapb",
             "aaaaaaaapc", "aaaaaaaapd", "aaaaaaaape", "aaaaaaaapf", "aaaaaaaapg", "aaaaaaaaph", "aaaaaaaapi",
             "aaaaaaaapj", "aaaaaaaapk", "aaaaaaaapl", "aaaaaaaapm", "aaaaaaaapn", "aaaaaaaapo", "aaaaaaaapp",
             "aaaaaaaapq", "aaaaaaaapr", "aaaaaaaaps", "aaaaaaaapt", "aaaaaaaapu", "aaaaaaaapv", "aaaaaaaapw",
             "aaaaaaaapx", "aaaaaaaapy", "aaaaaaaapz", "aaaaaaaaqa", "aaaaaaaaqb", "aaaaaaaaqc", "aaaaaaaaqd",
             "aaaaaaaaqe", "aaaaaaaaqf", "aaaaaaaaqg", "aaaaaaaaqh", "aaaaaaaaqi", "aaaaaaaaqj", "aaaaaaaaqk",
             "aaaaaaaaql", "aaaaaaaaqm", "aaaaaaaaqn", "aaaaaaaaqo", "aaaaaaaaqp", "aaaaaaaaqq", "aaaaaaaaqr",
             "aaaaaaaaqs", "aaaaaaaaqt", "aaaaaaaaqu", "aaaaaaaaqv", "aaaaaaaaqw", "aaaaaaaaqx", "aaaaaaaaqy",
             "aaaaaaaaqz", "aaaaaaaara", "aaaaaaaarb", "aaaaaaaarc", "aaaaaaaard", "aaaaaaaare", "aaaaaaaarf",
             "aaaaaaaarg", "aaaaaaaarh", "aaaaaaaari", "aaaaaaaarj", "aaaaaaaark", "aaaaaaaarl", "aaaaaaaarm",
             "aaaaaaaarn", "aaaaaaaaro", "aaaaaaaarp", "aaaaaaaarq", "aaaaaaaarr", "aaaaaaaars", "aaaaaaaart",
             "aaaaaaaaru", "aaaaaaaarv", "aaaaaaaarw", "aaaaaaaarx", "aaaaaaaary", "aaaaaaaarz", "aaaaaaaasa",
             "aaaaaaaasb", "aaaaaaaasc", "aaaaaaaasd", "aaaaaaaase", "aaaaaaaasf", "aaaaaaaasg", "aaaaaaaash",
             "aaaaaaaasi", "aaaaaaaasj", "aaaaaaaask", "aaaaaaaasl", "aaaaaaaasm", "aaaaaaaasn", "aaaaaaaaso",
             "aaaaaaaasp", "aaaaaaaasq", "aaaaaaaasr", "aaaaaaaass", "aaaaaaaast", "aaaaaaaasu", "aaaaaaaasv",
             "aaaaaaaasw", "aaaaaaaasx", "aaaaaaaasy", "aaaaaaaasz", "aaaaaaaata", "aaaaaaaatb", "aaaaaaaatc",
             "aaaaaaaatd", "aaaaaaaate", "aaaaaaaatf", "aaaaaaaatg", "aaaaaaaath", "aaaaaaaati", "aaaaaaaatj",
             "aaaaaaaatk", "aaaaaaaatl", "aaaaaaaatm", "aaaaaaaatn", "aaaaaaaato", "aaaaaaaatp", "aaaaaaaatq",
             "aaaaaaaatr", "aaaaaaaats", "aaaaaaaatt", "aaaaaaaatu", "aaaaaaaatv", "aaaaaaaatw", "aaaaaaaatx",
             "aaaaaaaaty", "aaaaaaaatz", "aaaaaaaaua", "aaaaaaaaub", "aaaaaaaauc", "aaaaaaaaud", "aaaaaaaaue",
             "aaaaaaaauf", "aaaaaaaaug", "aaaaaaaauh", "aaaaaaaaui", "aaaaaaaauj", "aaaaaaaauk", "aaaaaaaaul",
             "aaaaaaaaum", "aaaaaaaaun", "aaaaaaaauo", "aaaaaaaaup", "aaaaaaaauq", "aaaaaaaaur", "aaaaaaaaus",
             "aaaaaaaaut", "aaaaaaaauu", "aaaaaaaauv", "aaaaaaaauw", "aaaaaaaaux", "aaaaaaaauy", "aaaaaaaauz",
             "aaaaaaaava", "aaaaaaaavb", "aaaaaaaavc", "aaaaaaaavd", "aaaaaaaave", "aaaaaaaavf", "aaaaaaaavg",
             "aaaaaaaavh", "aaaaaaaavi", "aaaaaaaavj", "aaaaaaaavk", "aaaaaaaavl", "aaaaaaaavm", "aaaaaaaavn",
             "aaaaaaaavo", "aaaaaaaavp", "aaaaaaaavq", "aaaaaaaavr", "aaaaaaaavs", "aaaaaaaavt", "aaaaaaaavu",
             "aaaaaaaavv", "aaaaaaaavw", "aaaaaaaavx", "aaaaaaaavy", "aaaaaaaavz", "aaaaaaaawa", "aaaaaaaawb",
             "aaaaaaaawc", "aaaaaaaawd", "aaaaaaaawe", "aaaaaaaawf", "aaaaaaaawg", "aaaaaaaawh", "aaaaaaaawi",
             "aaaaaaaawj", "aaaaaaaawk", "aaaaaaaawl", "aaaaaaaawm", "aaaaaaaawn", "aaaaaaaawo", "aaaaaaaawp",
             "aaaaaaaawq", "aaaaaaaawr", "aaaaaaaaws", "aaaaaaaawt", "aaaaaaaawu", "aaaaaaaawv", "aaaaaaaaww",
             "aaaaaaaawx", "aaaaaaaawy", "aaaaaaaawz", "aaaaaaaaxa", "aaaaaaaaxb", "aaaaaaaaxc", "aaaaaaaaxd",
             "aaaaaaaaxe", "aaaaaaaaxf", "aaaaaaaaxg", "aaaaaaaaxh", "aaaaaaaaxi", "aaaaaaaaxj", "aaaaaaaaxk",
             "aaaaaaaaxl", "aaaaaaaaxm", "aaaaaaaaxn", "aaaaaaaaxo", "aaaaaaaaxp", "aaaaaaaaxq", "aaaaaaaaxr",
             "aaaaaaaaxs", "aaaaaaaaxt", "aaaaaaaaxu", "aaaaaaaaxv", "aaaaaaaaxw", "aaaaaaaaxx", "aaaaaaaaxy",
             "aaaaaaaaxz", "aaaaaaaaya", "aaaaaaaayb", "aaaaaaaayc", "aaaaaaaayd", "aaaaaaaaye", "aaaaaaaayf",
             "aaaaaaaayg", "aaaaaaaayh", "aaaaaaaayi", "aaaaaaaayj", "aaaaaaaayk", "aaaaaaaayl", "aaaaaaaaym",
             "aaaaaaaayn", "aaaaaaaayo", "aaaaaaaayp", "aaaaaaaayq", "aaaaaaaayr", "aaaaaaaays", "aaaaaaaayt",
             "aaaaaaaayu", "aaaaaaaayv", "aaaaaaaayw", "aaaaaaaayx", "aaaaaaaayy", "aaaaaaaayz", "aaaaaaaaza",
             "aaaaaaaazb", "aaaaaaaazc", "aaaaaaaazd", "aaaaaaaaze", "aaaaaaaazf", "aaaaaaaazg", "aaaaaaaazh",
             "aaaaaaaazi", "aaaaaaaazj", "aaaaaaaazk", "aaaaaaaazl", "aaaaaaaazm", "aaaaaaaazn", "aaaaaaaazo",
             "aaaaaaaazp", "aaaaaaaazq", "aaaaaaaazr", "aaaaaaaazs", "aaaaaaaazt", "aaaaaaaazu", "aaaaaaaazv",
             "aaaaaaaazw", "aaaaaaaazx", "aaaaaaaazy", "aaaaaaaazz"]

    res = Solution().findWords(board, words)
    assert res
