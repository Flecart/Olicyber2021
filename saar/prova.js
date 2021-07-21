// import "crypto-js"

// const SPN_KEY_SIZE_BITS = 128;
// const SPN_KEY_SIZE_BYTES = SPN_KEY_SIZE_BITS / 8;
// const SPN_BLOCK_SIZE_BITS = 128;
// const SPN_BLOCK_SIZE_BYTES = SPN_BLOCK_SIZE_BITS / 8;

// function gen_key_spn() {
//     const key = new Uint8Array(SPN_KEY_SIZE_BYTES);
//     crypto.getRandomValues(key);
//     return key;
// }


// console.log(gen_key_spn())
roundkey = [1,2,3,4,5,6,7,8,9,0]
roundkey = roundkey.concat(roundkey.splice(0, 2));
console.log(roundkey)