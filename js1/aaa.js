import fs from 'fs';
import crypto from 'crypto';

const alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

let t = 0;
let n = 6;

// バッファ
let buffer = [];

// 最初にファイル初期化
fs.writeFileSync('hashed.jsonl', '');

function generate(current) {
  if (current.length === n) {
    t++;

    const hash = crypto
      .createHash('sha256')
      .update(current)
      .digest('hex');

    // バッファに追加
    buffer.push(JSON.stringify({
      original: current,
      hash: hash
    }));

    // 10000件ごとにまとめて書く
    if (buffer.length >= 10000) {
      fs.appendFileSync('hashed.jsonl', buffer.join('\n') + '\n');
      buffer = [];
      console.log(t);
    }

    return;
  }

  for (let i = 0; i < alpha.length; i++) {
    generate(current + alpha[i]);
  }
}

generate("");

// 残りを書き込む
if (buffer.length > 0) {
  fs.appendFileSync('hashed.jsonl', buffer.join('\n') + '\n');
}

console.log("combination : " + t);