// Qn-1 JavaScript Program To Print Hello World
// console.log("Hello World!")

// Qn-2 Add two numbers
// let a = 1;
// let b = 2;
// let sum = a + b;
// console.log("The sum of numbers is" + sum);

// Qn-5 JavaScript Program to Swap Two Variables
// let a = 1;
// let b = 2;
// let temp;
// console.log("The numbers before swapping is " +a+ " and " + b );
// // temp = a;
// // a = b;
// // b = temp;
  
// a = a + b;
// b = a - b;
// a = a - b;
// console.log("The numbers after swapping is " +a+ " and " + b );

// Qn-10 Javascript Program to Check if a number is Positive, Negative, or Zero
// let num = 100
//         if (num > 0){
//             console.log("The number is positive")
//         }
//         else if (num < 0){
//             console.log("The number is negative")
//         }
//         else{
//             console.log("The number is zero")
//         }


// Qn-11 Javascript Program to Check if a Number is Odd or Even
        // num = 50
        // if((num % 2) == 0){
        //     console.log("The number is even")
        // }
        // else{
        //     console.log("The number is odd")
        // }

// Qn-12 JavaScript Program to Find the Largest Among Three Numbers
        // let a = 10;
        // let b = 20;
        // let c = 30;
        // if ((a>b) && (a>c)){
        //     console.log(a + " is the largest number");
        // }
        // else if ((b>a) && (b>c)){
        //     console.log(b + " is the largest number");
        // }
        // else{
        //     console.log(c + " is the largest number");
        // }

// Qn-13 JavaScript Program to Check Prime Number
// const number = parseInt(prompt("Enter a positive number: "));
// let isPrime = true;
// if (number === 1) {
//     console.log("1 is neither prime nor composite number.");
// }
// else if (number > 1) {
//     for (let i = 2; i <= number/2; i++) {
//         if (number % i == 0) {
//             isPrime = false;
//             break;
//         }
//     }
//     if (isPrime) {
//         console.log(`${number} is a prime number`);
//     } else {
//         console.log(`${number} is a not prime number`);
//     }
// }
// else {
//     console.log("The number is not a prime number.");
// }

// Qn-14 JavaScript Program to Print All Prime Numbers in an Interval
// const lowerNumber = parseInt(prompt("Enter the lower number: "));
// const higherNumber = parseInt(prompt("Enter the higher number: "));     
// console.log(`Prime numbers between ${lowerNumber} and ${higherNumber} are:`);

// for (let i = lowerNumber; i <= higherNumber; i++) {
//         let isPrime = true;
//         if (i === 1) {
//                 isPrime = false;
//         }
//         else {
//             for (let j = 2; j <= i / 2; j++) {
//                 if (i % j == 0) {
//                     isPrime = false;
//                     break;
//                 }
//             }
//         }
//         if (isPrime) {
//                 console.log(i);
//         }
// }

// Qn-15 JavaScript Program to Find the Factorial of a Number
// const number = parseInt(prompt("Enter a positive integer: "));
// let factorial = 1;   
// if (number < 0) {
//     console.log("Error! Factorial for negative number does not exist.");
// }
// else if (number === 0) {
//     console.log(`The factorial of 0 is 1.`);
// }
// else {
//     for (let i = 1; i <= number; i++) {
//         factorial *= i;
//     }
//     console.log(`The factorial of ${number} is ${factorial}.`);
// }


// Qn-16 JavaScript Program to Display the Multiplication Table
// const number = parseInt(prompt("Enter a number to display its multiplication table: "));
// console.log(`Multiplication table of ${number}:`);
// for (let i = 1; i <= 10; i++) {
//     const result = number * i;
//     console.log(`${number} x ${i} = ${result}`);
// }


// Qn-17 JavaScript Program to Generate Fibonacci Series
// const nterms = parseInt(prompt("Enter the number of terms: "));
// let n1 = 0, n2 = 1, nextTerm;
// console.log("Fibonacci Series:");
// for (let i = 1; i <= nterms; i++) {
//     console.log(n1);
//     nextTerm = n1 + n2;
//     n1 = n2;
//     n2 = nextTerm;
// }


