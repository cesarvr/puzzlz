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

function test(e1 , e2 ){
	console.log('test result: ', e1 === e2 ? 'Pass': 'Fail')

}

let smalpha = require('./index')
function test2(e1){
	let e = smalpha(e1)
	console.log('decoded:',e)

	test(smorse(e), e1)
	console.log('')
}

function bonus1(){
	let list = require('fs').readFileSync('./bonus.txt').toString().split('\n')
	list = list.map(l => smalpha(l))
	console.log(list)
}

test2('.--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----..')
test2('.----...---.-....--.-........-----....--.-..-.-..--.--...--..-.---.--..-.-...--..-')
test2('..-...-..-....--.---.---.---..-..--....-.....-..-.--.-.-.--.-..--.--..--.----..-..')

test( smorse('etnicdskbhwmrxgopqlfavjuyz') , '.--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----..' )
test( smorse('wirnbfzehatqlojpgcvusyxkmd') , '.--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----..' )


//bonus1()


