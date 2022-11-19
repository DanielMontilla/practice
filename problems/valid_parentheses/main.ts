import { assertEquals } from "https://deno.land/std@0.165.0/testing/asserts.ts";
const { test } = Deno;

/** 
 * problem: Valid Parentheses
 * @ https://leetcode.com/problems/valid-parentheses/
 * author: Daniel Montilla (https://github.com/DanielMontilla)
 */

const solution = (s: string): boolean => {
  type Open = '(' | '[' | '{';
  type Close = ')' | ']' | '}';

  const stack: Open[] = []
  const closing = {
    ')': '(',
    ']': '[',
    '}': '{'
  } as const;

  for (const c of s) {
    if (c in closing) { // If we find a bracket thats closing then:
      if (stack[stack.length - 1] == closing[c as Close]) {
        stack.pop();
      } else {
        return false;
      }
    } else {
      stack.push(c as Open)
    }
  }

  return stack.length <= 0;
}

test('test_0', () => { assertEquals(solution("()"), true) });
test('test_1', () => { assertEquals(solution("()[]{}"), true) });
test('test_2', () => { assertEquals(solution("(]"), false) });
test('test_3', () => { assertEquals(solution(")"), false) });
test('test_4', () => { assertEquals(solution("({}){[]}"), true) });
test('test_5', () => { assertEquals(solution("["), false) });

/** Notes:
 * Runtime: 107 ms, faster than 66.62% of TypeScript online submissions for Valid Parentheses.
 * Memory Usage: 44.6 MB, less than 48.39% of TypeScript online submissions for Valid Parentheses.
 * 
 * could prob optimize using better iteration methods (for loop instead of for of loop)
 */