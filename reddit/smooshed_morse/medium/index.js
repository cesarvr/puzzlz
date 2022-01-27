const MORSE = `.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..`.split(' ')
const ALPHA = function() {
  let alpha = []
  for (var i = 65; i <= 90; i++) 
    alpha.push( String.fromCharCode(i).toLowerCase() )
  return alpha
}()

let Mapping = ALPHA.reduce((acc, curr, idx) => Object.assign(acc, {[ MORSE[idx] ]: curr }) ,{})

/*
 "wirnbfzehatqlojpgcvusyxkmd"

(".--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----..")

  a: .
  b: -
  c: .-
  candidate = '.'             [a, ]
               -
               -.
               ..
               -.-
               .-
               .-.
               ...
               ...- h
               ...- h
 */
 
const build_blocks = (blocks, partial) => {
 let candidate = ''
 let acc = []
 let solution =  []
 partial = partial || []

 while(true) {
  let l = blocks.shift() 
  if(l !== undefined)
    candidate += l
  else {
    candidate.split('').reverse().forEach(c => blocks.unshift(c))
    return solution
  }

  let letter = Mapping[candidate]

  if(letter !== undefined && partial.indexOf(letter) === -1) {
    partial.push(letter)
    solution = build_blocks(blocks, partial)

    if(solution.length > 0 || blocks.length === 0) {  // We only got here if we hit the end
      solution.unshift(letter)
      return solution
    }else
      partial.pop()
  }
  
  if(candidate.length === 4 || blocks.length === 0) {

    candidate.split('').reverse().forEach(c => blocks.unshift(c))
    return solution
  }
 }


 
  return solution
}


const smalpha = (morse_code) => {
  let morse = morse_code.split('')
  let r = build_blocks(morse).join('')
 // console.log(r.length === 'wirnbfzehatqlojpgcvusyxkmd'.length)
  return r
}

module.exports = smalpha

/*
{
  '.-': 'a',
  '-...': 'b',
  '-.-.': 'c',
  '-..': 'd',
  '.': 'e',
  '..-.': 'f',
  '--.': 'g',
  '....': 'h',
  '..': 'i',
  '.---': 'j',
  '-.-': 'k',
  '.-..': 'l',
  '--': 'm',
  '-.': 'n',
  '---': 'o',
  '.--.': 'p',
  '--.-': 'q',
  '.-.': 'r',
  '...': 's',
  '-': 't',
  '..-': 'u',
  '...-': 'v',
  '.--': 'w',
  '-..-': 'x',
  '-.--': 'y',
  '--..': 'z'
}

*/
//smalpha('')

//console.log(Mapping)
//let n = smalpha(".--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----..")
//console.log('translation ->',n)
