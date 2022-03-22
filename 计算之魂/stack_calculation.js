/**
 * solution: stack, last in first out
 * O(n)
 */
const string = "3+2*2-4/2";

// calculate priority
const stack = [];
let preInput = "";
string.split("").forEach((input) => {
  if (preInput === "*" || preInput === "/") {
    const operator = stack.pop();
    const num1 = stack.pop();
    const num2 = input;
    if (operator === "*") {
      stack.push(num1 * num2);
    } else {
      stack.push(num1 / num2);
    }
  } else {
    stack.push(input);
  }

  preInput = input;
});

// calculate result
const calculate = (num1, operator, num2) => {
  if (operator === "+") {
    return Number(num1) + Number(num2);
  } else if (operator === "-") {
    return Number(num1) - Number(num2);
  }
};
let result = calculate(stack[0], stack[1], stack[2]);
for (let i = 3; i < stack.length; i += 2) {
  result = calculate(result, stack[i], stack[i + 1]);
}

console.log(`${string} = ${result} from ${stack}`);

/**
 * solution: stack the same, plus with minus
 * O(n)
 */
const aString = "3+2*2-4/2";

// calculate priority
const aStack = [];
let aPreInput = "";
aString.split("").forEach((input) => {
  if (aPreInput === "*" || aPreInput === "/") {
    const operator = aStack.pop();
    const num1 = aStack.pop();
    const num2 = input;
    if (operator === "*") {
      aStack.push(num1 * num2);
    } else {
      aStack.push(num1 / num2);
    }
  } else if (aPreInput === "-") {
    aStack.pop();
    aStack.push(`-${input}`);
  } else if (aPreInput === "+") {
    aStack.pop();
    aStack.push(input);
  } else {
    aStack.push(input);
  }

  aPreInput = input;
});

let aResult = 0;
aStack.forEach((num) => {
  aResult += Number(num);
});

console.log(`${aString} = ${aResult} from ${aStack}`);
