function arrayDiff(a, b) {
    for (let i = 0; i < a.length; i++) {
        for (let j = 0; j < b.length; j++) {
            if (a[i] == b[j]) {
                a = a.filter((item) => item !== b[j]);
            }
        }
    }
    return a;
}


// [2], "a was [1,2], b was [1]"
console.log(arrayDiff([1, 2], [1]));
// [2,2], "a was [1,2,2], b was [1]"
console.log(arrayDiff([1, 2, 2], [1]));
// [1], "a was [1,2,2], b was [2]"
console.log(arrayDiff([1, 2, 2], [2]));
// [1,2,2], "a was [1,2,2], b was []"
console.log(arrayDiff([1, 2, 2], []));
// "a was [], b was [1,2]"
console.log(arrayDiff([], [1, 2]));
// [3], "a was [1,2,3], b was [1,2]"
console.log(arrayDiff([1, 2, 3], [1, 2]));
