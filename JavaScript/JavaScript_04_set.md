# JavaScript_04_set

## ✨ 교집합

```javascript
Set.prototype.intersection = function (set) {
  return new Set([...this].filter(v => set.has(v)))
}

const setA = new Set([1, 2, 3, 4])
const setB = new Set([2, 4])
console.log(setA.intersection(setB))      // Set(2) { 2, 4 }
```

<br/>

## ✨ 합집합

```javascript
Set.prototype.union = function (set) {
  return new Set([...this, ...set])
}

const setA = new Set([1, 2, 3, 4])
const setB = new Set([2, 4])
console.log(setA.union(setB))             // Set(4) { 1, 2, 3, 4 }
```

<br/>

## ✨ 차집합

```javascript
Set.prototype.difference = function (set) {
  return new Set([...this].filter(v => !set.has(v)))
}

const setA = new Set([1, 2, 3, 4])
const setB = new Set([2, 4])
console.log(setA.difference(setB))        // Set(2) { 1, 3 }
```

<br/>

## ✨ 부분 집합과 상위 집합

```javascript
Set.prototype.isSuperset = function (subset) {
  const supersetArr = [...this]
  return [...subset].every(v => supersetArr.includes(v))
}

const setA = new Set([1, 2, 3, 4])
const setB = new Set([2, 4])
console.log(setA.isSuperset(setB))        // true
```

