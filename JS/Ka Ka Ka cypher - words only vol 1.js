function kaCokadekaMe(word) {
    const vowel = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"];
    const list = word.split("");
    list.splice(0, 0, "ka");

    for (let i = 0; i < list.length - 1; i++) {
        if (vowel.includes(list[i]) && !vowel.includes(list[i + 1])) {
            list.splice(i + 1, 0, "ka");
        }
    }
    return list.join("");
}

console.log(
    kaCokadekaMe("a")
    // "kaa"
);
console.log(
    kaCokadekaMe("z")
    // "kaz"
);
console.log(
    kaCokadekaMe("ka")
    // "kaka"
);
console.log(
    kaCokadekaMe("Abbaa")
    // "kaAkabbaa"
);
console.log(
    kaCokadekaMe("maintenance")
    // "kamaikantekanakance"
);
console.log(
    kaCokadekaMe("Woodie")
    // "kaWookadie"
);
console.log(
    kaCokadekaMe("Incomprehensibilities")
    // "kaIkancokamprekahekansikabikalikatiekas"
);
