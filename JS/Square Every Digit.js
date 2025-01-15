function squareDigits(num) {
    let ans = "";
    const nums = num.toString();

    for (const element of nums) {
        ans += element ** 2;
    }
    return parseInt(ans);
}

console.log(squareDigits(3212)); // 9414
console.log(squareDigits(2112)); // 4114
console.log(squareDigits(0)); // 0