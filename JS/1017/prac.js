const palindrome = (str)=>{
  let len = parseInt(str.length/2)
  let cnt = 0
  
  for (let k=0; k<len; k++){
    let k2 = len-(k+1)

    if (str[k] === str[k2]){
      console.log(k, k2)
      console.log(str[k], str[k2])
      cnt++
    } else {
     break 
    }
  }
  console.log(cnt)
  let ans
  if (cnt!=0&&cnt===len){
    ans = 'true'
  } else {
    ans = 'false'
  }
  console.log(ans)
}
palindrome('level')
palindrome('hi')