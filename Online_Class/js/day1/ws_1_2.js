function palindrome(str) {
  const pal = str.split('').reverse().join('')
  if (pal==str){
    console.log('true')
  } else {
    console.log('false')
  }
}

palindrome('level')