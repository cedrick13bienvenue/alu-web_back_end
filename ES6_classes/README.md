# ES6 classes

## Description
Eleven exercises on ES6 classes: constructors, getters and setters with
type checks, methods and static methods, inheritance and abstract-style
base classes, and metaprogramming with well-known symbols
(`Symbol.toStringTag`, `Symbol.toPrimitive`, `Symbol.species`).

## Resources
- [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
- [Metaprogramming](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming)

## Learning Objectives
By the end of this project, you should be able to explain, without Google:
- How to define a class
- How to add methods to a class
- Why and how to add a static method to a class
- How to extend a class from another
- Metaprogramming and symbols

## Requirements
- All files executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- All files end with a new line
- Code uses the `.js` extension
- Tested with Jest (`npm run test`), linted with ESLint
- The whole project passes `npm run full-test`

## Setup
```
npm install
```

## Tasks
| File | Description |
| --- | --- |
| `0-classroom.js` | `ClassRoom` - stores `maxStudentsSize` |
| `1-make_classrooms.js` | `initializeRooms` - three classrooms of size 19, 20, and 34 |
| `2-hbtn_course.js` | `ALXCourse` - type-checked getters and setters for name, length, students |
| `3-currency.js` | `Currency` - getters/setters and `displayFullCurrency` |
| `4-pricing.js` | `Pricing` - `displayFullPrice` and static `convertPrice` |
| `5-building.js` | `Building` - abstract-style base requiring `evacuationWarningMessage` |
| `6-sky_high.js` | `SkyHighBuilding` - extends `Building` with floors |
| `7-airport.js` | `Airport` - default string description is its code |
| `8-hbtn_class.js` | `ALXClass` - casts to its size (number) or location (string) |
| `9-hoisting.js` | Fixed hoisting bugs; default-exports `listOfStudents` |
| `10-car.js` | `Car` - `cloneCar` returns a new instance of the same (sub)class |

## Usage
```
npx babel-node 0-main.js
npm run test
npm run full-test
```
