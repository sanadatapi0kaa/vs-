import fs from 'fs';

const text = fs.readFileSync("3-F.txt", "utf-8");
const lines = text.split("\n");

const counter = {};

for (const line of lines) {
  const parts = line.trim().split("\t");

  if (parts.length >= 2) {
    const name = parts[1];

    if (!counter[name]) {
      counter[name] = 0;
    }
    counter[name]++;
  }
}

// 多い順にソート
const sorted = Object.entries(counter).sort((a, b) => b[1] - a[1]);
console.log("発言数一覧");
console.log("集計期間： 25/4/16 ~");
for (const [name, count] of sorted) {
  console.log(`${name}: ${count}`);
}