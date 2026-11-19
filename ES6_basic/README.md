# ES6 Basics

## Description
Thirteen small exercises covering ES6 syntax: `const`/`let`, block
scoping, arrow functions, default/rest/spread parameters, template
literals, shorthand and computed property names, method properties, and
`for...of` loops.

## Resources
- [ECMAScript 6 - ECMAScript 2015](https://devdocs.io/javascript/)
- [Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
- [Default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
- [Rest parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)

## Learning Objectives
By the end of this project, you should be able to explain, without Google:
- What ES6 is, and the new features it introduced
- The difference between a constant and a variable
- Block-scoped variables
- Arrow functions and function parameter defaults
- Rest and spread function parameters
- String templating in ES6
- Object creation and their properties in ES6
- Iterators and `for...of` loops

## Requirements
- All files executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- All files end with a new line
- Code uses the `.js` extension
- Code is tested with Jest and linted with ESLint
- All functions are exported

## Setup
```
npm install
```

## Tasks
| File | Description |
| --- | --- |
| `0-constants.js` | `taskFirst`/`taskNext` - `const` and `let` instead of `var` |
| `1-block-scoped.js` | `taskBlock` - block-scoped variables that don't leak out of an `if` |
| `2-arrow.js` | `getNeighborhoodsList` - an arrow function instead of `self = this` |
| `3-default-parameter.js` | `getSumOfHoods` - default parameter values |
| `4-rest-parameter.js` | `returnHowManyArguments` - counts arguments via rest syntax |
| `5-spread-operator.js` | `concatArrays` - concatenates arrays and a string via spread syntax |
| `6-string-interpolation.js` | `getSanFranciscoDescription` - a template literal |
| `7-getBudgetObject.js` | `getBudgetObject` - object property shorthand |
| `8-getBudgetCurrentYear.js` | `getBudgetForCurrentYear` - computed property names |
| `9-getFullBudget.js` | `getFullBudgetObject` - ES6 method properties |
| `10-loops.js` | `appendToEachArrayValue` - a `for...of` loop instead of `for...in` |
| `11-createEmployeesObject.js` | `createEmployeesObject` - builds a department-keyed object |
| `12-createReportObject.js` | `createReportObject` - summarizes employees with a method property |

## Usage
```
npx babel-node 0-main.js
npm test
npm run full-test
```

## Verification notes
Every task was run against the exact `*-main.js` example from the
project page (not committed here, since only the numbered task files
are graded) with real Node 12 + Babel, and matched the expected output.
`1-block-scoped.js` intentionally triggers `no-unused-vars` on its
shadowed inner bindings (that's the whole point of the exercise), so
those two lines carry a scoped `eslint-disable-next-line` rather than
weakening the rule project-wide.
