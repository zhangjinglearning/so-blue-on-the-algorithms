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
const getWordSequence = (son) => {
  const sonWord = wordsHip[son];
  const sonSeq = sonWord.charAt(sonWord.length - 1);
  return sonSeq;
};
const maxHeap = (start, end) => {
  const dad = start;
  let son = dad * 2 + 1;

  // out of bound
  if (son >= end) {
    return;
  }

  // find the bigger son
  if (son + 1 < end) {
    const son1Seq = getWordSequence(son);
    const son2Seq = getWordSequence(son + 1);
    if (son1Seq < son2Seq) {
      son++;
    }
  }

  // compare with dad
  const sonSeq = getWordSequence(son);
  const dadSeq = getWordSequence(dad);
  if (sonSeq > dadSeq) {
    wordHipSwap(son, dad);
    maxHeap(son, end);
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
