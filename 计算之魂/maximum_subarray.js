// solution one
const nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
let curSum = 0;
let maxSum = 0;
let startIndex = 0;
let endIndex = 0;

nums.forEach((curVal, index) => {
  curSum = Math.max(curSum + curVal, curVal);
  if (curSum < 0) {
    startIndex = index + 1;
  }
  if (curSum > maxSum) {
    maxSum = curSum;
    endIndex = index;
  } 
  console.log(`${index}. curSum: ${curSum}, maxSum: ${maxSum}`);
});

console.log(`sum[${startIndex}, ${endIndex}] = ${maxSum}`);
