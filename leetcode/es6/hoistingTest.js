hoistedFn();
// test = 5; // Breaks!

function hoistedFn() {
  console.log(test);
}

var test = 5; // Hoists test, so it DOESN'T break, BUT still prints undef obv

// unproven conclusion: vars are hoisted BEFORE functions? 
