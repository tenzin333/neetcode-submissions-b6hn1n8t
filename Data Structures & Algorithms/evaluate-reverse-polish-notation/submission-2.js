class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        const operators = new Set(['+', '-', '/', '*']);
        let result = 0;
        while (tokens.length > 1) {
            for (let i = 0; i < tokens.length; i++) {
                if (operators.has(tokens[i])) {
                    const op1 = tokens[i-2];
                    const op2 = tokens[i-1];
                    switch (tokens[i]) {

                        case '+': result = Number(op1) + Number(op2);
                                            break;
                        case '-': result = Number(op1) - Number(op2);
                                            break;
                        case '/': result = Math.trunc(op1/op2);
                                            break;
                        case '*':  result = Number(op1) * Number(op2);
                                            break;
                }
                    tokens.splice(i-2,3,result.toString());
                    break;
                }

            }

        }

        return Number(tokens[0]);

    }
}
