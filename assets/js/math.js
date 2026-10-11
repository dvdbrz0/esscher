(function () {
  // Typeset formulas written as \( ... \) or \[ ... \] on pages where the layout
  // did not already load KaTeX (front-page summaries, topic lists, related stories).
  if (window.renderMathInElement) return;
  var main = document.querySelector("main");
  if (!main) return;
  var text = main.textContent;
  if (text.indexOf("\\(") === -1 && text.indexOf("\\[") === -1) return;
  var me = document.currentScript;
  var base = (me && me.getAttribute("data-base")) || "/assets/katex/";
  var css = document.createElement("link");
  css.rel = "stylesheet";
  css.href = base + "katex.min.css";
  document.head.appendChild(css);
  function load(src, done) {
    var s = document.createElement("script");
    s.src = src;
    s.onload = done;
    document.head.appendChild(s);
  }
  load(base + "katex.min.js", function () {
    load(base + "contrib/auto-render.min.js", function () {
      renderMathInElement(main, {
        delimiters: [{ left: "\\[", right: "\\]", display: true }, { left: "\\(", right: "\\)", display: false }],
        throwOnError: false
      });
    });
  });
})();
