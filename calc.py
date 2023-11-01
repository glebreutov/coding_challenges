import copy
from typing import List


class Solution:

    @staticmethod
    def is_op(c):
        return c in ["+", "-", "*", "/", "(", ")"]

    @staticmethod
    def parse(expr) -> List:
        seq = []
        val_buffer = ""
        for i, s in enumerate(expr):
            if s == " ":
                continue

            if Solution.is_op(s):
                if val_buffer:
                    seq.append(int(val_buffer))
                    val_buffer = ""
                seq.append(s)
            else:
                val_buffer += s

        if val_buffer:
            seq.append(int(val_buffer))

        return seq
            
    @staticmethod
    def parenthesis(seq: List):
        buffer = []
        while seq:
            el = seq.pop(0)
            if el == "(":
                group = Solution.parenthesis(seq)
                buffer.append(group)
            elif el == ")":
                return buffer
            else:
                buffer.append(el)

        return buffer

    @staticmethod
    def op_priority(seq: List):
        buffer = []
        while seq:
            el = seq.pop(0)
            if type(el) == list:
                buffer.append(Solution.op_priority(el))
            elif el in ["*", "/"]:
                right_val = seq.pop(0)
                right = Solution.op_priority(right_val) if type(right_val) == list else right_val
                buffer.append([buffer.pop(), el, right])
            else:
                buffer.append(el)

        return buffer

    @staticmethod
    def eval_expr(graph) -> int:
        left = None
        op = None
        right = None
        while graph:
            el = graph.pop(0)
            if type(el) == list and not op:
                left = Solution.eval_expr(el)
            elif type(el) == list and op:
                right = Solution.eval_expr(el)
            elif Solution.is_op(el):
                op = el
            elif not op:
                left = el
            else:
                right = el

            if left is not None and right is not None  and op:
                match op:
                    case "*":
                        left *= right
                    case "/":
                        left /= right
                    case "-":
                        left -= right
                    case "+":
                        left += right
                right = None
                op = None
            elif left is None and right is not None and op:
                left = -1 * right
                right = None
                op = None
        return left


    def calculate(self, expr: str) -> int:
        seq = Solution.parse(expr)
        prnt = Solution.parenthesis(seq)
        prior = Solution.op_priority(copy.deepcopy(prnt))

        return Solution.eval_expr(prior)


def test_case1():
    seq = Solution.parse("1 + 1")
    assert seq
    assert Solution().calculate("1 + 1") == 2



def test_case2():
    assert Solution().calculate(" 2-1 + 2 ") == 3


def test_case3():
    assert Solution().calculate("(1+(4+5+2)-3)+(6+8)") == 23


def test_case4():
    assert Solution().calculate("-1-2") == -3

def test_case5():
    assert Solution().calculate("2*4+1") == 9
    assert Solution().calculate("1 + 2*4") == 9


def test_case6():
    assert Solution().calculate("4/2") == 2
    assert Solution().calculate("5/2") == 2.5


def test_case_prior1():
    seq = Solution.parse("(1+(2+3*8)")
    prnt = Solution.parenthesis(seq)
    prior = Solution.op_priority(copy.deepcopy(prnt))

    assert prior


def test_case_big():
    s = "5+3-4-(1+2-7+(10-1+3+5+(3-0+(8-(3+(8-(10-(6-10-8-7+(0+0+7)-10+5-3-2+(9+0+(7+(2-(2-(9)-2+5+4+2+(2+9+1+5+5-8-9-2-9+1+0)-(5-(9)-(0-(7+9)+(10+(6-4+6))+0-2+(10+7+(8+(7-(8-(3)+(2)+(10-6+10-(2)-7-(2)+(3+(8))+(1-3-8)+6-(4+1)+(6))+6-(1)-(10+(4)+(8)+(5+(0))+(3-(6))-(9)-(4)+(2))))))-1)))+(9+6)+(0))))+3-(1))+(7))))))))"

    assert Solution().calculate("(6-10-8-7+(0+0+7)") == (6-10-8-7+(0+0+7))
    # assert Solution().calculate(s) == -35