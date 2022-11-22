import { assertEquals } from "https://deno.land/std@0.165.0/testing/asserts.ts";
const { test } = Deno;

/** 
 * problem: Daily Temperatures
 * @ https://leetcode.com/problems/daily-temperatures/
 * author: Daniel Montilla (https://github.com/DanielMontilla)
 */

type StackEl = [temp: number, day: number];

const solution =  (temperatures: number[]): number[] => {
  const res = Array<number>(temperatures.length);
  const stack = Array<number>();

  main: for (let i = temperatures.length - 1; i >= 0; i--) {

    while (stack[stack.length - 1] != undefined) {

      const top = stack[stack.length - 1];

      if (temperatures[i] < temperatures[top]) {
        stack.push(i);
        res[i] = top - i;
        continue main;
      } else {
        stack.pop();
      }
    }

    
    stack.push(i);
    res[i] = 0;
  }

  return res;
}

test('test_0', () => { assertEquals(solution([73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0]) });
test('test_0', () => { assertEquals(solution([30,40,50,60]), [1,1,1,0]) });
test('test_0', () => { assertEquals(solution([30,60,90]), [1,1,0]) });

solution([73,74,75,71,69,72,76,73])

/** Notes:
 * Runtime: 545 ms, faster than 46.20% of TypeScript online submissions for Daily Temperatures.
 * Memory Usage: 63.7 MB, less than 82.07% of TypeScript online submissions for Daily Temperatures.
 * 
 * Maybe there is a more efficient two pointer solution...
 */