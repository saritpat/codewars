function thirt(n) {
    let str = n.toString();
    let temp = 0
    let digit = 0

    while (true) {
        for (let i = str.length-1; i >= 0; i--) {
            temp += parseInt(str[i]) * (10**digit % 13)
            digit++;
        }

        if (str == temp) {
            return parseInt(str)
        } else {
            str = temp.toString()
            temp = 0
            digit = 0
        }
    }
}

console.log(
    thirt(8529)
    // 79
);
console.log(
    thirt(85299258)
    // 31
);
console.log(
    thirt(5634)
    // 57
);
console.log(
    thirt(1111111111)
    // 71
);
console.log(
    thirt(987654321)
    // 30
);
