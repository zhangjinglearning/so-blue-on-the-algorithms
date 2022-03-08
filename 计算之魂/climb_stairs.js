/**
 * solution one: recursive by fibonacci
 * O(2^n)
 */
const climbStairs = (n) => {
  if (n < 3) {
    return n;
  }
  return climbStairs(n - 1) + climbStairs(n - 2);
};

console.log("climb stairs:", climbStairs(20));
