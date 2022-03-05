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

// solution two: forward and backward
// const numList = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
const numList = [1, 1, 1, 1, -5, 1, 1, 1, 1];
let forwardMaxIndex = 0;
let backwardMaxIndex = numList.length - 1;
let forwardMaxSum = 0;
let backwardMaxSum = 0;

let forwardCurSum = 0;
numList.forEach((curVal, index) => {
  forwardCurSum += curVal;
  if (forwardCurSum > forwardMaxSum) {
    forwardMaxSum = forwardCurSum;
    forwardMaxIndex = index;
  }
});
console.log(`forwardMaxIndex: ${forwardMaxIndex}, forwardMaxSum: ${forwardMaxSum}`);

let backwardCurSum = 0;
for (let i = numList.length - 1; i >= 0; i--) {
  backwardCurSum += numList[i];
  if (backwardCurSum > backwardMaxSum) {
    backwardMaxSum = backwardCurSum;
    backwardMaxIndex = i;
  }
}
console.log(`backwardMaxIndex: ${backwardMaxIndex}, backwardMaxSum: ${backwardMaxSum}`);

if (forwardMaxIndex > backwardMaxIndex) {
  let sum = 0;
  for (let i = backwardMaxIndex; i <= forwardMaxIndex; i++) {
    sum += numList[i];
  }
  console.log(`sum[${backwardMaxIndex}, ${forwardMaxIndex}] = ${sum}`);
} else {
  if (forwardMaxSum > backwardMaxSum) {
    console.log(`sum[0, ${forwardMaxIndex}] = ${forwardMaxSum}`);
  } else {
    console.log(`sum[${backwardMaxIndex}, ${numList.length-1}] = ${backwardMaxSum}`);
  }
}