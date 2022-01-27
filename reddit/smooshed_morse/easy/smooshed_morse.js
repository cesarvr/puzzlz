/* 20190805_challenge_380_easy_smooshed_morse_code_1 */ 

const morse = `.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..`.split(' ')

const letters = function(){
  let alpha = {}
  let cnt = 0
  for(let i= 65; i <= 90; i+=1){
    alpha[String.fromCharCode(i).toLowerCase()] = morse[cnt]
    cnt++
  }

  return alpha
}()

const smorse = function(w1) {
  return w1.split('').map(n => letters[n]).join('')
}

console.log(smorse("sos"))
console.log(smorse("sos")==='...---...')

console.log(smorse("daily") === "-...-...-..-.--")
console.log(smorse("programmer") === ".--..-.-----..-..-----..-.")
console.log(smorse("bits") === "-.....-...")
console.log(smorse("three") === "-.....-...")

console.log(smorse("bits"))
console.log(smorse("three"))

let words = require('fs').readFileSync('./e.txt').toString().split('\n')
let ret = require('fs').readFileSync('./e.txt').toString().split('\n').map(p => smorse(p))

let count = ret.reduce((acc, next) => {
  for(let i=0; i<next.length; i++){
    if(next[i] === '.')
      acc.dot += 1

    if(next[i] === '-')
      acc.dash +=1
  }
  return acc
}, {dot:0, dash:0})


console.log('count: ', count)

let count2 = ret.reduce((acc, next) => {
  acc[next]= acc[next] || 0
  acc[next] += 1
  return acc
},{})

let finding = {code:'', max:0}
for (let [key, value] of Object.entries(count2)) {
  if(value > 12) {
    console.log('v: ', key, ' v:', value)
    break;
  }
}

let max_dash = ret.forEach(next =>{
  let dash =0

  for(let i=0; i<next.length; i++){
    if(next[i] === '-'){
      dash++
      if(dash === 15){
        console.log(next, dash)
        return 
      }
    }else{
      dash = 0
    }
  }

})

console.log('perfect:', smorse('counterdemonstrations'))
console.log('', smorse('etnhkoqgdivmjsbacrfpxzwluy') )
console.log('.--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----..')

console.log('', smorse('etnicdskbhwmrxgopqlfavjuyz') === '.--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----..' )
process.exit(0)

let pb = words.filter(w => w.length === 21).map(w => Object.assign({word: w, coded:smorse(w)}))

pb = pb.filter(({coded}) => {
  let pck = coded.split('')
  return pck.filter(p => p === '.').length === pck.filter(p=> p==='-').length
})

console.log('perfect:', pb)


let palindrome = words.filter(w => w.length === 13).map(w => Object.assign({word: w, coded:smorse(w)}))

palindrome = palindrome.filter( ({coded}) => {
  return coded === coded.split('').reverse().join('')
})

console.log('palindrome:', palindrome)



let unique = ret.filter(coded => coded.length === 13) 

console.log('pre-unique ->', unique.length)

unique = unique.filter(coded => ret.filter( n => n.includes(coded)).length < 1  )
//unique = ret.filter( n => n.includes(unique[1]) ) 
console.log(ret)
console.log('unique ->', unique.length)


require('fs').writeFileSync('./morse_db',ret.join('\n'))








