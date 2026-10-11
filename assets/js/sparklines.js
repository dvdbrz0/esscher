(function () {
  // Word-sized line charts (Tufte's sparklines) next to each figure in the markets band,
  // drawn from the closing levels recorded in earlier daily editions.
  var band = document.querySelector(".ticker[data-markets]");
  if (!band || !window.fetch) return;
  var upTo = band.getAttribute("data-date") || "9999-99-99";
  var SVG = "http://www.w3.org/2000/svg";

  function num(v) {
    var x = parseFloat(String(v).replace(/[^0-9.\-]/g, ""));
    return isFinite(x) ? x : null;
  }

  fetch(band.getAttribute("data-markets"))
    .then(function (r) { return r.json(); })
    .then(function (editions) {
      var seen = {};
      var rows = editions
        .filter(function (e) { if (e.date > upTo || seen[e.date] || !e.ticker) return false; seen[e.date] = 1; return true; })
        .sort(function (a, b) { return a.date < b.date ? -1 : 1; })
        .slice(-10);
      band.querySelectorAll(".tick[data-label]").forEach(function (tick) {
        var label = tick.getAttribute("data-label");
        var series = [];
        rows.forEach(function (e) {
          e.ticker.forEach(function (t) { if (t.label === label) { var v = num(t.value); if (v !== null) series.push(v); } });
        });
        if (series.length < 2) return;
        var w = 46, h = 14, pad = 2;
        var min = Math.min.apply(null, series), max = Math.max.apply(null, series);
        var span = max - min || 1;
        var pts = series.map(function (v, i) {
          var x = pad + (i * (w - 2 * pad)) / (series.length - 1);
          var y = h - pad - ((v - min) / span) * (h - 2 * pad);
          return [x, y];
        });
        var svg = document.createElementNS(SVG, "svg");
        svg.setAttribute("class", "spark");
        svg.setAttribute("width", w);
        svg.setAttribute("height", h);
        svg.setAttribute("viewBox", "0 0 " + w + " " + h);
        svg.setAttribute("aria-hidden", "true");
        var line = document.createElementNS(SVG, "polyline");
        line.setAttribute("points", pts.map(function (p) { return p[0].toFixed(1) + "," + p[1].toFixed(1); }).join(" "));
        line.setAttribute("fill", "none");
        line.setAttribute("stroke", "currentColor");
        line.setAttribute("stroke-width", "1.2");
        line.setAttribute("stroke-linejoin", "round");
        svg.appendChild(line);
        var last = pts[pts.length - 1];
        var dot = document.createElementNS(SVG, "circle");
        dot.setAttribute("cx", last[0].toFixed(1));
        dot.setAttribute("cy", last[1].toFixed(1));
        dot.setAttribute("r", "1.8");
        dot.setAttribute("class", series[series.length - 1] >= series[series.length - 2] ? "spark-end up" : "spark-end down");
        svg.appendChild(dot);
        tick.setAttribute("title", label + ", last " + series.length + " editions");
        tick.appendChild(svg);
      });
    })
    .catch(function () {});
})();
