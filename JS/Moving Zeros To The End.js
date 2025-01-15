function moveZeros(arr) {
    let count = 0;
    for (const element of arr) {
        if (element === 0) {
            count++;
        }
    }

    arr = arr.filter((item) => item !== 0);

    for (let i = 0; i < count; i++) {
        arr.push(0);
    }
    return arr;
}

// function moveZeros(arr) {
//     return [...arr.filter((n) => n !== 0), ...arr.filter((n) => n === 0)];
// }

console.log(
    moveZeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
    // [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
);

console.log(
    moveZeros([
        9, +0, 9, 1, 2, 1, 1, 3, 1, 9, +0, +0, 9, +0, +0, +0, +0, +0, +0, +0,
    ])
    // [ 9, 9, 1, 2, 1, 1, 3, 1, 9, 9, +0, +0, +0, +0, +0, +0, +0, +0, +0, +0 ]
);
