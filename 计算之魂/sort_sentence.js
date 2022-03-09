/**
 * solution one: in-place
 * O(n)
 */
const sentence = "is2 sentence4 This1 a3";
const words = sentence.split(" ");
const wordsTemp = new Array(words.length);
words.forEach((word) => {
  const seq = word.charAt(word.length - 1);
  wordsTemp[seq - 1] = word;
});
console.log(wordsTemp.join(" "));

/**
 * solution two: heap
 * O(nlogn)
 */
const sentenceHip = "is2 sentence4 This1 a3";
const wordsHip = sentenceHip.split(" ");
const wordHipSwap = (index1, index2) => {
  const temp = wordsHip[index1];
  wordsHip[index1] = wordsHip[index2];
  wordsHip[index2] = temp;
};
const maxHeap = (start, end) => {
  const dad = start;
  let leftSon = 2 * dad + 1;

  // out of bound
  if (leftSon >= end) {
    return;
  }

  // find the max son
  const leftSonWord = wordsHip[leftSon];
  const leftSonSeq = leftSonWord.charAt(leftSonWord.length - 1);
  if (leftSon + 1 < end) {
    const rightSonWord = wordsHip[leftSon + 1];
    const rightSonSeq = rightSonWord.charAt(rightSonWord.length - 1);
    if (leftSonSeq > rightSonSeq) {
      leftSon++;
    }
  }

  // swap
  const dadWord = wordsHip[dad];
  const dadSeq = dadWord.charAt(dadWord.length - 1);
  if (leftSonSeq > dadSeq) {
    wordHipSwap(leftSon - 1, dad);
    maxHeap(leftSon - 1, end);
  }
};

// build heap
const len = wordsHip.length;
const mid = Math.floor(len / 2);
for (let i = mid - 1; i >= 0; i--) {
  maxHeap(i, len);
}

// sort
for (let i = len - 1; i > 0; i--) {
  wordHipSwap(0, i);
  maxHeap(0, i);
}

console.log(wordsHip.join(" "));
