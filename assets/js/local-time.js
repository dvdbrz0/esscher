(function () {
  // Times are written in UTC in the page; show them in the reader's own time zone.
  // data-local says how much to show: day-date-time, full-date-time, date-time, short-date-time or time.
  if (!window.Intl || !Intl.DateTimeFormat || !Intl.DateTimeFormat.prototype.formatToParts) return;
  var opts = {
    "day-date-time": { weekday: "long", day: "numeric", month: "long", year: "numeric" },
    "date-time": { day: "numeric", month: "long" },
    "full-date-time": { day: "numeric", month: "long", year: "numeric" },
    "short-date-time": { day: "numeric", month: "short", year: "numeric" },
    "time": {}
  };
  document.querySelectorAll("time[data-local]").forEach(function (el) {
    var kind = el.getAttribute("data-local");
    var d = new Date(el.getAttribute("datetime"));
    if (!opts[kind] || isNaN(d)) return;
    try {
      var o = Object.assign({ hour: "2-digit", minute: "2-digit", hourCycle: "h23", timeZoneName: "short" }, opts[kind]);
      var p = {};
      new Intl.DateTimeFormat("en-GB", o).formatToParts(d).forEach(function (x) { p[x.type] = x.value; });
      var date = [p.weekday, p.day, p.month, p.year].filter(Boolean).join(" ");
      var time = p.hour + ":" + p.minute + " " + p.timeZoneName;
      el.textContent = date ? date + ", " + time : time;
      el.title = el.getAttribute("datetime").replace("T", " ").replace(/:\d\dZ$|Z$/, "") + " UTC";
    } catch (e) { /* keep the UTC text */ }
  });
})();
