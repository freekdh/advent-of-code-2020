from advent_of_code_2020.day18.solve import EquationEvaluator


def test():
    equation_evaluator = EquationEvaluator()
    assert equation_evaluator.evaluate("2 * 3 + (4 * 5)") == 26
    assert equation_evaluator.evaluate("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
    assert (
        equation_evaluator.evaluate("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")
        == 12240
    )
    assert (
        equation_evaluator.evaluate("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")
        == 13632
    )