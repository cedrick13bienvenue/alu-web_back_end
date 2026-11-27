# ES6 data manipulation

## Description
Eleven exercises on working with data in ES6: `map`, `filter`, and
`reduce` on arrays, typed arrays through `ArrayBuffer` and `DataView`,
and the `Set` and `Map` data structures.

## Resources
- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [Typed Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays)
- [Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
- [Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [WeakMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)

## Learning Objectives
By the end of this project, you should be able to explain, without Google:
- How to use `map`, `filter`, and `reduce` on arrays
- Typed arrays
- The `Set`, `Map`, and weak link data structures

## Requirements
- All files executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- All files end with a new line
- Code uses the `.js` extension
- Tested with Jest (`npm run test`), linted with ESLint
- The whole project passes `npm run full-test`
- All functions are exported

## Setup
```
npm install
```

## Tasks
| File | Description |
| --- | --- |
| `0-get_list_students.js` | `getListStudents` - the list of student objects |
| `1-get_list_student_ids.js` | `getListStudentIds` - student ids via `map`, `[]` for non-arrays |
| `2-get_students_by_loc.js` | `getStudentsByLocation` - students in a city via `filter` |
| `3-get_ids_sum.js` | `getStudentIdsSum` - sum of ids via `reduce` |
| `4-update_grade_by_city.js` | `updateStudentGradeByCity` - `filter` + `map`, `N/A` when no grade |
| `5-typed_arrays.js` | `createInt8TypedArray` - Int8 value in a `DataView`, throws `Position outside range` |
| `6-set.js` | `setFromArray` - a `Set` from an array |
| `7-has_array_values.js` | `hasValuesFromArray` - whether every array value is in the set |
| `8-clean_set.js` | `cleanSet` - prefixed values with the prefix stripped, joined by `-` |
| `9-groceries_list.js` | `groceriesList` - the groceries `Map` |
| `10-update_uniq_items.js` | `updateUniqueItems` - quantities of 1 become 100, throws `Cannot process` |

## Usage
```
npx babel-node 0-main.js
npm run test
npm run full-test
```
