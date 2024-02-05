/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
  const vowels = 'aeiouAEIOU';
  const sArray = s.split(''); 
  const vowelArray = sArray.filter(char => vowels.includes(char)); 

  return sArray.map(char => vowels.includes(char) ? vowelArray.pop() : char).join('');
}