// 매매일지 페이지를 아티팩트와 같은 껍데기로 감싸 브라우저에 띄우고,
// 스크립트 문법을 확인한 뒤 PC(밝은 테마)·휴대폰(어두운 테마) 스크린샷을 찍는다.
// 저장소 기능은 없으므로 예시 데이터를 넣어 화면만 확인한다. (예시 값은 실제 사용자 숫자가 아님)
//
// 사용법: node trading-journal/dev/preview.js [탭] [출력 폴더]
//   탭: open | closed | stats | goal | rules  (기본: open)
const { chromium } = require("playwright");
const { execFileSync } = require("child_process");
const fs = require("fs");
const os = require("os");
const path = require("path");

const tab = process.argv[2] || "open";
const outDir = process.argv[3] || fs.mkdtempSync(path.join(os.tmpdir(), "journal-preview-"));
const src = fs.readFileSync(path.join(__dirname, "..", "index.html"), "utf8");

// 1) 문법 확인
const script = src.slice(src.indexOf("<script>") + 8, src.lastIndexOf("</script>"));
const jsFile = path.join(outDir, "page.js");
fs.writeFileSync(jsFile, script);
execFileSync(process.execPath, ["--check", jsFile], { stdio: "inherit" });
console.log("문법 OK");

// 2) 아티팩트 게시 때와 같은 기본 껍데기
const shell = '<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover">' +
  "<style>:root{color-scheme:light;padding:env(safe-area-inset-top,0) 0 env(safe-area-inset-bottom,0)}body{margin:0;font:14px system-ui}img{max-width:100%}[hidden]{display:none!important}</style>" +
  "</head><body>" + src + "</body></html>";
const htmlFile = path.join(outDir, "page.html");
fs.writeFileSync(htmlFile, shell);

const SAMPLE = () => {
  const d = (m) => `2026-${m}`;
  state.settings = { ...state.settings, capital: 50000000, maxWeight: 20, maxLossPct: 2, currentAssets: 300000000,
    sim: { total: 300000000, invest: 50000000, monthly: 2000000, saveGrowth: 0, rate: 10, otherGrowth: 3, age: 40, years: 20 } };
  state.assets = [["06", 2.9e8, 4.6e7], ["07", 2.95e8, 4.8e7], ["08", 2.97e8, 4.9e7], ["09", 3.0e8, 5.0e7]]
    .map(([m, t, i]) => ({ id: d(m), month: d(m), total: t, invest: i, memo: "" }));
  state.trades = [
    { id: "a", name: "예시전자", buyDate: "2026-09-01", buyPrice: 70000, qty: 50, target: 84000, stop: 64000, reason: "예시 매수 이유", emotion: "차분함", horizon: "몇 달", violations: [], status: "open", currentPrice: 73000 },
    { id: "b", name: "예시화학", buyDate: "2026-07-01", buyPrice: 50000, qty: 40, target: 60000, stop: 46000, reason: "예시", emotion: "남들 따라(FOMO)", violations: ["체크 안 함: 예시"], status: "closed", sellDate: "2026-08-01", sellPrice: 44000, sellReason: "emotion" },
    { id: "c", name: "예시금융", buyDate: "2026-06-01", buyPrice: 20000, qty: 100, target: 24000, stop: 18500, reason: "예시", emotion: "확신", violations: [], status: "closed", sellDate: "2026-07-10", sellPrice: 24200, sellReason: "target" },
  ];
};

(async () => {
  const browser = await chromium.launch();
  for (const [width, scheme] of [[1000, "light"], [390, "dark"]]) {
    const page = await browser.newPage({ viewport: { width, height: 900 }, colorScheme: scheme });
    const errors = [];
    page.on("pageerror", (e) => errors.push(e.message));
    await page.goto("file://" + htmlFile);
    await page.evaluate(`(${SAMPLE})(); state.tab = ${JSON.stringify(tab)}; render();`);
    await page.waitForTimeout(400);
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth);
    const file = path.join(outDir, `${tab}-${width}-${scheme}.png`);
    await page.screenshot({ path: file, fullPage: true });
    console.log(`${file}  오류: ${errors.length ? errors.join(" | ") : "없음"}  가로 넘침: ${overflow ? "있음" : "없음"}`);
  }
  await browser.close();
})();
