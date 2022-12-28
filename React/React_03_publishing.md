# React_03_publishing

## ✨ install

```bash
npm i gh-pages
```

<br/>

## ✨ package.json

```json
// package.json
{
  ...
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "deploy": "gh-pages -d build",                   // 작성
    "predeploy": "npm run build"                     // 작성
  },
  "homepage": "https://nimusmix.github.io/TIL"       // 코드가 있는 repo
}
```
