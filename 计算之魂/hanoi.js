/**
 * solution: recursion and divide and conquer
 * O(2^n-1)
 */
let count = 0;
const move = (n, from, to, temp) => {
  count++;
  if (n === 1) {
    console.log(`move from ${from} to ${to}`);
    return;
  }
  move(n - 1, from, temp, to);
  console.log(`move from ${from} to ${to}`);
  move(n - 1, temp, to, from);
};

const startTime = new Date().getTime();
move(64, "A", "B", "C");
const endTime = new Date().getTime();
console.log((endTime - startTime) / 1000, "seconds");

console.log(`total move: ${count} times`);
