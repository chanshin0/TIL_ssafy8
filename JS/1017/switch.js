// <<switch문>>

let b = prompt()
let a = 10

switch (b) {
  case "더하기":{
    a += 2
    break
  }
  case "곱하기":{
    a *= 2
    break
  }
  default:
    a -= 2
}
console.log(a)