(function () {
  // Puts delayed quotes into the markets band on the front page and the latest edition.
  // They come from /live.json on this site, refreshed on weekdays by a scheduled job
  // (scripts/live_markets.py), so the reader's browser asks no one else. Quotes are used
  // only when they are newer than the close the edition reports; otherwise the edition's
  // figures stay. The page checks again every five minutes while it is open.
  var band = document.querySelector(".ticker[data-live]");
  if (!band || !window.fetch) return;
  var url = band.getAttribute("data-live");
  var closeDate = band.getAttribute("data-asof") || "";
  var label = band.querySelector(".ticker-label");
  var source = band.querySelector(".ticker-source");
  var shown = "";

  function sameDay(a, b) {
    return a.getFullYear() === b.getFullYear() && a.getMonth() === b.getMonth() && a.getDate() === b.getDate();
  }

  function when(d) {
    var time = d.toLocaleTimeString("en-GB", { hour: "2-digit", minute: "2-digit" });
    if (sameDay(d, new Date())) return time;
    return d.toLocaleDateString("en-GB", { weekday: "short" }) + " " + time;
  }

  function apply(live) {
    if (!live || !live.asof || !live.quotes || !live.quotes.length || live.asof === shown) return;
    var asof = new Date(live.asof);
    if (isNaN(asof.getTime())) return;
    // The edition's close is the record; quotes from that day or earlier add nothing.
    if (closeDate && live.asof.slice(0, 10) <= closeDate) return;
    live.quotes.forEach(function (q) {
      var tick = band.querySelector('.tick[data-label="' + q.label.replace(/"/g, '\\"') + '"]');
      if (!tick) return;
      var value = tick.querySelector(".tick-value");
      var change = tick.querySelector(".tick-change");
      if (value) value.textContent = q.value;
      if (change) {
        change.textContent = q.change || "";
        change.className = "tick-change" + (q.dir === "down" ? " down" : q.dir === "up" ? " up" : "");
      }
      var t = new Date(q.time);
      if (!isNaN(t.getTime())) tick.setAttribute("title", q.label + " at " + when(t) + ", delayed. Opens the full quote.");
      tick.classList.remove("is-empty");
    });
    if (label) {
      label.textContent = "Markets";
      label.setAttribute("title", "Quotes as of " + asof.toLocaleString("en-GB", { weekday: "long", day: "numeric", month: "long", hour: "2-digit", minute: "2-digit" }) +
        ", delayed. Source: " + (live.source || "") + ". Policy rates are from the day's edition.");
    }
    if (source) source.textContent = "As of " + when(asof) + ". " + (live.source || "") + ", delayed.";
    shown = live.asof;
    window.dispatchEvent(new Event("resize"));
  }

  function load() {
    fetch(url + "?t=" + Date.now(), { cache: "no-store" })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(apply)
      .catch(function () {});
  }

  load();
  setInterval(function () { if (!document.hidden) load(); }, 5 * 60 * 1000);
})();
