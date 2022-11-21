import { assertEquals } from "https://deno.land/std@0.165.0/testing/asserts.ts";

/** 
 * problem: Evaluate Reverse Polish Notation
 * @ https://leetcode.com/problems/evaluate-reverse-polish-notation/
 * author: Daniel Montilla (https://github.com/DanielMontilla)
 */

const { test } = Deno;
const OPERATORS = ['+', '-', '*', '/'] as const;
type Operator = typeof OPERATORS[number];

const solution = (tokens: string[]): number => {
  const parseOperation = (operand1: number, operator: Operator, operand2: number): number => {
    if (operator == '+') return operand1 + operand2;
    if (operator == '-') return operand1 - operand2;
    if (operator == '*') return operand1 * operand2;
    if (operator == '/') {
      const res = operand1 / operand2;
      return res > 0 ? Math.floor(res) : Math.ceil(res);
    }
    throw new Error(`invalid operator ${operator}...?`);
  }

  const stack = [] as number[];
  for (let i = 0; i < tokens.length; i++) {
    const char = tokens[i];

    if (OPERATORS.includes(char as Operator)) {
      const a = stack.pop();
      const b = stack.pop();
      if (a == undefined || b == undefined) throw new Error('invalid expresion...');
      stack.push(parseOperation(b, char as Operator, a));
    } else {
      stack.push(parseInt(char))
    }
  }

  return stack[0];
}

const solution_1 = (tokens: string[]): number => {
  const stack = [] as number[];
  for (let i = 0; i < tokens.length; i++) {
    const char = parseInt(tokens[i]);
    const token = isNaN(char) ? tokens[i] : char;
    
    if (typeof token == 'number') {
      stack.push(token);
    } else {
      const a = stack.pop() as number;
      const b = stack.pop() as number;
      let res = 0;

      switch (token) {
        case '+':
          res = b + a;
          break;
        case '-':
          res = b - a;
          break;
        case '*':
          res = b * a;
          break;
        case '/':
          res = b / a;
          res = res > 0 ? Math.floor(res) : Math.ceil(res);
          break;
      }
      stack.push(res);
    }
  }

  return stack[0];
}

test('0_test_0', () => { assertEquals(solution(["4","13","5","/","+"]), 6) });
test('0_test_1', () => { assertEquals(solution(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22) });
test('0_test_2', () => { assertEquals(solution(["2","1","+","3","*"]), 9) });

test('1_test_0', () => { assertEquals(solution_1(["4","13","5","/","+"]), 6) });
test('1_test_1', () => { assertEquals(solution_1(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22) });
test('1_test_2', () => { assertEquals(solution_1(["2","1","+","3","*"]), 9) });

/** Notes:
 * Solution
 * Runtime: 132 ms, faster than 44.34% of TypeScript online submissions for Evaluate Reverse Polish Notation.
 * Memory Usage: 45.2 MB, less than 83.26% of TypeScript online submissions for Evaluate Reverse Polish Notation.
 * 
 * Solution_1
 * Runtime: 133 ms, faster than 43.44% of TypeScript online submissions for Evaluate Reverse Polish Notation.
 * Memory Usage: 45.5 MB, less than 71.49% of TypeScript online submissions for Evaluate Reverse Polish Notation.
 * 
 * both solutions have a time complexity of O(n) and a space complexity of O(n)
 */