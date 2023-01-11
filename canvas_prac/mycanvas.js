const canvas = document.querySelector("canvas")
const context = canvas.getContext("2d")
canvas.width = 800
canvas.height = 800
context.lineWidth = 3

// context.moveTo(50,50)
// context.lineTo(50,150)
// context.lineTo(150,150)
// context.lineTo(150,50)
// context.lineTo(50,50)
// context.strokeStyle = "red"
// context.stroke()

function downMouse(e){
  context.moveTo(e.offsetX, e.offsetY)
  // console.log(e)
  isPainting = true
}

function upMouse(){
  isPainting = false
  // context.beginPath()
  // context.moveTo(e.offsetX, e.offsetY)
}

function onMove(e){
  // console.log(isPainting)
  if (isPainting){
    context.lineTo(e.offsetX, e.offsetY)
    context.stroke()
    return
  }
  // path를 끊어주지 않으면 속성을 변경할 때마다 이전에 그린것까지 전부 변경된다.
  context.beginPath()
  context.moveTo(e.offsetX, e.offsetY)
}

function rstCanvas(e){
  console.log(rstbtn)
  console.log(e)
  context.clearRect(0,0,canvas.height,canvas.width)
}

let isPainting = false

canvas.addEventListener("mousedown", downMouse)
document.addEventListener("mouseup", upMouse)
canvas.addEventListener("mousemove", onMove)
// document.addEventListener("mouseup", ()=>{isPainting=false})

const rstbtn = document.querySelector('button')
console.log(rstbtn)
console.log(document)
rstbtn.addEventListener("click", rstCanvas)

