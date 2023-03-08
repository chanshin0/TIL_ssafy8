const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Please enter some input: ", function(userInput) {
    //   console.log("You entered: " + userInput);
    const counts = ["zero", "one","two","three","four","five","six","seven","eight","nine"]
    let answer = ""
    let idx = 0

    // console.log(a,b,c)
    while (idx <= userInput.length) {
        let a = userInput.slice(idx, 3)
        let b = userInput.slice(idx, 4)
        let c = userInput.slice(idx, 5)
        for (const count of counts){
            console.log(count)
            if (count===a) {
                 answer += String(counts.indexOf(count))
                 idx += 3 
                 break
            }
            else if (count===b){
                 answer += String(counts.indexOf(count))
                 idx += 4 
                 break
            }
            else if (count===c){
                 answer += String(counts.indexOf(count))
                 idx += 5 
                 break
            } else {
                 answer += count
                 idx += 1
                 break
            }
            
         }
         console.log(answer)

    }
    console.log(answer)
    rl.close();
});





