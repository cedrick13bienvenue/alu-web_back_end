# ES6 Promises

## Description
Ten exercises on ES6 Promises: creating and settling them, `then`/
`catch`/`finally`, `Promise.all`, `Promise.allSettled`, `Promise.race`,
and `throw`/`try`/`catch` for synchronous error handling.

## Resources
- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [JavaScript Promise: An introduction](https://web.dev/promises/)
- [Await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
- [Async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)

## Learning Objectives
By the end of this project, you should be able to explain, without Google:
- Promises (how, why, and what)
- How to use `then`, `resolve`, and `catch`
- How to use every method of the `Promise` object
- `throw`/`try`
- The `await` operator
- How to use an `async` function

## Requirements
- All files executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- All files end with a new line
- Code uses the `.js` extension
- Tested with Jest (`npm run test`), linted with ESLint
- All functions are exported

## Setup
```
npm install
```

## Tasks
| File | Description |
| --- | --- |
| `0-promise.js` | `getResponseFromAPI` - returns a resolved Promise |
| `1-promise.js` | `getFullResponseFromAPI` - resolves or rejects based on a boolean |
| `2-then.js` | `handleResponseFromAPI` - `then`/`catch`/`finally` handlers |
| `3-all.js` | `handleProfileSignup` - `Promise.all` over `uploadPhoto`/`createUser` |
| `4-user-promise.js` | `signUpUser` - resolves with `{ firstName, lastName }` |
| `5-photo-reject.js` | `uploadPhoto` - always rejects with a processing error |
| `6-final-user.js` | `handleProfileSignup` - `Promise.allSettled` over both, mapped to `{status, value}` |
| `7-load_balancer.js` | `loadBalancer` - `Promise.race` between two downloads |
| `8-try.js` | `divideFunction` - throws on division by zero |
| `9-try.js` | `guardrail` - runs a function, always records that it ran |
| `utils.js` | `uploadPhoto`/`createUser` helpers used by task 3 |

## Usage
```
npx babel-node 0-main.js
npm test
npm run full-test
```
