/**
 * solution: divide and conquer for heap
 * O(n)
 */
const tree = [3, 9, 20, null, null, 15, 7];
const maximumDepth = (index = 0) => {
  const node = tree[index];
  if (!node) return 0;
  const left = maximumDepth(2 * index + 1);
  const right = maximumDepth(2 * index + 2);
  return Math.max(left, right) + 1;
};

console.log(`maximum depth of binary tree is ${maximumDepth()}`);
