var same_necklace = (word1, word2, n) => {
   n = n || 0 
   
   if(n === word2.length - 1)
     return word1 === word2
    

    if(word1.trim() === '' && word2.trim() === '')
      return true

    // Optimization 1
    // Necklace should be always same size.
    if(word1.length != word2.length)
      return false
    

    // Optimization 2
    // Necklace should weight the same. Their letters added together should 
    // amount the same final number. 
    // ['a','b'] => 95
    // ['b','a'] => 95
    //
    // This save us from unnecessary rotation.

    if(n === 0){
      let weight1 = word1.split('').map(p => p.charCodeAt(0)).reduce((a,n) => a+n)
      let weight2 = word2.split('').map(p => p.charCodeAt(0)).reduce((a,n) => a+n)
      
      if(weight1 !== weight2) {
        return false
      }
    }

    if(word1 === word2) {
     return true
    }
    
    let ww = word2.split('')
    let end = ww.pop()
    ww.unshift(end)
    n++
    return same_necklace(word1, ww.join(''), n) 
}

const test = () => {
  console.log(same_necklace("nicole", "icolen") === true) 
  console.log(same_necklace("nicole", "lenico") === true) 
  console.log(same_necklace("nicole", "coneli") === false) 
  console.log(same_necklace("aabaaaaabaab", "aabaabaabaaa") === true) 
  console.log(same_necklace("abc", "cba") === false) 
  console.log(same_necklace("xxyyy", "xxxyy") === false) 
  console.log(same_necklace("xyxxz", "xxyxz") === false)
  console.log(same_necklace("x", "x") === true) 
  console.log(same_necklace("x", "xx")===false) 
  console.log(same_necklace("x", "")===false) 
  console.log(same_necklace("", "")===true) 
}

var repeats = (word1, word2, n, r) => {
   n = n || 0
   r = r || 0 
   word2 = word2 || word1

    if(word1 === word2)
     r++

    if(word1 === '')
    return 1
    
    if(n === word1.length-1)
     return r
    
    let ww = word2.split('')
    let end = ww.pop()
    ww.unshift(end)
    n++
    return repeats(word1, ww.join(''), n, r) 
}

let input = require('fs').readFileSync('./e.txt').toString().split('\n')

let groups = input.reduce((acc, next) =>{
  if(next !== ''){
    acc[next.length] = acc[next.length] || []
    acc[next.length].push(next)
  }
  return acc
} ,{})

function evaluate(input){

  let store = {}
  let len  = input.length
  console.log('size: ', input.length)
  for(let x=0; x<len-1; x++) {
    let w1 = input[x]

    for(let y=x+1; y<len; y++){
       let w2 = input[y]
       let r = same_necklace(w1, w2)
        
       if(r === true){  
        store[w1] = store[w1] || []
        store[w1].push(w2)
       }  
    }
    
    if(store[w1] !== undefined && store[w1].length > 2) {
  
      console.log('solution: ', w1, store[w1])
      process.exit(0)
    }
  }

  return store
}

//let res = evaluate(['estop', 'pesto', 'stope', 'topes'])

let res = Object
  .keys(groups)
  .map(k => evaluate(groups[k]))

console.log('response ->', JSON.stringify(res))
 


