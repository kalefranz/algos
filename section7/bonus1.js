function factorial(n) {
    switch (n) {
        case 0:
        case 1:
            return 1;
        default:
            return n * factorial(n-1);
    }
    console.log('error');
}
// console.log(factorial(8));


function productOfArray(arr) {
    if (arr.length === 0) {
        return 0;
    }
    if (arr.length === 1) {
        return arr[0];
    }
    return arr[0] * productOfArray(arr.slice(1));
}
// console.log(productOfArray([1, 2, 3]));


function recursiveRange(n) {
    if (n === 0) return 0;
    return n + recursiveRange(n-1);
}
// console.log(recursiveRange(6));


function fib(n) {
    if (n <= 2) return 1;
    return fib(n-1) + fib(n-2);
}
// console.log(fib(4));

function reverse(word) {
    if (word.length === 1) return word[0];
    let len = word.length-1;
    return word[len] + reverse(word.slice(0, len));
}
// console.log(reverse("abcdefg"));


function isPalindrome(wordle) {
    function paliHelp(n) {
        if (n === 0) {
            return true;
        } else if (wordle[n] === wordle[wordle.length-n-1]) {
            return true && paliHelp(n-1);
        } else {
            return false;
        }
    }
    return paliHelp(Math.floor(wordle.length / 2));
}
// console.log(isPalindrome("tacocat"));


function someRecursive(arr, callback) {
    if (arr.length === 0) return false;
    return callback(arr[0]) || someRecursive(arr.slice(1), callback);
}
const isOdd = (val) => val % 2 !== 0;
// console.log(someRecursive([], isOdd));


function flatten(arrs) {
    var newArr = [];
    if (arrs instanceof Array) {
        if (arrs.length === 0) {
            return arrs;
        } else if (arrs.length === 1) {
            let element = arrs[0];
            if (element instanceof Array) {
                return flatten(element);
            } else {
                return [element];
            }
        } else {
            let element = arrs[0];
            if (element instanceof Array) {
                newArr = newArr.concat(flatten(element));
            } else {
                newArr.push(element);
            }
            newArr = newArr.concat(flatten(arrs.slice(1)));
            return newArr;
        }
    }
    console.log("error ${arrs}");
}
// console.log(flatten([1, 2, 3]));
// console.log(flatten([1, 2, [], 3, [4, 5] ]));
// console.log(flatten([1, [2, [3, 4], [[5]]]]));
console.log(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]));
